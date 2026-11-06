#!/usr/bin/env python3
"""Profile-permission tests for the Supabase feasibility prototype.

Two kinds of check, reported separately because they are different evidence:

* **Lint** (always runs): reads the migrations and asserts the *shape* of the
  privilege model — no table-wide write grant on `profiles`, a column grant on
  `display_name` only, RLS enabled, the guard trigger present, and every
  required case represented in the SQL test file. This proves the migration
  says the right thing. It does **not** prove the database behaves that way.

* **Integration** (runs only with a database): executes
  `tests/sql/profile_permissions.test.sql` through psycopg against
  `$DATABASE_URL` or `$SUPABASE_DB_URL` (with migrations 0001–0005 applied).
  Without a driver or a URL the case is reported **BLOCKED**, never PASS.

Run:
    python prototypes/supabase-feasibility/tests/test_profile_permissions.py
    DATABASE_URL=... python prototypes/supabase-feasibility/tests/test_profile_permissions.py --integration
Exit: 0 all executed checks pass; 1 a check failed; 77 integration BLOCKED.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
MIGRATIONS = ROOT.parent / "migrations"
SQL_TEST = ROOT / "sql" / "profile_permissions.test.sql"

REQUIRED_CASES = [
    "user updates own display_name (allowed)",
    "user cannot update own profiles.treasury (denied)",
    "user cannot update own nations.treasury (denied)",
    "user cannot update another user's profile (0 rows)",
    "user cannot modify another nation's treasury (denied)",
    "SECURITY DEFINER path cannot change profiles.treasury (denied)",
    "authorized server operation still credits nations.treasury",
]


def read_all_migrations() -> dict[str, str]:
    """Read every migration keyed by filename, in application order."""
    return {p.name: p.read_text(encoding="utf-8") for p in sorted(MIGRATIONS.glob("*.sql"))}


WRITE_PRIVILEGES = {"insert", "update", "delete", "truncate"}


def _split_privileges(priv_text: str) -> list[str]:
    """Split a GRANT/REVOKE privilege list on commas outside parentheses."""
    return [p.strip() for p in re.split(r",(?![^()]*\))", priv_text) if p.strip()]


def _table_wide_write(priv_text: str) -> set[str]:
    """Write privileges this list grants across the whole table.

    `update (display_name)` is column-scoped, so it is deliberately excluded;
    `select, insert, update` and `all` include table-wide write privileges.
    """
    out: set[str] = set()
    for priv in _split_privileges(priv_text):
        if "(" in priv:
            continue
        head = priv.strip().lower()
        if head in ("all", "all privileges"):
            out |= WRITE_PRIVILEGES
        elif head in WRITE_PRIVILEGES:
            out.add(head)
    return out


def _roles(role_text: str) -> set[str]:
    """Normalise a GRANT/REVOKE role list."""
    return {r.strip().strip('"').lower() for r in role_text.split(",") if r.strip()}


def final_profile_write_state(docs: dict[str, str]) -> dict[str, set[str]]:
    """Replay GRANT/REVOKE on `feasibility.profiles` in migration order.

    A grant earlier in the chain does not fail the lint if a later migration
    revokes it; the check reports the *final* state. Column grants never mark a
    table-wide write.
    """
    state: dict[str, set[str]] = {}
    for name in sorted(docs):
        sql = re.sub(r"--[^\n]*", "", docs[name])
        for statement in sql.split(";"):
            text = " ".join(statement.split())
            match = re.match(
                r"(?is)^(grant|revoke)\s+(.+?)\s+on\s+(?:table\s+)?"
                r"(?:feasibility\.)?profiles\s+(?:to|from)\s+(.+)$",
                text,
            )
            if not match:
                continue
            action, priv_text, role_text = match.group(1).lower(), match.group(2), match.group(3)
            roles = _roles(role_text)
            if action == "grant":
                writes = _table_wide_write(priv_text)
                for role in roles:
                    state.setdefault(role, set()).update(writes)
            else:
                privs = _split_privileges(priv_text)
                if any(p.strip().lower() in ("all", "all privileges") for p in privs):
                    for role in roles:
                        state.setdefault(role, set()).clear()
                else:
                    removed = {re.sub(r"\(.*\)", "", p).strip().lower() for p in privs}
                    for role in roles:
                        state.setdefault(role, set()).difference_update(removed)
    return state


def lint() -> list[tuple[str, bool, str]]:
    """Statically check that no migration leaves a table-wide profile write."""
    docs = read_all_migrations()
    corrective = docs.get("0005_profile_column_privileges.sql", "")
    schema = docs.get("0001_schema.sql", "")
    results: list[tuple[str, bool, str]] = []

    final_writes = final_profile_write_state(docs)
    offending = {role: sorted(privs) for role, privs in final_writes.items() if privs}
    results.append(("no migration leaves a table-wide write grant on profiles",
                    not offending,
                    f"final write state: {offending}" if offending else "none"))

    results.append((
        "0005 revokes table-wide UPDATE before granting a column",
        bool(re.search(r"revoke\s+update\s+on\s+table\s+feasibility\.profiles\s+from\s+authenticated", corrective, re.I))
        and bool(re.search(r"grant\s+update\s*\(\s*display_name\s*\)\s+on\s+table\s+feasibility\.profiles\s+to\s+authenticated", corrective, re.I)),
        "revoke + column grant present"))

    results.append((
        "0005 grants no other column",
        len(re.findall(r"grant\s+update\s*\(([^)]*)\)", corrective, re.I)) == 1,
        "exactly one column-level grant"))

    results.append((
        "profiles has row-level security enabled",
        bool(re.search(r"alter\s+table\s+feasibility\.profiles\s+enable\s+row\s+level\s+security", schema, re.I)),
        "RLS enabled in 0001"))

    results.append((
        "an own-row UPDATE policy exists",
        bool(re.search(r"create\s+policy\s+\w+\s+on\s+feasibility\.profiles\s+for\s+update\s+to\s+authenticated", schema, re.I)),
        "policy present in 0001"))

    results.append((
        "the guard trigger refuses server-authoritative columns",
        "profiles_guard_server_columns" in corrective
        and "profiles.treasury is server-authoritative" in corrective
        and bool(re.search(r"create\s+trigger\s+profiles_guard_server_columns", corrective, re.I)),
        "trigger defined in 0005"))

    results.append((
        "the correction is re-applicable",
        "drop trigger if exists" in corrective.lower()
        and "create or replace function" in corrective.lower(),
        "idempotent statements"))

    test_sql = SQL_TEST.read_text(encoding="utf-8") if SQL_TEST.exists() else ""
    # The SQL file escapes apostrophes as ''; normalise before matching notices.
    normalised = test_sql.replace("''", "'")
    missing = [case for case in REQUIRED_CASES if case not in normalised]
    results.append(("the SQL test file covers all seven required cases",
                    not missing, f"missing: {missing}" if missing else "7/7 present"))

    results.append((
        "the test file rolls back and asserts with exceptions",
        "rollback;" in test_sql and "raise exception 'FAIL" in test_sql,
        "transactional, fail-loud test"))

    # Sanity: no migration may point the guard at the wrong schema.
    results.append((
        "the corrective migration targets the feasibility schema",
        "feasibility.profiles" in corrective and "public.profiles" not in corrective,
        "schema matches 0001"))
    return results


def _strip_psql_meta_commands(sql: str) -> str:
    """Remove client-only psql commands (`\\set`, `\\echo`, …) before execution.

    The connecting driver speaks the PostgreSQL wire protocol, not psql's
    meta-language; sending `\\set` or `\\echo` to the server raises a syntax
    error. Only backslash-command lines are removed; every SQL statement and
    the fail-fast `raise exception` assertions are kept.
    """
    return "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("\\"))


def integration() -> tuple[str, str]:
    """Return (status, detail) where status is PASS, FAIL or BLOCKED."""
    url = os.environ.get("DATABASE_URL") or os.environ.get("SUPABASE_DB_URL")
    if not url:
        return "BLOCKED", "no DATABASE_URL / SUPABASE_DB_URL in the environment"
    driver = None
    for name in ("psycopg", "psycopg2"):
        try:
            driver = __import__(name)
            break
        except ImportError:
            continue
    if driver is None:
        return "BLOCKED", "neither psycopg nor psycopg2 is installed"
    if not SQL_TEST.exists():
        return "BLOCKED", "the SQL test file is missing"
    sql = _strip_psql_meta_commands(SQL_TEST.read_text(encoding="utf-8"))
    try:
        conn = driver.connect(url)
    except Exception as exc:  # connection refused, bad credentials, no network
        return "BLOCKED", f"could not connect: {exc}"
    try:
        with conn.cursor() as cur:
            # The test begins with `set role authenticated`; prove the
            # connecting role may do that before blaming the SQL.
            cur.execute("select current_user")
            user = cur.fetchone()[0]
            cur.execute("select coalesce(rolsuper, false) from pg_roles where rolname = current_user")
            row = cur.fetchone()
            superuser = bool(row[0]) if row else False
            cur.execute("select pg_has_role(current_user, 'authenticated', 'MEMBER')")
            member = bool(cur.fetchone()[0])
        if not (superuser or member):
            return "BLOCKED", f"role {user!r} cannot SET ROLE authenticated"
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.rollback()
        return "PASS", "profile_permissions.test.sql executed on a live database"
    except Exception as exc:
        conn.rollback()
        return "FAIL", f"{exc}"
    finally:
        conn.close()


def main(argv: list[str]) -> int:
    """Run the lint, optionally the integration test, and return the exit code."""
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--integration", action="store_true",
                    help="also attempt the live-database test")
    args = ap.parse_args(argv)

    print("PROFILE PERMISSION LINT (migration shape, not database behaviour)")
    failures = 0
    for name, ok, detail in lint():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")
        failures += 0 if ok else 1
    print(f"  lint: {len(lint()) - failures}/{len(lint())} passed")

    status = "NOT RUN"
    detail = "integration not requested"
    if args.integration:
        status, detail = integration()
        print(f"\nPROFILE PERMISSION INTEGRATION: {status} — {detail}")

    print("\nRESULT:")
    print(f"  lint: {'PASS' if failures == 0 else 'FAIL'}")
    print(f"  integration: {status}")
    print("  A static migration lint is NOT proof that the database enforces the policy.")
    if failures:
        return 1
    if args.integration and status in ("BLOCKED", "FAIL"):
        return 77 if status == "BLOCKED" else 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
