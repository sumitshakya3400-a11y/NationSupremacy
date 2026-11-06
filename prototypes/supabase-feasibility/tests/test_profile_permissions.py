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
    return {p.name: p.read_text(encoding="utf-8") for p in sorted(MIGRATIONS.glob("*.sql"))}


def lint() -> list[tuple[str, bool, str]]:
    docs = read_all_migrations()
    joined = "\n".join(docs.values())
    corrective = docs.get("0005_profile_column_privileges.sql", "")
    schema = docs.get("0001_schema.sql", "")
    results: list[tuple[str, bool, str]] = []

    table_wide = [
        name for name, text in docs.items()
        if re.search(r"grant\s+(?:all|update|insert)\b[^;]*\bon\s+(?:table\s+)?feasibility\.profiles",
                     text, re.I)
        and not re.search(r"revoke\s+(?:all|update|insert)\b[^;]*\bfeasibility\.profiles", text, re.I)
    ]
    results.append(("no migration leaves a table-wide write grant on profiles",
                    not table_wide, f"offending files: {table_wide}" if table_wide else "none"))

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
    del joined
    return results


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
    sql = SQL_TEST.read_text(encoding="utf-8")
    try:
        conn = driver.connect(url)
    except Exception as exc:  # connection refused, bad credentials, no network
        return "BLOCKED", f"could not connect: {exc}"
    try:
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
