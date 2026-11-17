#!/usr/bin/env python3
"""Prompt 14A controlled numerical-contract validator (documentation QA only).

Implements the canonical contract architecture adopted by D-238:

* strict schema validation for the contract registry, two B-04 contracts,
  the canonical lexicon and the reviewed-evidence mappings;
* deterministic rendering of the two controlled B-04 clauses and 100 %
  material-coverage verification;
* a closed-vocabulary ingestion parser for prose amendments (migration and
  diagnostic path only -- semantic changes must arrive as typed contract
  patches);
* typed proposition diffs;
* an evidence gate and a separate D-014 authority gate;
* deterministic fingerprints for contracts, projections, source Markdown and
  evidence documents;
* regression fixtures for the six mandatory negative classes and the required
  positive cases.

Python standard library only. No network, no model inference, no randomness.
A passing result is documentation-level consistency only; it does not prove
gameplay, balance, runtime behaviour or owner acceptance.

Usage:
    python 14A_contract_validator.py
    python 14A_contract_validator.py --json
    python 14A_contract_validator.py --seal
    python 14A_contract_validator.py --write-report PATH
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

THIS = os.path.abspath(__file__)
DOCS = os.path.dirname(os.path.dirname(THIS))
REPO = os.path.dirname(DOCS)
CONTRACTS = os.path.join(DOCS, "stage-2", "22_numerical_contracts")
B04 = os.path.join(DOCS, "stage-2", "10_economic_formula_and_balance_register.md")
B14 = os.path.join(DOCS, "stage-2", "22_formulas_and_balance.md")
B09 = os.path.join(DOCS, "stage-2", "16_alliances_formula_register.md")
DECISIONS = os.path.join(DOCS, "DECISIONS.md")
POLICY = os.path.join(DOCS, "AUTONOMOUS_DECISION_POLICY.md")
MANIFEST = os.path.join(DOCS, "qa_backups", "14A_b04_source_contract_amendments.json")
FIXTURES = os.path.join(DOCS, "qa_backups", "14A_contract_fixtures")

BASELINE_HASHES = {
    "F-EC-000b": "bb1090ccae5cd15e0d883a57ab63216a106ff7c4e503e85cf2146e19e02271c6",
    "F-EC-000f": "3025cc447ebb91be8d226ff5035da0e403947d2be603e81e535bbd5600bca5ca",
}
BASELINE_CLAUSES = {
    "F-EC-000b": "**F-EC-000b — Integer arithmetic.** *Provisional (REQ-162).* All quantities are integers. Every division states its rounding: `floor` (toward negative infinity for negative values; toward zero for the positive values used here), `ceil` or `round_half_up`. No formula uses binary floating point. A percentage is an integer in **basis points** (bp), where 10,000 bp = 100%.",
    "F-EC-000f": "**F-EC-000f — Constants are versioned.** *Provisional.* The constants below are the **v1.0 provisional calibration**, carried unchanged into v1.1 (see F-EC-044). They are not observed prices and not balance claims. Prompt 14 may change a value only by a new revision of this register.",
}
ADOPTION_DECISION = "D-238"
MANDATORY_CODES = {
    "CONTRACT_SCHEMA_INVALID",
    "CONTRACT_UNMAPPED_TERM",
    "CONTRACT_UNPARSED_MATERIAL_SEGMENT",
    "CONTRACT_PROJECTION_MISMATCH",
    "CONTRACT_PROPOSITION_CONFLICT",
    "CONTRACT_EXCEPTION_UNSUPPORTED",
    "CONTRACT_SCOPE_MISMATCH",
    "CONTRACT_EVIDENCE_MAPPING_MISSING",
    "CONTRACT_EVIDENCE_NOT_REVIEWED",
    "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
    "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
    "CONTRACT_AUTHORITY_MISMATCH",
    "CONTRACT_OWNER_AUTHORIZATION_MISSING",
}
EXTRA_CODES = {
    "CONTRACT_EVIDENCE_INTEGRITY_FAILED",
    "CONTRACT_FINGERPRINT_MISMATCH",
    "CONTRACT_MANIFEST_INVALID",
    "CONTRACT_NOT_IMPLEMENTED",
    "CONTRACT_TRUSTED_INPUT_OVERRIDE",
    "CONTRACT_REQUEST_SCHEMA_INVALID",
    "CONTRACT_UNAUTHORIZED_PATH",
    "CONTRACT_PATH_TRAVERSAL",
    "CONTRACT_COVERAGE_GAP",
    "CONTRACT_CONTRACT_FIELD_CHANGE",
    "CONTRACT_FIXTURE_MODE_FORBIDDEN",
}
SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema", "$id", "title", "description", "type", "required",
    "additionalProperties", "properties", "enum", "const", "pattern",
    "minLength", "minimum", "maximum", "items", "minItems", "maxItems",
    "uniqueItems", "minProperties", "maxProperties", "oneOf", "anyOf", "allOf", "$ref", "$defs",
}


# ---------------------------------------------------------------------------
# basic helpers
# ---------------------------------------------------------------------------
def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def write_text(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(data)


def write_json(path, obj):
    write_text(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def _reject_constant(value):
    raise ValueError(f"non-finite JSON number is not allowed: {value}")


def _no_duplicate_pairs(pairs):
    seen = {}
    for key, value in pairs:
        if key in seen:
            raise ValueError(f"duplicate JSON key: {key!r}")
        seen[key] = value
    return seen


def load_json_strict(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return json.load(fh, object_pairs_hook=_no_duplicate_pairs,
                         parse_constant=_reject_constant)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def canonical_json(obj):
    return (json.dumps(obj, sort_keys=True, ensure_ascii=False,
                       separators=(",", ":")) + "\n").encode("utf-8")


def contract_sha256(contract):
    return sha256_bytes(canonical_json(contract))


def projection_sha256(text):
    return sha256_bytes(text.encode("utf-8"))


def source_clause_sha256(text):
    return sha256_bytes(norm_text(text).encode("utf-8"))


def problem(code, path, message):
    if code not in MANDATORY_CODES and code not in EXTRA_CODES:
        raise ValueError(f"unregistered contract error code: {code}")
    return {"code": code, "path": path, "message": message}


def fmt(prob):
    return f"{prob['code']} path={prob['path']}: {prob['message']}"


def norm_text(text):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", lambda m: m.group(1), text or "")
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


def split_sentences(text):
    """Split normalized prose on sentence boundaries outside parentheses."""
    out, buf, depth = [], [], 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
        buf.append(ch)
        if depth == 0 and ch in ".!?" and (i + 1 >= len(text) or text[i + 1].isspace()):
            seg = "".join(buf).strip()
            if seg:
                out.append(seg)
            buf = []
        elif depth == 0 and ch == ";" and i + 1 < len(text) and text[i + 1].isspace():
            seg = "".join(buf).strip()
            if seg:
                out.append(seg)
            buf = []
        i += 1
    seg = "".join(buf).strip()
    if seg:
        out.append(seg)
    return out


def extract_clause(document, fid):
    for para in (document or "").split("\n\n"):
        if para.strip().startswith("**" + fid):
            return para.strip()
    return ""


def replace_clause(document, fid, new_clause):
    paras = document.split("\n\n")
    for i, para in enumerate(paras):
        if para.strip().startswith("**" + fid):
            paras[i] = new_clause.strip()
            return "\n\n".join(paras)
    raise ValueError(f"clause {fid} not found")


def section_block(document, section):
    token = (section or "").strip()
    if not token:
        return ""
    if token.startswith(("F-", "D-", "REQ-")):
        for para in document.split("\n\n"):
            if para.strip().startswith("**" + token) or para.strip().startswith("| " + token + " "):
                return para
        for line in document.splitlines():
            if re.match(r"^\|\s*" + re.escape(token) + r"\s*\|", line):
                return line
        heading = re.compile(r"^#{1,6}\s*" + re.escape(token) + r"(?:\s|$)", re.I)
        lines = document.splitlines()
        for i, line in enumerate(lines):
            if heading.match(line):
                return "\n".join(lines[i:i + 200])
        for line in document.splitlines():
            if token in line:
                return line
        return ""
    lines = document.splitlines()
    pat = re.compile(r"^#{1,6}\s*" + re.escape(token) + r"(?:\s|$)", re.I)
    for i, line in enumerate(lines):
        if pat.match(line):
            return "\n".join(lines[i:i + 160])
    for i, line in enumerate(lines):
        if token in line:
            return "\n".join(lines[i:i + 160])
    return ""


def substantive(text, minimum=30):
    low = (text or "").lower().strip()
    if len(low) < minimum or not re.search(r"[a-z]", low):
        return False
    if any(g in low for g in ("n/a", "none", "tbd", "placeholder", "generic",
                              "no evidence", "test only", "approved because confirmed")):
        return False
    return True


def marker(text, label, stops):
    pat = label + r"\s*[:\-]\s*(.*?)(?=" + "|".join(stops) + r"|$)"
    m = re.search(pat, text or "", re.I | re.S)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# strict JSON-schema subset validator
# ---------------------------------------------------------------------------
def schema_meta_problems(schema, path="$"):
    problems = []
    def walk(node, at):
        if isinstance(node, dict):
            for key, value in node.items():
                if key not in SUPPORTED_SCHEMA_KEYWORDS:
                    problems.append(problem(
                        "CONTRACT_SCHEMA_INVALID", f"{at}.{key}",
                        f"unsupported schema keyword {key!r}; the schema may not silently ignore constraints"))
            if "properties" in node and isinstance(node["properties"], dict):
                for key, value in node["properties"].items():
                    walk(value, f"{at}.properties.{key}")
            if "$defs" in node and isinstance(node["$defs"], dict):
                for key, value in node["$defs"].items():
                    walk(value, f"{at}.$defs.{key}")
            if "items" in node:
                walk(node["items"], f"{at}.items")
            if "additionalProperties" in node and isinstance(node["additionalProperties"], dict):
                walk(node["additionalProperties"], f"{at}.additionalProperties")
            for comb in ("oneOf", "anyOf", "allOf"):
                if comb in node and isinstance(node[comb], list):
                    for i, value in enumerate(node[comb]):
                        walk(value, f"{at}.{comb}[{i}]")
        elif isinstance(node, list):
            for i, value in enumerate(node):
                walk(value, f"{at}[{i}]")
    walk(schema, path)
    return problems


def resolve_ref(root, ref):
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported $ref: {ref}")
    node = root
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def _type_ok(value, name):
    if name == "object":
        return isinstance(value, dict)
    if name == "array":
        return isinstance(value, list)
    if name == "string":
        return isinstance(value, str)
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if name == "boolean":
        return isinstance(value, bool)
    if name == "null":
        return value is None
    return False


def validate_schema(instance, schema, root, path="$"):
    if schema is True:
        return []
    if schema is False:
        return [problem("CONTRACT_SCHEMA_INVALID", path, "the schema forbids this value")]
    if "$ref" in schema:
        return validate_schema(instance, resolve_ref(root, schema["$ref"]), root, path)
    problems = []
    if "allOf" in schema:
        for branch in schema["allOf"]:
            problems.extend(validate_schema(instance, branch, root, path))
    if "anyOf" in schema:
        if not any(not validate_schema(instance, branch, root, path) for branch in schema["anyOf"]):
            problems.append(problem("CONTRACT_SCHEMA_INVALID", path, "value matches none of the anyOf branches"))
    if "oneOf" in schema:
        matches = sum(1 for branch in schema["oneOf"]
                      if not validate_schema(instance, branch, root, path))
        if matches != 1:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"value must match exactly one oneOf branch; matched {matches}"))
        return problems
    if "type" in schema:
        names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(instance, name) for name in names):
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"expected type {names}, got {type(instance).__name__}"))
            return problems
    if "const" in schema and instance != schema["const"]:
        problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", path,
            f"expected the constant {schema['const']!r}, got {instance!r}"))
    if "enum" in schema and instance not in schema["enum"]:
        problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", path,
            f"value {instance!r} is not in the closed enumeration {schema['enum']}"))
    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"string {instance!r} does not match pattern {schema['pattern']!r}"))
        if "minLength" in schema and len(instance) < schema["minLength"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"string is shorter than minLength {schema['minLength']}"))
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"number {instance} is below the minimum {schema['minimum']}"))
        if "maximum" in schema and instance > schema["maximum"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"number {instance} is above the maximum {schema['maximum']}"))
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"array has {len(instance)} items; minItems is {schema['minItems']}"))
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"array has {len(instance)} items; maxItems is {schema['maxItems']}"))
        if "uniqueItems" in schema and schema["uniqueItems"]:
            seen = set()
            for i, item in enumerate(instance):
                key = json.dumps(item, sort_keys=True, ensure_ascii=False)
                if key in seen:
                    problems.append(problem(
                        "CONTRACT_SCHEMA_INVALID", f"{path}[{i}]",
                        "duplicate array item (uniqueItems)"))
                seen.add(key)
        if "items" in schema:
            for i, item in enumerate(instance):
                problems.extend(validate_schema(item, schema["items"], root, f"{path}[{i}]"))
    if isinstance(instance, dict):
        if "minProperties" in schema and len(instance) < schema["minProperties"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"object has {len(instance)} properties; minProperties is {schema['minProperties']}"))
        if "maxProperties" in schema and len(instance) > schema["maxProperties"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", path,
                f"object has {len(instance)} properties; maxProperties is {schema['maxProperties']}"))
        for key in schema.get("required", []):
            if key not in instance:
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", path,
                    f"missing mandatory field {key!r}"))
        props = schema.get("properties", {})
        for key, value in instance.items():
            if key in props:
                problems.extend(validate_schema(value, props[key], root, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", f"{path}.{key}",
                    f"unknown field {key!r} (additionalProperties is false)"))
            elif isinstance(schema.get("additionalProperties"), dict):
                problems.extend(validate_schema(
                    value, schema["additionalProperties"], root, f"{path}.{key}"))
    return problems


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------
def load_artifacts(contracts_dir=CONTRACTS, mode="production"):
    """Load the registry without validating it; validation is separate."""
    result = {"problems": [], "mode": mode, "dir": contracts_dir}
    try:
        index = load_json_strict(os.path.join(contracts_dir, "index.json"))
        schema = load_json_strict(os.path.join(contracts_dir, "schema.json"))
        lexicon = load_json_strict(os.path.join(contracts_dir, "lexicon.json"))
        mappings = load_json_strict(os.path.join(contracts_dir, "evidence_mappings.json"))
    except Exception as exc:
        result["problems"].append(problem(
            "CONTRACT_SCHEMA_INVALID", "$", f"registry file could not be parsed: {exc}"))
        return result
    result.update({"index": index, "schema": schema, "lexicon": lexicon,
                   "mappings": mappings, "contracts": {}, "referenced": {}})
    refs = index.get("contracts", []) if isinstance(index, dict) else []
    for ref in refs:
        rel = ref.get("path", "") if isinstance(ref, dict) else ""
        try:
            contract = load_json_strict(os.path.join(contracts_dir, rel))
            result["contracts"][contract.get("clause_id", rel)] = contract
            result["referenced"][ref.get("contract_id")] = ref
        except Exception as exc:
            result["problems"].append(problem(
                "CONTRACT_SCHEMA_INVALID", rel, f"contract could not be parsed: {exc}"))
    return result


class TrustedPathError(Exception):
    pass


class TrustedContext:
    """Trusted validation environment loaded from fixed repository paths.

    An amendment request never supplies or replaces any of these inputs. A
    fixture context may be constructed by the regression harness; the public
    production entry point always uses the cached repository context.
    """

    def __init__(self, repo_root=None, contracts_dir=None, fixture_mode=False):
        self.repo_root = os.path.realpath(repo_root or REPO)
        self.contracts_dir = os.path.realpath(contracts_dir or CONTRACTS)
        self.fixture_mode = fixture_mode
        self.problems = []
        self._load()

    def _load(self):
        self.b04_path = os.path.join(self.repo_root, "docs", "stage-2",
                                     "10_economic_formula_and_balance_register.md")
        self.b14_path = os.path.join(self.repo_root, "docs", "stage-2",
                                     "22_formulas_and_balance.md")
        self.b09_path = os.path.join(self.repo_root, "docs", "stage-2",
                                     "16_alliances_formula_register.md")
        self.decisions_path = os.path.join(self.repo_root, "docs", "DECISIONS.md")
        self.policy_path = os.path.join(self.repo_root, "docs",
                                        "AUTONOMOUS_DECISION_POLICY.md")
        self.artifacts = load_artifacts(self.contracts_dir)
        self.index = self.artifacts.get("index", {})
        self.schema = self.artifacts.get("schema", {})
        self.lexicon = self.artifacts.get("lexicon", {})
        self.mappings = self.artifacts.get("mappings", {})
        self.contracts = self.artifacts.get("contracts", {})
        self.contracts_by_id = {c["contract_id"]: c for c in self.contracts.values()}
        self.decisions_text = read(self.decisions_path)
        self.policy_text = read(self.policy_path)
        self.owner_authorizations = copy.deepcopy(
            self.index.get("owner_authorizations", []))
        if self.fixture_mode:
            self.problems = []
        else:
            self.problems = self._verify()

    def _verify(self):
        problems = list(self.artifacts.get("problems", []))
        problems.extend(validate_registry(self.artifacts, self.decisions_text,
                                          "production"))
        b04_text = read(self.b04_path)
        for clause, contract in self.contracts.items():
            source_text = b04_text if clause.startswith("F-EC-") else None
            problems.extend(validate_contract_semantics(
                contract, self.schema, self.lexicon, self.decisions_text,
                source_text, "production"))
            template_path = self.resolve_contract_artifact(
                contract.get("rendering", {}).get("template_path", ""))
            template_text = read(template_path)
            problems.extend(template_projection_problems(contract, template_text))
        evidence_problems, _ = evidence_integrity(
            self.mappings, self.contracts, "production", self.repo_root)
        problems.extend(evidence_problems)
        headers, records, malformed, dupes = parse_decisions(self.decisions_text)
        by_id = {r["_id"]: r for r in records}
        if ADOPTION_DECISION in dupes or ADOPTION_DECISION not in by_id:
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
                "the contract-adoption decision does not exist exactly once"))
        for did in ("D-014", "D-045", "D-064"):
            if did not in by_id:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{did}",
                    f"{did} is missing from the trusted decision register"))
        if self.index.get("preserved_baseline", {}).get("d014_policy_sha256") != \
                sha256_file(self.policy_path):
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", "$.index.preserved_baseline.d014_policy_sha256",
                "the D-014 policy file bytes do not match the trusted registry"))
        return problems

    def resolve(self, rel, root=None, must_exist=True):
        """Resolve a repository-relative path without traversal or symlinks."""
        if not isinstance(rel, str) or not rel:
            raise TrustedPathError("empty or non-string path")
        if os.path.isabs(rel) or re.match(r"^[A-Za-z]:", rel):
            raise TrustedPathError(f"absolute path is not permitted: {rel!r}")
        parts = [p for p in re.split(r"[\\/]+", rel) if p]
        if not parts or any(p in (".", "..") for p in parts):
            raise TrustedPathError(f"path traversal or ambiguous path: {rel!r}")
        base = os.path.realpath(root or self.repo_root)
        candidate = os.path.realpath(os.path.join(base, *parts))
        if candidate != base and not candidate.startswith(base + os.sep):
            raise TrustedPathError(f"path escapes the trusted root: {rel!r}")
        current = base
        for part in parts:
            current = os.path.join(current, part)
            if os.path.islink(current):
                raise TrustedPathError(f"symbolic-link redirection is not permitted: {rel!r}")
        if must_exist and not os.path.isfile(candidate):
            raise TrustedPathError(f"trusted path does not resolve to a file: {rel!r}")
        return candidate

    def resolve_contract_artifact(self, rel):
        return self.resolve(rel, root=self.contracts_dir)

    def contract_for_target(self, target):
        if not isinstance(target, str):
            return None
        for clause, contract in self.contracts.items():
            if target in (clause, contract.get("contract_id")):
                return clause
        return None

    def mapping_by_id(self, evidence_id):
        for mapping in self.mappings.get("mappings", []):
            if mapping.get("evidence_id") == evidence_id:
                return mapping
        return None

    def decision_row(self, decision_id):
        headers, records, malformed, dupes = parse_decisions(self.decisions_text)
        matches = [r for r in records if r["_id"] == decision_id]
        if len(matches) == 1 and decision_id not in dupes:
            return matches[0]
        return None


_PRODUCTION_CONTEXT = None


def get_trusted_context():
    global _PRODUCTION_CONTEXT
    if _PRODUCTION_CONTEXT is None:
        _PRODUCTION_CONTEXT = TrustedContext()
    return _PRODUCTION_CONTEXT


def reset_trusted_context():
    global _PRODUCTION_CONTEXT
    _PRODUCTION_CONTEXT = None


class FixtureRequest(dict):
    """Test-harness request carrying a trusted fixture context.

    This is not a JSON request shape. The public entry point accepts plain
    dictionaries only; this subclass is created exclusively by the regression
    fixture builders and is never produced by production callers.
    """

    def __init__(self, data, context):
        super().__init__(data)
        self.fixture_context = context


def make_fixture_context(decisions_text=None, mappings=None,
                         owner_authorizations=None):
    base = get_trusted_context()
    context = copy.copy(base)
    context.fixture_mode = True
    context.problems = []
    context.decisions_text = decisions_text if decisions_text is not None else base.decisions_text
    context.mappings = copy.deepcopy(mappings) if mappings is not None else copy.deepcopy(base.mappings)
    context.owner_authorizations = copy.deepcopy(
        owner_authorizations if owner_authorizations is not None else [])
    context.artifacts = dict(base.artifacts)
    context.artifacts["mappings"] = context.mappings
    return context


REQUEST_ALLOWED_FIELDS = {
    "amendment_id", "target_contract", "candidate_document",
    "candidate_contract", "evidence_refs", "decision_ref", "notes",
}
REQUEST_PRIVILEGED_TERMS = (
    "baseline", "base_contract", "schema", "lexicon", "evidence", "decision",
    "owner", "template", "contracts_dir", "context", "policy", "manifest",
    "allowlist", "mode",
)
FORBIDDEN_CANDIDATE_CONTRACT_FIELDS = {
    "schema", "lexicon", "evidence_mappings", "decisions", "decision_register",
    "owner_authorizations", "manifest", "policy", "index", "context",
}


def validate_request_schema(request):
    problems = []
    if not isinstance(request, dict):
        return [problem("CONTRACT_REQUEST_SCHEMA_INVALID", "$.request",
                        "amendment request must be an object")]
    for key in request:
        if key in REQUEST_ALLOWED_FIELDS:
            continue
        low = key.lower()
        if any(term in low for term in REQUEST_PRIVILEGED_TERMS):
            problems.append(problem(
                "CONTRACT_TRUSTED_INPUT_OVERRIDE", f"$.request.{key}",
                "the amendment request may not supply or replace a trusted validation input"))
        else:
            problems.append(problem(
                "CONTRACT_REQUEST_SCHEMA_INVALID", f"$.request.{key}",
                f"unknown amendment request field {key!r}"))
    required = ("target_contract", "candidate_document", "decision_ref")
    for key in required:
        if key not in request:
            problems.append(problem(
                "CONTRACT_REQUEST_SCHEMA_INVALID", f"$.request.{key}",
                f"missing mandatory amendment request field {key!r}"))
    if "target_contract" in request and not isinstance(request["target_contract"], str):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.target_contract",
            "target_contract must be a contract ID or clause ID string"))
    if "candidate_document" in request and not isinstance(request["candidate_document"], str):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.candidate_document",
            "candidate_document must be text"))
    if "decision_ref" in request and not re.fullmatch(r"D-[0-9]{3}", str(request["decision_ref"])):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.decision_ref",
            "decision_ref must be a D-### identifier"))
    if "candidate_contract" in request and not isinstance(request["candidate_contract"], (dict, type(None))):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.candidate_contract",
            "candidate_contract must be an object or null"))
    if isinstance(request.get("candidate_contract"), dict):
        for key in request["candidate_contract"]:
            if key in FORBIDDEN_CANDIDATE_CONTRACT_FIELDS:
                problems.append(problem(
                    "CONTRACT_TRUSTED_INPUT_OVERRIDE",
                    f"$.request.candidate_contract.{key}",
                    "a candidate contract may not embed a trusted registry, decision register or authorization source"))
    if "evidence_refs" in request:
        refs = request["evidence_refs"]
        if not isinstance(refs, list) or any(not isinstance(x, str) or not x.startswith("EV-") for x in refs):
            problems.append(problem(
                "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.evidence_refs",
                "evidence_refs must be a list of EV- identifiers"))
    if "amendment_id" in request and not isinstance(request["amendment_id"], str):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.amendment_id",
            "amendment_id must be a string"))
    if "notes" in request and not isinstance(request["notes"], str):
        problems.append(problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.notes",
            "notes must be a string"))
    return problems


def template_projection_problems(contract, template_text):
    """Validate that a projection template contains no unaccounted literal text."""
    problems = []
    placeholders = re.findall(r"\{\{([^{}]+)\}\}", template_text or "")
    structural_allowed = {"clause_id", "title", "numerical_status_display"}
    fragment_ids = [f["proposition_id"] for f in contract.get("rendering", {}).get("fragments", [])]
    for ph in placeholders:
        if ph in structural_allowed or ph in fragment_ids:
            continue
        problems.append(problem(
            "CONTRACT_PROJECTION_MISMATCH", "$.rendering.template_path",
            f"projection template contains an unaccounted placeholder {{{{{ph}}}}}"))
    rendered = template_text or ""
    for key in structural_allowed:
        rendered = rendered.replace("{{" + key + "}}", str(contract.get(key, "")))
    fragments = {f["proposition_id"]: f for f in contract.get("rendering", {}).get("fragments", [])}
    for fid, frag in fragments.items():
        frag_text, frag_problems = render_fragment(contract, frag)
        problems.extend(frag_problems)
        rendered = rendered.replace("{{" + fid + "}}", frag_text)
    canonical, canonical_problems = render_contract(contract)
    problems.extend(canonical_problems)
    if norm_text(rendered) != norm_text(canonical):
        problems.append(problem(
            "CONTRACT_PROJECTION_MISMATCH", "$.rendering.template_path",
            "projection template contains literal text not derived from the typed contract"))
    return problems


# ---------------------------------------------------------------------------
# proposition compatibility and contract semantics
# ---------------------------------------------------------------------------
COMPAT = {
    "NUMERIC_DOMAIN": {
        "subjects": {"ALL_QUANTITIES", "ECONOMIC_ARITHMETIC", "DERIVED_CALCULATIONS", "CATEGORY_A_TEST_PROPOSITION"},
        "predicates": {"HAS_TYPE"}, "objects": {"NUMERIC_TYPE"},
    },
    "DIVISION_ROUNDING": {
        "subjects": {"EVERY_DIVISION"}, "predicates": {"STATES_ROUNDING"},
        "objects": {"ROUNDING_SET"},
    },
    "ARITHMETIC_REPRESENTATION": {
        "subjects": {"FORMULA_CALCULATIONS"}, "predicates": {"USES_REPRESENTATION"},
        "objects": {"REPRESENTATION_CLASS"},
    },
    "PERCENTAGE_REPRESENTATION": {
        "subjects": {"PERCENTAGE"}, "predicates": {"IS_REPRESENTED_AS"},
        "objects": {"PERCENTAGE_UNIT"},
    },
    "ARITHMETIC_AUTHORITY": {
        "subjects": {"ECONOMIC_ARITHMETIC"}, "predicates": {"USES_REPRESENTATION"},
        "objects": {"REPRESENTATION_CLASS"},
    },
    "CONSTANT_CLASSIFICATION": {
        "subjects": {"F_EC_000F_CONSTANTS", "V1_0_CALIBRATION", "CONSTANT_SET"},
        "predicates": {"IS_CLASSIFIED_AS", "HAS_EVIDENCE_STATE"},
        "objects": {"CONSTANT_STATUS", "CALIBRATION_CLASS", "CALIBRATION_EVIDENCE"},
    },
    "CONSTANT_CARRY_FORWARD": {
        "subjects": {"V1_0_CALIBRATION"}, "predicates": {"IS_CARRIED_UNCHANGED_INTO"},
        "objects": {"REGISTER_VERSION_CARRY"},
    },
    "CONSTANT_PROPERTY": {
        "subjects": {"F_EC_000F_CONSTANTS"},
        "predicates": {"ARE_OBSERVED_PRICES", "ARE_BALANCE_CLAIMS"},
        "objects": {"BOOLEAN_PROPERTY"},
    },
    "VALUE_CHANGE_AUTHORITY": {
        "subjects": {"VALUE_CHANGE"}, "predicates": {"REQUIRES_REVISION"},
        "objects": {"REVISION_REQUIREMENT", "REVISION_AUTHORITY"},
    },
    "FRACTIONAL_ACCUMULATION": {
        "subjects": {"CROSS_TURN_FRACTIONAL_REMAINDER", "WITHIN_TURN_CUMULATIVE_ACCRUAL"},
        "predicates": {"PERSISTS_ACROSS_TURNS", "PERSISTS_WITHIN_TURN"},
        "objects": {"UNRESOLVED", "ACCUMULATION_SCOPE"},
    },
}
OBJECT_DIMENSIONS = {
    "NUMERIC_TYPE": ("DIMENSIONLESS", {"NONE"}),
    "ROUNDING_SET": ("DIMENSIONLESS", {"NONE"}),
    "REPRESENTATION_CLASS": ("DIMENSIONLESS", {"NONE"}),
    "PERCENTAGE_UNIT": ("RATE", {"BASIS_POINT"}),
    "CONSTANT_STATUS": ("DIMENSIONLESS", {"NONE"}),
    "REGISTER_VERSION_CARRY": ("DIMENSIONLESS", {"NONE"}),
    "BOOLEAN_PROPERTY": ("DIMENSIONLESS", {"NONE"}),
    "UNRESOLVED": ("DIMENSIONLESS", {"NONE"}),
    "REVISION_REQUIREMENT": ("DIMENSIONLESS", {"NONE"}),
    "ACCUMULATION_SCOPE": ("DIMENSIONLESS", {"NONE"}),
    "SCOPE_QUALIFIER": ("DIMENSIONLESS", {"NONE"}),
    "CALIBRATION_CLASS": ("DIMENSIONLESS", {"NONE"}),
    "REVISION_AUTHORITY": ("DIMENSIONLESS", {"NONE"}),
    "CALIBRATION_EVIDENCE": ("DIMENSIONLESS", {"NONE"}),
}
MODALITY_POLARITY = {
    "MUST": {"AFFIRM"},
    "MUST_NOT": {"AFFIRM"},
    "MAY": {"AFFIRM"},
    "MAY_NOT": {"AFFIRM"},
    "NOT_ESTABLISHED": {"NEUTRAL"},
}


def parse_decisions(text):
    headers, records, malformed, counts = None, [], [], {}
    for line in (text or "").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if headers is None:
            low = [c.lower() for c in cells]
            if low and low[0] == "id" and "date" in low:
                headers = low
            continue
        m = re.match(r"^\|\s*(D-[0-9]{3})\s*\|", line)
        if not m:
            continue
        did = m.group(1)
        if len(cells) != len(headers):
            malformed.append((did, len(cells), len(headers)))
            continue
        rec = dict(zip(headers, cells))
        rec["_id"] = did
        records.append(rec)
        counts[did] = counts.get(did, 0) + 1
    dupes = sorted(d for d, c in counts.items() if c > 1)
    return headers, records, malformed, dupes


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, buf, i = [], [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            buf.append("|")
            i += 2
            continue
        if s[i] == "|":
            cells.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(s[i])
        i += 1
    cells.append("".join(buf).strip())
    return cells


def decision_cell(rec, prefix):
    for key, value in rec.items():
        if key.startswith(prefix):
            return value
    return ""


def decision_state(rec):
    status = decision_cell(rec, "status")
    m = re.search(r"category\s*([ABCD])", status, re.I)
    category = m.group(1).upper() if m else ""
    low = status.lower()
    return {
        "category": category,
        "status": status,
        "confirmed": "confirmed" in low,
        "provisional": "provisional" in low,
        "owner": any(w in low for w in ("owner-approved", "owner approved",
                                        "owner authorized", "owner accepted")),
        "inactive": any(w in low for w in ("pending", "proposed", "rejected",
                                           "deferred", "superseded", "not approved")),
    }


def render_fragment(contract, fragment):
    by_id = {p["id"]: p for p in contract["propositions"]}
    prop = by_id.get(fragment["proposition_id"])
    if not prop:
        return "", [problem("CONTRACT_SCHEMA_INVALID",
                            f"$.rendering.fragments.{fragment['proposition_id']}",
                            "rendering fragment targets a dangling proposition")]
    text = fragment["template"]
    problems = []
    for ph in re.findall(r"\{\{([^{}]+)\}\}", text):
        if ph == "basis_point_relation":
            value = prop.get("numeric", {}).get("basis_point_relation")
            if not value:
                problems.append(problem(
                    "CONTRACT_PROJECTION_MISMATCH",
                    f"$.propositions[{prop['id']}].numeric.basis_point_relation",
                    "rendering placeholder has no typed value"))
                continue
            text = text.replace("{{basis_point_relation}}", value)
        else:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", "$.rendering.fragments",
                f"unknown rendering placeholder {{{{{ph}}}}}"))
    return text, problems


def render_contract(contract):
    """Render the projection exclusively from typed contract fields.

    No caller-supplied template text participates. The projection template file
    is checked separately by template_projection_problems().
    """
    problems = []
    rendering = contract.get("rendering", {})
    prefix = rendering.get("structural_prefix", "")
    structural_allowed = {"clause_id", "title", "numerical_status_display"}
    for ph in re.findall(r"\{\{([^{}]+)\}\}", prefix):
        if ph not in structural_allowed:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", "$.rendering.structural_prefix",
                f"unknown structural placeholder {{{{{ph}}}}}"))
            continue
        prefix = prefix.replace("{{" + ph + "}}", str(contract.get(ph, "")))
    expected_prefix = (f"**{contract.get('clause_id')} — {contract.get('title')}.** "
                       f"*{contract.get('numerical_status_display')}.*")
    if norm_text(prefix) != norm_text(expected_prefix):
        problems.append(problem(
            "CONTRACT_PROJECTION_MISMATCH", "$.rendering.structural_prefix",
            "the structural prefix must contain only the clause identity, title and numerical status; extra material is not permitted"))
    fragments = rendering.get("fragments", [])
    fragment_ids = [f["proposition_id"] for f in fragments]
    clause_ids = [p["id"] for p in contract.get("propositions", [])
                  if p.get("projection_visibility") == "CLAUSE" and p.get("status") == "ACTIVE"]
    if len(fragment_ids) != len(set(fragment_ids)):
        problems.append(problem(
            "CONTRACT_PROJECTION_MISMATCH", "$.rendering.fragments",
            "duplicate rendering fragments are not permitted"))
    for fid in clause_ids:
        count = fragment_ids.count(fid)
        if count != 1:
            problems.append(problem(
                "CONTRACT_PROJECTION_MISMATCH", "$.rendering.fragments",
                f"clause proposition {fid} must appear exactly once in the projection; found {count}"))
    for fid in fragment_ids:
        if fid not in clause_ids:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", "$.rendering.fragments",
                f"fragment for {fid} is not an active CLAUSE proposition"))
    fragment_texts = []
    for fragment in fragments:
        text, frag_problems = render_fragment(contract, fragment)
        problems.extend(frag_problems)
        if len(split_sentences(norm_text(text))) > 1:
            problems.append(problem(
                "CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.rendering.fragments",
                f"fragment {fragment.get('proposition_id')} contains more than one material sentence"))
        fragment_texts.append(text)
    rendered = prefix
    if fragment_texts:
        rendered = rendered + " " + " ".join(fragment_texts)
    return rendered, problems


def canonical_projection_template(contract):
    rendering = contract.get("rendering", {})
    prefix = rendering.get("structural_prefix", "")
    fragment_ids = [f["proposition_id"] for f in rendering.get("fragments", [])]
    return prefix + ((" " + " ".join("{{" + fid + "}}" for fid in fragment_ids)) if fragment_ids else "")


def coverage_pieces(contract):
    problems = []
    pieces = []
    prefix = contract.get("rendering", {}).get("structural_prefix", "")
    for key in ("clause_id", "title", "numerical_status_display"):
        prefix = prefix.replace("{{" + key + "}}", str(contract.get(key, "")))
    pieces.extend(split_sentences(norm_text(prefix)))
    for frag in contract.get("rendering", {}).get("fragments", []):
        frag_text, frag_problems = render_fragment(contract, frag)
        problems.extend(frag_problems)
        pieces.extend(split_sentences(norm_text(frag_text)))
    return pieces, problems


def material_coverage(contract, clause_text):
    """Complete span accounting for the rendered projection.

    Every expected material piece must appear exactly once, in order, with no
    non-whitespace material before it, between pieces, or after the last piece.
    A fragment-presence check is not sufficient and is not used.
    """
    pieces, problems = coverage_pieces(contract)
    pieces = [p for p in pieces if p]
    rendered, render_problems = render_contract(contract)
    problems.extend(render_problems)
    expected = norm_text(rendered)
    actual = norm_text(clause_text)
    cursor = 0
    covered = 0
    missing = []
    gaps = []
    spans = []
    for piece in pieces:
        idx = actual.find(piece, cursor)
        if idx < 0:
            missing.append(piece)
            continue
        if idx > cursor:
            gap = actual[cursor:idx].strip()
            if gap:
                gaps.append(gap)
        spans.append({"piece": piece, "start": idx, "end": idx + len(piece)})
        covered += 1
        cursor = idx + len(piece)
    leftover = actual[cursor:].strip()
    if leftover:
        gaps.append(leftover)
    duplicates = sorted({p for p in pieces if actual.count(p) > 1})
    uncovered = gaps + missing + duplicates
    segments = len(pieces)
    ratio = 1.0 if actual == expected else (
        covered / float(segments + len(uncovered)) if (segments + len(uncovered)) else 0.0)
    return {
        "segments": segments,
        "covered": covered,
        "ratio": ratio,
        "exact": actual == expected,
        "missing": missing,
        "duplicates": duplicates,
        "gaps": gaps,
        "leftover": leftover,
        "uncovered_material": uncovered,
        "spans": spans,
        "problems": problems,
    }

def _object_equal(a, b):
    return json.dumps(a, sort_keys=True, ensure_ascii=False) == \
        json.dumps(b, sort_keys=True, ensure_ascii=False)


def _authority_arithmetic_rule(contract, prop):
    if contract.get("clause_id") != "F-EC-000b":
        return True
    if prop.get("kind") not in ("NUMERIC_DOMAIN", "DIVISION_ROUNDING",
                                "ARITHMETIC_REPRESENTATION", "PERCENTAGE_REPRESENTATION"):
        return True
    if prop.get("subject") == "CATEGORY_A_TEST_PROPOSITION":
        return True
    auth = prop.get("authority", {})
    return (auth.get("category") == "B" and auth.get("owner_reserved") is False
            and {"D-045", "D-064"}.issubset(set(auth.get("basis_decisions", []))))


def validate_contract_semantics(contract, schema, lexicon, decisions_text,
                                source_document_text, mode="production"):
    problems = []
    pid = contract.get("contract_id", "<contract>")
    if contract.get("schema_version") != "1.0.0":
        problems.append(problem("CONTRACT_SCHEMA_INVALID", "$.schema_version",
                                "contract schema_version must be 1.0.0"))
    props = contract.get("propositions", [])
    ids = [p.get("id") for p in props]
    if len(ids) != len(set(ids)):
        problems.append(problem("CONTRACT_SCHEMA_INVALID", "$.propositions",
                                "duplicate proposition identifiers"))
    for index, prop in enumerate(props):
        at = f"$.propositions[{index}]"
        pid_value = prop.get("id", "")
        if not str(pid_value).startswith(pid + "/P-"):
            problems.append(problem("CONTRACT_SCHEMA_INVALID", at + ".id",
                                    f"proposition ID {pid_value!r} is not namespaced to {pid}"))
        compat = COMPAT.get(prop.get("kind"))
        if not compat:
            problems.append(problem("CONTRACT_SCHEMA_INVALID", at + ".kind",
                                    f"unknown proposition kind {prop.get('kind')!r}"))
            continue
        if prop.get("subject") not in compat["subjects"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".subject",
                f"subject {prop.get('subject')!r} is not compatible with kind {prop.get('kind')!r}"))
        if prop.get("predicate") not in compat["predicates"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".predicate",
                f"predicate {prop.get('predicate')!r} is not compatible with kind {prop.get('kind')!r}"))
        obj = prop.get("object", {})
        obj_type = obj.get("type") if isinstance(obj, dict) else None
        if obj_type not in compat["objects"]:
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".object",
                f"object type {obj_type!r} is not compatible with kind {prop.get('kind')!r}"))
        if prop.get("subject") == "CROSS_TURN_FRACTIONAL_REMAINDER" and \
                prop.get("predicate") != "PERSISTS_ACROSS_TURNS":
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".predicate",
                "CROSS_TURN_FRACTIONAL_REMAINDER requires PERSISTS_ACROSS_TURNS"))
        if prop.get("subject") == "WITHIN_TURN_CUMULATIVE_ACCRUAL" and \
                prop.get("predicate") != "PERSISTS_WITHIN_TURN":
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".predicate",
                "WITHIN_TURN_CUMULATIVE_ACCRUAL requires PERSISTS_WITHIN_TURN"))
        pair = MODALITY_POLARITY.get(prop.get("modality"))
        if not pair or prop.get("polarity") not in pair:
            problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", at + ".polarity",
                f"modality {prop.get('modality')!r} cannot be combined with polarity {prop.get('polarity')!r}; negative meaning is carried only by MUST_NOT"))
        if prop.get("modality") == "MUST_NOT" and prop.get("polarity") == "NEGATE":
            problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", at + ".polarity",
                "double negation is not a representable proposition form"))
        units = prop.get("units", {})
        expected_dim = OBJECT_DIMENSIONS.get(obj_type)
        if expected_dim and (units.get("dimension"), set([units.get("unit")])) != \
                (expected_dim[0], expected_dim[1]):
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".units",
                f"unit {units.get('dimension')}/{units.get('unit')} is incompatible with object type {obj_type}"))
        timing = prop.get("timing", {})
        scope = prop.get("scope", {})
        if timing.get("persistence") != scope.get("persistence"):
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".timing.persistence",
                f"timing persistence {timing.get('persistence')!r} does not match scope persistence {scope.get('persistence')!r}"))
        if scope.get("inheritance") != "NONE":
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".scope.inheritance",
                "proposition scope must be explicit (inheritance NONE); ambiguous inheritance is rejected"))
        for sysname in scope.get("systems", []):
            if sysname not in contract.get("scope", {}).get("systems", []):
                problems.append(problem(
                    "CONTRACT_SCOPE_MISMATCH", at + ".scope.systems",
                    f"proposition system {sysname!r} is outside the contract scope"))
        if scope.get("domain") != contract.get("scope", {}).get("domain"):
            problems.append(problem(
                "CONTRACT_SCOPE_MISMATCH", at + ".scope.domain",
                f"proposition domain {scope.get('domain')!r} does not match contract domain"))
        concepts = [c["concept_id"] for c in lexicon.get("concepts", [])]
        for concept in scope.get("distinct_from", []):
            if concept not in concepts:
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", at + ".scope.distinct_from",
                    f"dangling concept reference {concept!r}"))
        numeric = prop.get("numeric", {})
        if prop.get("kind") == "DIVISION_ROUNDING":
            if numeric.get("rounding") != obj.get("allowed"):
                problems.append(problem(
                    "CONTRACT_PROPOSITION_CONFLICT", at + ".numeric.rounding",
                    "rounding list must equal the typed ROUNDING_SET allowed list"))
            if obj.get("floor_negative") != "TOWARD_NEGATIVE_INFINITY" or \
                    obj.get("floor_positive") != "TOWARD_ZERO":
                problems.append(problem(
                    "CONTRACT_PROPOSITION_CONFLICT", at + ".object",
                    "floor semantics changed: negative values must floor toward negative infinity and positive values toward zero"))
        if prop.get("kind") == "PERCENTAGE_REPRESENTATION":
            if numeric.get("precision") != "BASIS_POINT" or \
                    numeric.get("basis_point_relation") != "10,000 bp = 100%":
                problems.append(problem(
                    "CONTRACT_PROPOSITION_CONFLICT", at + ".numeric",
                    "basis-point percentages require the 10,000 bp = 100% relation"))
        if prop.get("kind") == "NUMERIC_DOMAIN" and obj.get("value") == "INTEGER":
            if numeric.get("representation") != "INTEGER" or numeric.get("precision") != "WHOLE_UNIT":
                problems.append(problem(
                    "CONTRACT_PROPOSITION_CONFLICT", at + ".numeric",
                    "integer numeric domain requires INTEGER representation and WHOLE_UNIT precision"))
        if prop.get("kind") == "ARITHMETIC_REPRESENTATION" and \
                obj.get("value") == "BINARY_FLOATING_POINT" and \
                numeric.get("representation") != "BINARY_FLOATING_POINT":
            problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", at + ".numeric.representation",
                "the prohibited representation must be named in numeric.representation"))
        if not _authority_arithmetic_rule(contract, prop):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", at + ".authority",
                "F-EC-000b arithmetic propositions must be Category B, not owner-reserved, and cite D-045 and D-064"))
        auth = prop.get("authority", {})
        if not auth.get("basis_decisions"):
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", at + ".authority.basis_decisions",
                                    "proposition authority must cite at least one existing decision"))
        headers, records, malformed, dupes = parse_decisions(decisions_text)
        by_decision = {r["_id"]: r for r in records}
        for did in auth.get("basis_decisions", []):
            if did in dupes or did not in by_decision:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", at + ".authority.basis_decisions",
                    f"authority decision {did} does not exist exactly once in DECISIONS.md"))
            else:
                state = decision_state(by_decision[did])
                if state["inactive"]:
                    problems.append(problem(
                        "CONTRACT_AUTHORITY_MISMATCH", at + ".authority.basis_decisions",
                        f"authority decision {did} is pending, rejected, deferred or superseded"))
        if auth.get("category") in ("A", "D") and not auth.get("owner_reserved"):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", at + ".authority.owner_reserved",
                "Category A/D proposition must be marked owner_reserved"))
        if auth.get("category") == "B" and auth.get("owner_reserved"):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", at + ".authority.owner_reserved",
                "Category B proposition cannot be owner-reserved"))
        anchor = prop.get("source_anchor", {})
        doc_path = anchor.get("document", "")
        if not os.path.isfile(os.path.join(REPO, doc_path)):
            problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", at + ".source_anchor.document",
                f"source document does not resolve: {doc_path}"))
        else:
            doc = read(os.path.join(REPO, doc_path))
            block = section_block(doc, anchor.get("section", ""))
            if not block or norm_text(anchor.get("excerpt", "")) not in norm_text(block):
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", at + ".source_anchor",
                    f"anchor excerpt does not appear in {doc_path} section {anchor.get('section')!r}"))
        if anchor.get("source_kind") == "CLAUSE" and doc_path != contract.get("source_document"):
            problems.append(problem(
                "CONTRACT_SCOPE_MISMATCH", at + ".source_anchor.document",
                "CLAUSE anchor must use the contract source document"))
        if prop.get("projection_visibility") == "CLAUSE":
            if anchor.get("source_kind") != "CLAUSE":
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", at + ".source_anchor.source_kind",
                    "CLAUSE-visible proposition requires a CLAUSE anchor"))
        elif prop.get("projection_visibility") == "DERIVED_FROM_BASELINE_EVIDENCE":
            if anchor.get("source_kind") != "BASELINE_EVIDENCE":
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", at + ".source_anchor.source_kind",
                    "derived proposition requires a BASELINE_EVIDENCE anchor"))
        for ex_index, exception in enumerate(prop.get("exceptions", [])):
            ex_at = f"{at}.exceptions[{ex_index}]"
            target = exception.get("target_proposition")
            if target not in ids:
                problems.append(problem(
                    "CONTRACT_EXCEPTION_UNSUPPORTED", ex_at + ".target_proposition",
                    f"exception targets a dangling proposition {target!r}"))
                continue
            target_prop = next(p for p in props if p["id"] == target)
            policy = contract.get("change_policy", {}).get("propositions", {}).get(target, {})
            if not policy.get("exceptions_allowed"):
                problems.append(problem(
                    "CONTRACT_EXCEPTION_UNSUPPORTED", ex_at,
                    f"no exception is authorized for proposition {target}"))
            target_systems = set(target_prop.get("scope", {}).get("systems", []))
            ex_systems = set(exception.get("scope", {}).get("systems", []))
            if not ex_systems.issubset(target_systems):
                problems.append(problem(
                    "CONTRACT_SCOPE_MISMATCH", ex_at + ".scope.systems",
                    f"exception scope {sorted(ex_systems)} is wider than the target scope {sorted(target_systems)}"))
            ex_authority = exception.get("authority", {})
            did = ex_authority.get("decision")
            if did not in by_decision:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", ex_at + ".authority.decision",
                    f"exception authority decision {did!r} does not exist"))
    # change policy coverage
    policy = contract.get("change_policy", {}).get("propositions", {})
    if set(policy) != set(ids):
        problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", "$.change_policy.propositions",
            "change policy must cover exactly the proposition set"))
    for pid_value, entry in policy.items():
        prop = next((p for p in props if p["id"] == pid_value), None)
        if not prop:
            continue
        if entry.get("category") != prop.get("authority", {}).get("category"):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.change_policy.propositions.{pid_value}.category",
                "change-policy category does not match the proposition authority category"))
        if entry.get("owner_reserved") != prop.get("authority", {}).get("owner_reserved"):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.change_policy.propositions.{pid_value}.owner_reserved",
                "change-policy owner_reserved does not match the proposition authority"))
        if entry.get("baseline_unresolved") and prop.get("modality") != "NOT_ESTABLISHED":
            problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", f"$.change_policy.propositions.{pid_value}.baseline_unresolved",
                "baseline_unresolved is set but the proposition is not NOT_ESTABLISHED"))
    # rendering and projection
    rendered, render_problems = render_contract(contract)
    problems.extend(render_problems)
    if source_document_text is not None:
        clause = extract_clause(source_document_text, contract.get("clause_id", ""))
        if not clause:
            problems.append(problem(
                "CONTRACT_PROJECTION_MISMATCH", "$.source_document",
                f"source clause {contract.get('clause_id')} is missing"))
        else:
            if norm_text(rendered) != norm_text(clause):
                problems.append(problem(
                    "CONTRACT_PROJECTION_MISMATCH", "$.rendering",
                    "rendered projection does not equal the source clause after normalization"))
            coverage = material_coverage(contract, clause)
            problems.extend(coverage["problems"])
            if not coverage["exact"] or coverage["uncovered_material"]:
                problems.append(problem(
                    "CONTRACT_COVERAGE_GAP", "$.rendering",
                    f"material coverage is {coverage['covered']}/{coverage['segments']}; "
                    f"uncovered={coverage['uncovered_material']}"))
    return problems


def validate_registry(artifacts, decisions_text, mode="production"):
    problems = []
    schema = artifacts.get("schema", {})
    index = artifacts.get("index", {})
    lexicon = artifacts.get("lexicon", {})
    mappings = artifacts.get("mappings", {})
    problems.extend(schema_meta_problems(schema))
    problems.extend(validate_schema(index, {"$ref": "#/$defs/index"}, schema, "$.index"))
    problems.extend(validate_schema(lexicon, {"$ref": "#/$defs/lexicon"}, schema, "$.lexicon"))
    problems.extend(validate_schema(mappings, {"$ref": "#/$defs/evidence_mappings"}, schema, "$.evidence_mappings"))
    problems.extend(validate_schema(index.get("cross_cutting_authority"),
                                    {"$ref": "#/$defs/proposition"}, schema, "$.cross_cutting_authority"))
    for clause, contract in artifacts.get("contracts", {}).items():
        problems.extend(validate_schema(contract, {"$ref": "#/$defs/contract"}, schema,
                                        f"$.contracts.{clause}"))
    # registry cross-references
    refs = {r.get("contract_id"): r for r in index.get("contracts", [])}
    for clause, contract in artifacts.get("contracts", {}).items():
        ref = refs.get(contract.get("contract_id"))
        if not ref:
            problems.append(problem("CONTRACT_SCHEMA_INVALID", "$.index.contracts",
                                    f"contract {contract.get('contract_id')} is not indexed"))
            continue
        for field in ("contract_version", "numerical_status", "lifecycle_status"):
            if ref.get(field) != contract.get(field):
                problems.append(problem(
                    "CONTRACT_SCHEMA_INVALID", f"$.index.contracts.{contract.get('contract_id')}.{field}",
                    f"index {field} does not match the contract"))
        if ref.get("contract_sha256") != contract_sha256(contract):
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.contracts.{contract.get('contract_id')}.contract_sha256",
                "recorded contract fingerprint does not match the canonical contract bytes"))
        rendered, _ = render_contract(contract)
        if ref.get("projection_sha256") != projection_sha256(rendered):
            problems.append(problem(
                "CONTRACT_PROJECTION_MISMATCH", f"$.index.contracts.{contract.get('contract_id')}.projection_sha256",
                "recorded projection fingerprint does not match the rendered projection"))
        if ref.get("source_sha256") != contract.get("baseline_source_hash"):
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.contracts.{contract.get('contract_id')}.source_sha256",
                "recorded source hash does not match the contract baseline hash"))
        if contract.get("baseline_source_hash") != BASELINE_HASHES.get(clause):
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.contracts.{clause}.baseline_source_hash",
                "baseline hash is not the preserved B-04 hash"))
    # index file hashes
    for name, rel in (("schema", "schema.json"), ("lexicon", "lexicon.json"),
                      ("evidence_mappings", "evidence_mappings.json")):
        recorded = index.get(name, {}).get("sha256")
        actual = sha256_file(os.path.join(artifacts["dir"], rel))
        if recorded != actual:
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.{name}.sha256",
                f"recorded {name} fingerprint does not match the file bytes"))
    # source documents
    for entry in index.get("source_documents", []):
        path = os.path.join(REPO, entry.get("path", ""))
        if not os.path.isfile(path):
            problems.append(problem("CONTRACT_SCHEMA_INVALID", "$.index.source_documents",
                                    f"source document does not resolve: {entry.get('path')}"))
        elif entry.get("sha256") != sha256_file(path):
            problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.source_documents.{entry.get('path')}",
                "recorded source-document hash does not match the file bytes"))
    # owner authorizations in production
    for entry in index.get("owner_authorizations", []):
        if mode == "production" and entry.get("fixture_only"):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", "$.index.owner_authorizations",
                f"owner authorization {entry.get('authorization_id')} is a test fixture and cannot authorize a production amendment"))
    return problems


# ---------------------------------------------------------------------------
# lexicon, modality and ingestion
# ---------------------------------------------------------------------------
def concept_list(lexicon):
    return lexicon.get("concepts", [])


def _surface_pattern(surface):
    return re.compile(r"(?<![a-z0-9])" + re.escape(surface) + r"(?![a-z0-9])", re.I)


def concept_matches(text, lexicon):
    """Return non-overlapping longest surface-form matches."""
    low = " " + (text or "").lower() + " "
    candidates = []
    for concept in concept_list(lexicon):
        for surface in concept.get("surface_forms", []):
            for m in _surface_pattern(surface).finditer(low):
                candidates.append((m.start(), m.end(), -len(surface), concept))
    candidates.sort()
    taken, out = [], []
    for start, end, _, concept in candidates:
        if any(not (end <= s or start >= e) for s, e in taken):
            continue
        taken.append((start, end))
        out.append(concept)
    return out


def unknown_family_terms(text, lexicon):
    low = " " + (text or "").lower() + " "
    hits = []
    for family, roots in lexicon.get("unknown_material_families", {}).items():
        for root in roots:
            if re.search(r"(?<![a-z0-9])" + re.escape(root), low):
                hits.append((family, root))
    return hits


def normalize_modality(text):
    """Deterministic modality normalization with explicit double-negation rules."""
    low = " " + (text or "").lower() + " "
    if re.search(r"not\s+not\s+(?:permitted|allowed)", low):
        return "PERMIT"
    if re.search(r"not\s+(?:prohibited|forbidden|banned)", low):
        return "PERMIT"
    if re.search(r"not\s+(?:permitted|allowed)", low):
        return "PROHIBIT"
    if re.search(r"(?:may|can|must)\s+not|cannot|can\s+not", low):
        return "PROHIBIT"
    if re.search(r"\b(?:no|never|without)\b", low):
        return "PROHIBIT"
    if re.search(r"\bprohibition\b", low):
        return "PROHIBIT"
    has_perm = bool(re.search(r"\b(?:may|can|permitted|allowed|preserved|retained|carried|carries|carry|remains|remain)\b", low))
    has_proh = bool(re.search(r"\b(?:prohibited|forbidden|banned)\b", low))
    if has_perm and has_proh:
        return None
    if has_perm:
        return "PERMIT"
    if re.search(r"\b(?:must|shall|required|states)\b", low):
        return "MANDATE"
    return None


def equivalent_modality(base, candidate):
    if base == "MUST":
        return candidate in ("MANDATE", "MUST")
    if base == "MUST_NOT":
        return candidate in ("PROHIBIT", "MUST_NOT")
    if base == "MAY":
        return candidate in ("PERMIT", "MAY")
    if base == "NOT_ESTABLISHED":
        return candidate in ("UNRESOLVED", "NOT_ESTABLISHED")
    return False


def _has_qualifier(text, lexicon, kind):
    low = (text or "").lower()
    return any(q in low for q in lexicon.get("persistence_qualifiers", {}).get(kind, []))


def _basis_relation(text):
    m = re.search(r"(\d[\d,]*)\s*bp\s*=\s*100%", text or "", re.I)
    if not m:
        return None
    return m.group(1).replace(",", "")


def _descriptor(kind, predicate, obj, modality):
    return {"kind": kind, "predicate": predicate, "object": obj,
            "modality": modality}


def _assertive_modality(modality):
    return "PROHIBIT" if modality == "PROHIBIT" else "MANDATE"


def _candidates_for_concepts(concepts, modality, sentence, lexicon):
    """Return one typed descriptor per independently recognised proposition."""
    ids = [c["concept_id"] for c in concepts]
    out = []
    if "SCOPE_TREASURY_SUBSYSTEM" in ids and modality == "PERMIT" and any(
            i in ids for i in ("BINARY_FLOATING_POINT", "CROSS_TURN_REMAINDER_PERSISTENCE",
                               "DECIMAL_FRACTION")):
        return {"status": "EXCEPTION",
                "message": "a subsystem permission on controlled arithmetic is an unsupported exception"}
    representations = [i for i in ids if i in ("BINARY_FLOATING_POINT", "INTEGER_REPRESENTATION", "DECIMAL_FRACTION")]
    if len(set(representations)) > 1:
        return {"status": "AMBIGUOUS", "message": "sentence names more than one representation class"}
    if "BINARY_FLOATING_POINT" in ids:
        out.append(_descriptor("ARITHMETIC_REPRESENTATION", "USES_REPRESENTATION",
                               {"type": "REPRESENTATION_CLASS", "value": "BINARY_FLOATING_POINT"},
                               modality or "MANDATE"))
    if "DECIMAL_FRACTION" in ids:
        out.append(_descriptor("NUMERIC_DOMAIN", "HAS_TYPE",
                               {"type": "NUMERIC_TYPE", "value": "DECIMAL_FRACTION"},
                               modality or "MANDATE"))
    if "INTEGER_REPRESENTATION" in ids:
        out.append(_descriptor("NUMERIC_DOMAIN", "HAS_TYPE",
                               {"type": "NUMERIC_TYPE", "value": "INTEGER"},
                               modality or "MANDATE"))
    if "CROSS_TURN_REMAINDER_PERSISTENCE" in ids and "CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN" in ids:
        return {"status": "AMBIGUOUS", "message": "sentence mixes within-turn and across-turn accumulation concepts"}
    if "CROSS_TURN_REMAINDER_PERSISTENCE" in ids:
        if not _has_qualifier(sentence, lexicon, "ACROSS_TURNS"):
            return {"status": "AMBIGUOUS", "message": "fractional-accumulation concept lacks an across-turn qualifier"}
        out.append(_descriptor("FRACTIONAL_ACCUMULATION", "PERSISTS_ACROSS_TURNS",
                               {"type": "ACCUMULATION_SCOPE", "value": "ACROSS_TURNS"},
                               modality or "MANDATE"))
    if "CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN" in ids:
        if not _has_qualifier(sentence, lexicon, "WITHIN_TURN"):
            return {"status": "AMBIGUOUS", "message": "cumulative-accrual concept lacks a within-turn qualifier"}
        out.append(_descriptor("FRACTIONAL_ACCUMULATION", "PERSISTS_WITHIN_TURN",
                               {"type": "ACCUMULATION_SCOPE", "value": "WITHIN_TURN"},
                               modality or "MANDATE"))
    if "BASIS_POINT" in ids:
        relation = _basis_relation(sentence)
        if relation is not None and relation != "10000":
            return {"status": "CONFLICT", "message": "the basis-point relation differs from 10,000 bp = 100%"}
        descriptor = _descriptor("PERCENTAGE_REPRESENTATION", "IS_REPRESENTED_AS",
                                 {"type": "PERCENTAGE_UNIT", "unit": "BASIS_POINT", "basis": 10000},
                                 modality or "MANDATE")
        descriptor["_force_changed"] = relation is None
        out.append(descriptor)
    rounding = [i for i in ids if i in ("ROUND_FLOOR", "ROUND_CEIL", "ROUND_HALF_UP")]
    if rounding:
        allowed = []
        if "ROUND_FLOOR" in rounding:
            allowed.append("FLOOR")
        if "ROUND_CEIL" in rounding:
            allowed.append("CEIL")
        if "ROUND_HALF_UP" in rounding:
            allowed.append("ROUND_HALF_UP")
        out.append(_descriptor("DIVISION_ROUNDING", "STATES_ROUNDING",
                               {"type": "ROUNDING_SET", "allowed": allowed,
                                "floor_negative": "TOWARD_NEGATIVE_INFINITY",
                                "floor_positive": "TOWARD_ZERO"},
                               "MANDATE"))
    if "FINAL_CALIBRATION" in ids and "PROVISIONAL_CALIBRATION" in ids:
        return {"status": "AMBIGUOUS", "message": "sentence names both provisional and final calibration"}
    if "FINAL_CALIBRATION" in ids:
        out.append(_descriptor("CONSTANT_CLASSIFICATION", "IS_CLASSIFIED_AS",
                               {"type": "CALIBRATION_CLASS", "value": "FINAL"},
                               _assertive_modality(modality)))
    if "PROVISIONAL_CALIBRATION" in ids:
        out.append(_descriptor("CONSTANT_CLASSIFICATION", "IS_CLASSIFIED_AS",
                               {"type": "CONSTANT_STATUS", "value": "V1_0_PROVISIONAL_CALIBRATION"},
                               _assertive_modality(modality)))
    if "VERSION_CARRY_FORWARD" in ids:
        out.append(_descriptor("CONSTANT_CARRY_FORWARD", "IS_CARRIED_UNCHANGED_INTO",
                               {"type": "REGISTER_VERSION_CARRY", "from": "v1.0",
                                "to": "v1.1", "reference": "F-EC-044"},
                               "MANDATE"))
    if "OBSERVED_PRICES_CONSTANT" in ids:
        out.append(_descriptor("CONSTANT_PROPERTY", "ARE_OBSERVED_PRICES",
                               {"type": "BOOLEAN_PROPERTY", "value": "OBSERVED_PRICES"},
                               _assertive_modality(modality)))
    if "BALANCE_CLAIMS_CONSTANT" in ids:
        out.append(_descriptor("CONSTANT_PROPERTY", "ARE_BALANCE_CLAIMS",
                               {"type": "BOOLEAN_PROPERTY", "value": "BALANCE_CLAIMS"},
                               _assertive_modality(modality)))
    if "OWNER_ONLY_REVISION_AUTHORITY" in ids:
        out.append(_descriptor("VALUE_CHANGE_AUTHORITY", "REQUIRES_REVISION",
                               {"type": "REVISION_AUTHORITY", "value": "OWNER_ONLY"},
                               "MANDATE"))
    if "REVISION_REQUIREMENT" in ids:
        out.append(_descriptor("VALUE_CHANGE_AUTHORITY", "REQUIRES_REVISION",
                               {"type": "REVISION_REQUIREMENT", "mechanism": "NEW_REGISTER_REVISION",
                                "authority": "D-014"},
                               "MANDATE"))
    if not out:
        return {"status": "UNMAPPED", "message": "material concept has no typed mapping"}
    return {"status": "TYPED", "candidates": out}


def analyze_sentence(sentence, contract, lexicon):
    low = (sentence or "").lower()
    for marker_text in lexicon.get("exception_markers", []):
        escaped = re.escape(marker_text.strip())
        if re.search(r"(?<![a-z0-9])" + escaped + r"(?![a-z0-9])", low):
            return {"status": "EXCEPTION", "message": "exception or conditional construction on a controlled clause"}
    concepts = concept_matches(sentence, lexicon)
    if not concepts:
        families = unknown_family_terms(sentence, lexicon)
        if families:
            return {"status": "UNMAPPED",
                    "message": f"unknown material term(s) {sorted(set(r for _, r in families))}"}
        return {"status": "UNPARSED", "message": "material sentence was not consumed by the controlled grammar"}
    modality = normalize_modality(sentence)
    built = _candidates_for_concepts(concepts, modality, sentence, lexicon)
    if built["status"] != "TYPED":
        return built
    equivalents, changed, added, conflicts = [], [], [], []
    for candidate in built["candidates"]:
        props = [p for p in contract.get("propositions", [])
                 if p.get("kind") == candidate["kind"] and p.get("predicate") == candidate["predicate"]]
        if not props:
            added.append(candidate)
            continue
        baseline = props[0]
        object_equal = _object_equal(baseline.get("object"), candidate["object"])
        if candidate["kind"] == "DIVISION_ROUNDING":
            object_equal = set(baseline["object"].get("allowed", [])) == set(candidate["object"].get("allowed", []))
        base_mod = baseline.get("modality")
        cand_mod = candidate["modality"]
        if candidate.get("_force_changed"):
            changed.append({"proposition_id": baseline["id"],
                            "reason": "the sentence omits material detail from proposition " + baseline["id"],
                            "candidate": candidate})
            continue
        if object_equal and equivalent_modality(base_mod, cand_mod):
            equivalents.append(baseline["id"])
            continue
        if base_mod in ("MUST", "MUST_NOT") and cand_mod in ("PERMIT", "MAY", "MANDATE"):
            conflicts.append(f"an affirmative or permission statement contradicts the baseline {base_mod} proposition {baseline['id']}")
            continue
        if base_mod == "MUST" and cand_mod == "PROHIBIT":
            conflicts.append(f"a prohibition contradicts the baseline MUST proposition {baseline['id']}")
            continue
        if base_mod == "NOT_ESTABLISHED" and cand_mod in ("PERMIT", "MANDATE", "MAY"):
            changed.append({"proposition_id": baseline["id"],
                            "reason": f"unresolved proposition {baseline['id']} is being turned into an affirmative rule",
                            "candidate": candidate})
            continue
        if not object_equal:
            conflicts.append(f"an object change contradicts the baseline proposition {baseline['id']}")
            continue
        changed.append({"proposition_id": baseline["id"],
                        "reason": f"a modality change affects proposition {baseline['id']}",
                        "candidate": candidate})
    if conflicts:
        return {"status": "CONFLICT", "message": "; ".join(conflicts)}
    if changed:
        return {"status": "CHANGED", "propositions": changed}
    if added:
        return {"status": "ADDED", "candidates": added}
    return {"status": "EQUIVALENT", "proposition_ids": equivalents}
def baseline_sentences(contract):
    rendered, _ = render_contract(contract)
    sentences = split_sentences(norm_text(rendered))
    fragments = contract.get("rendering", {}).get("fragments", [])
    out = []
    for sentence in sentences:
        pids = []
        for frag in fragments:
            frag_text, _ = render_fragment(contract, frag)
            if frag_text and norm_text(frag_text) in sentence:
                pids.append(frag["proposition_id"])
        out.append((sentence, pids))
    return out


def ingest_clause(contract, clause_text, lexicon):
    rendered, render_problems = render_contract(contract)
    base_norm = norm_text(rendered)
    cand_norm = norm_text(clause_text)
    coverage = material_coverage(contract, clause_text)
    if cand_norm == base_norm:
        return {"status": "BASELINE", "problems": render_problems, "coverage": coverage,
                "changed": [], "added": [], "removed": []}
    expected = baseline_sentences(contract)
    candidate_sentences = split_sentences(cand_norm)
    matched = set()
    changed, added, removed = [], [], []
    problems = list(render_problems)
    for sentence in candidate_sentences:
        exact = next((e for e in expected if norm_text(sentence) == e[0]), None)
        if exact:
            matched.update(exact[1])
            continue
        result = analyze_sentence(sentence, contract, lexicon)
        if result["status"] == "EQUIVALENT":
            matched.update(result["proposition_ids"])
        elif result["status"] == "CONFLICT":
            problems.append(problem("CONTRACT_PROPOSITION_CONFLICT", "$.ingestion",
                                    result["message"] + f" :: {sentence!r}"))
        elif result["status"] == "EXCEPTION":
            problems.append(problem("CONTRACT_EXCEPTION_UNSUPPORTED", "$.ingestion",
                                    result["message"] + f" :: {sentence!r}"))
        elif result["status"] == "UNMAPPED":
            problems.append(problem("CONTRACT_UNMAPPED_TERM", "$.ingestion",
                                    result["message"] + f" :: {sentence!r}"))
        elif result["status"] == "UNPARSED":
            problems.append(problem("CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.ingestion",
                                    result["message"] + f" :: {sentence!r}"))
        elif result["status"] == "AMBIGUOUS":
            problems.append(problem("CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.ingestion",
                                    result["message"] + f" :: {sentence!r}"))
        elif result["status"] == "CHANGED":
            changed.extend(result["propositions"])
        elif result["status"] == "ADDED":
            for candidate in result["candidates"]:
                added.append({"candidate": candidate, "sentence": sentence})
    for sentence, pids in expected:
        for pid in pids:
            if pid not in matched:
                removed.append({"proposition_id": pid, "sentence": sentence})
    if coverage["duplicates"]:
        problems.append(problem("CONTRACT_PROPOSITION_CONFLICT", "$.ingestion",
                                "duplicate material sentence(s) are not permitted: " +
                                "; ".join(coverage["duplicates"])))
    if removed:
        problems.append(problem("CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.ingestion",
                                "baseline material is missing: " +
                                ", ".join(sorted({r['proposition_id'] for r in removed}))))
    if problems:
        status = "REJECTED"
    elif changed or added:
        status = "CHANGED"
    else:
        status = "WORDING_ONLY"
    return {"status": status, "problems": problems, "coverage": coverage,
            "changed": changed, "added": added, "removed": removed}


# ---------------------------------------------------------------------------
# diffs
# ---------------------------------------------------------------------------
def _field_changes(a, b, prefix=""):
    out = []
    if type(a) is not type(b):
        return [prefix or "$"]
    if isinstance(a, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a or key not in b:
                out.append(f"{prefix}.{key}")
            else:
                out.extend(_field_changes(a[key], b[key], f"{prefix}.{key}"))
    elif isinstance(a, list):
        if a != b:
            out.append(prefix or "$")
    elif a != b:
        out.append(prefix or "$")
    return out


def diff_contracts(base, candidate):
    base_by = {p["id"]: p for p in base.get("propositions", [])}
    cand_by = {p["id"]: p for p in candidate.get("propositions", [])}
    added = sorted(set(cand_by) - set(base_by))
    removed = sorted(set(base_by) - set(cand_by))
    changed, unchanged = [], []
    for pid in sorted(set(base_by) & set(cand_by)):
        fields = _field_changes(base_by[pid], cand_by[pid], f"$.propositions.{pid}")
        if fields:
            changed.append({"proposition_id": pid, "fields": fields})
        else:
            unchanged.append(pid)
    material_fields = {"schema_version", "contract_id", "clause_id", "source_document",
                       "baseline_source_hash", "scope", "numerical_status"}
    wording_fields = {"title", "source_version", "numerical_status_display", "rendering"}
    metadata_fields = ("contract_version", "effective_decision", "lifecycle_status")
    metadata_changes = []
    for field in metadata_fields:
        previous = base.get(field)
        proposed = candidate.get(field)
        metadata_changes.append({
            "field": field,
            "previous": previous,
            "proposed": proposed,
            "changed": previous != proposed,
            "classification": "UNCHANGED" if previous == proposed else "PENDING",
        })
    contract_changes = []
    for key in sorted(set(base) | set(candidate)):
        if key == "propositions" or key in metadata_fields:
            continue
        if base.get(key) == candidate.get(key):
            continue
        if key == "change_policy":
            base_pol = base.get("change_policy", {}).get("propositions", {})
            cand_pol = candidate.get("change_policy", {}).get("propositions", {})
            common = set(base_pol) & set(cand_pol)
            changed_common = sorted(pid for pid in common if base_pol[pid] != cand_pol[pid])
            if changed_common:
                contract_changes.append({"field": "change_policy", "category": "material",
                                         "details": changed_common})
            continue
        category = "material" if key in material_fields else (
            "wording" if key in wording_fields else "material")
        contract_changes.append({"field": key, "category": category})
    result = {
        "added": added, "removed": removed, "changed": changed,
        "unchanged": unchanged,
        "rendering_changed": base.get("rendering") != candidate.get("rendering"),
        "scope_changed": any(any(".scope" in f for f in c["fields"]) for c in changed),
        "exception_changed": any(any(".exceptions" in f for f in c["fields"]) for c in changed),
        "units_changed": any(any(".units" in f for f in c["fields"]) for c in changed),
        "timing_changed": any(any(".timing" in f for f in c["fields"]) for c in changed),
        "authority_changed": any(any(".authority" in f for f in c["fields"]) for c in changed),
        "contract_changes": contract_changes,
        "metadata_changes": metadata_changes,
        "material_contract_changes": [c for c in contract_changes if c["category"] == "material"],
        "wording_contract_changes": [c for c in contract_changes if c["category"] == "wording"],
    }
    result["changed_ids"] = [c["proposition_id"] for c in changed]
    result["all_changed"] = sorted(set(added) | set(removed) | set(result["changed_ids"]))
    return result


# ---------------------------------------------------------------------------
# evidence gate
# ---------------------------------------------------------------------------
PLACEHOLDER_REVIEWERS = {
    "", "tbd", "todo", "n/a", "none", "ai", "assistant", "prompt 14a",
    "implementation actor", "author", "reviewer", "owner",
}
FOREIGN_DOMAIN_TERMS = (
    "fair-play", "fair play", "appeal", "retention", "sanction", "privacy",
    "moderation", "account", "display-name", "reroll",
)


def _review_is_valid(mapping, mode):
    review = mapping.get("review", {})
    if review.get("review_status") != "REVIEWED":
        return False, "mapping is not REVIEWED"
    identity = (review.get("reviewed_by") or "").strip()
    role = (review.get("reviewer_role") or "").strip()
    date = (review.get("reviewed_at") or "").strip()
    rationale = (review.get("review_rationale") or "").strip()
    if identity.lower() in PLACEHOLDER_REVIEWERS:
        return False, "reviewer identity is missing or a placeholder"
    if not role or not substantive(rationale, 20):
        return False, "reviewer role or rationale is missing"
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        return False, "review date is not ISO-8601"
    if identity.lower() == (mapping.get("implementation_actor") or "").lower():
        return False, "reviewer is the implementation actor"
    if mode == "production" and any(t in identity.upper() or t in role.upper()
                                    for t in ("SYNTHETIC", "FIXTURE", "TEST")):
        return False, "synthetic or fixture review cannot satisfy a production evidence gate"
    if any(t in identity.upper() for t in ("TEMP-OWNER", "PLACEHOLDER")):
        return False, "placeholder reviewer identity"
    return True, ""


def _contracts_by_id(contracts):
    out = {}
    for key, contract in (contracts or {}).items():
        if isinstance(contract, dict) and contract.get("contract_id"):
            out[contract["contract_id"]] = contract
        elif isinstance(contract, dict):
            out[key] = contract
    return out


def evidence_integrity(mappings_doc, contracts, mode="production", repo_root=REPO):
    contracts = _contracts_by_id(contracts)
    problems = []
    stats = {"mappings": 0, "reviewed": 0, "not_reviewed": 0, "supports": 0}
    seen = set()
    for mapping in mappings_doc.get("mappings", []):
        stats["mappings"] += 1
        at = f"$.mappings[{mapping.get('evidence_id')}]"
        if mapping.get("evidence_id") in seen:
            problems.append(problem("CONTRACT_SCHEMA_INVALID", at,
                                    "duplicate evidence_id"))
        seen.add(mapping.get("evidence_id"))
        contract = contracts.get(mapping.get("contract_id"))
        if not contract:
            problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at,
                                    f"dangling contract reference {mapping.get('contract_id')!r}"))
            continue
        prop = next((p for p in contract.get("propositions", [])
                     if p["id"] == mapping.get("proposition_id")), None)
        if not prop:
            problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at,
                                    f"dangling proposition reference {mapping.get('proposition_id')!r}"))
            continue
        path = os.path.join(repo_root, mapping.get("document_path", ""))
        if not os.path.isfile(path):
            problems.append(problem("CONTRACT_EVIDENCE_INTEGRITY_FAILED", at + ".document_path",
                                    "evidence document does not resolve"))
            continue
        if mapping.get("document_sha256") != sha256_file(path):
            problems.append(problem("CONTRACT_EVIDENCE_INTEGRITY_FAILED", at + ".document_sha256",
                                    "stale evidence hash: the document bytes do not match the reviewed hash"))
        block = section_block(read(path), mapping.get("section", ""))
        if not block or norm_text(mapping.get("excerpt", "")) not in norm_text(block):
            problems.append(problem("CONTRACT_EVIDENCE_INTEGRITY_FAILED", at + ".excerpt",
                                    "the cited excerpt does not appear in the cited section"))
        review = mapping.get("review", {})
        if review.get("review_status") == "REVIEWED":
            ok, why = _review_is_valid(mapping, mode)
            if not ok:
                problems.append(problem("CONTRACT_EVIDENCE_NOT_REVIEWED", at + ".review", why))
                stats["not_reviewed"] += 1
            else:
                stats["reviewed"] += 1
                if mapping.get("classification") == "SUPPORTS":
                    stats["supports"] += 1
        else:
            stats["not_reviewed"] += 1
            if mapping.get("classification") != "NOT_REVIEWED":
                problems.append(problem(
                    "CONTRACT_EVIDENCE_NOT_REVIEWED", at + ".classification",
                    "an unreviewed mapping must carry classification NOT_REVIEWED"))
        prop_systems = set(prop.get("scope", {}).get("systems", []))
        map_systems = set(mapping.get("scope", {}).get("systems", []))
        if not prop_systems.issubset(map_systems):
            problems.append(problem(
                "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at + ".scope.systems",
                f"evidence scope {sorted(map_systems)} does not cover proposition scope {sorted(prop_systems)}"))
    # baseline coverage: every proposition that will require evidence on change
    covered = {m.get("proposition_id") for m in mappings_doc.get("mappings", [])
               if m.get("status") == "ACTIVE"}
    for contract in contracts.values():
        for prop in contract.get("propositions", []):
            policy = contract.get("change_policy", {}).get("propositions", {}).get(prop["id"], {})
            if policy.get("evidence_required_on_change") and prop["id"] not in covered:
                problems.append(problem(
                    "CONTRACT_EVIDENCE_MAPPING_MISSING", f"$.mappings.{prop['id']}",
                    "no evidence mapping covers this proposition"))
    return problems, stats


def has_supports_review(proposition_id, mappings_doc, mode="test"):
    for mapping in mappings_doc.get("mappings", []):
        if mapping.get("proposition_id") != proposition_id:
            continue
        if mapping.get("classification") != "SUPPORTS":
            continue
        ok, _ = _review_is_valid(mapping, mode)
        if ok:
            return True
    return False


def revalidate_mapping(mapping, context):
    """Revalidate one trusted evidence mapping against the actual source bytes."""
    problems = []
    at = f"$.mappings[{mapping.get('evidence_id')}]"
    contract = context.contracts_by_id.get(mapping.get("contract_id"))
    if not contract:
        return [problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at,
                        f"dangling contract reference {mapping.get('contract_id')!r}")]
    prop = next((p for p in contract.get("propositions", [])
                 if p["id"] == mapping.get("proposition_id")), None)
    if not prop:
        return [problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at,
                        f"dangling proposition reference {mapping.get('proposition_id')!r}")]
    try:
        path = context.resolve(mapping.get("document_path", ""))
    except TrustedPathError as exc:
        return [problem("CONTRACT_UNAUTHORIZED_PATH", at + ".document_path", str(exc))]
    if mapping.get("document_sha256") != sha256_file(path):
        problems.append(problem(
            "CONTRACT_EVIDENCE_INTEGRITY_FAILED", at + ".document_sha256",
            "stale evidence hash: the document bytes do not match the recorded hash"))
    block = section_block(read(path), mapping.get("section", ""))
    if not block or norm_text(mapping.get("excerpt", "")) not in norm_text(block):
        problems.append(problem(
            "CONTRACT_EVIDENCE_INTEGRITY_FAILED", at + ".excerpt",
            "the cited excerpt does not appear in the cited section"))
    prop_systems = set(prop.get("scope", {}).get("systems", []))
    map_systems = set(mapping.get("scope", {}).get("systems", []))
    if not prop_systems.issubset(map_systems):
        problems.append(problem(
            "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at + ".scope.systems",
            f"evidence scope {sorted(map_systems)} does not cover proposition scope {sorted(prop_systems)}"))
    review = mapping.get("review", {})
    mode = "test" if context.fixture_mode else "production"
    if review.get("review_status") == "REVIEWED":
        ok, why = _review_is_valid(mapping, mode)
        if not ok:
            problems.append(problem("CONTRACT_EVIDENCE_NOT_REVIEWED", at + ".review", why))
    elif mapping.get("classification") != "NOT_REVIEWED":
        problems.append(problem(
            "CONTRACT_EVIDENCE_NOT_REVIEWED", at + ".classification",
            "an unreviewed mapping must carry classification NOT_REVIEWED"))
    return problems


def evidence_gate(changed_props, mappings_doc, contracts, mode="production",
                  provisional_ids=None, allow_provisional=False,
                  context=None, evidence_refs=None):
    contracts = _contracts_by_id(contracts)
    problems = []
    provisional_ids = set(provisional_ids or [])
    provisional_open = []
    all_mappings = mappings_doc.get("mappings", [])
    target_contract_id = changed_props[0].get("contract_id") if changed_props else None
    if evidence_refs and context is not None:
        for ref in evidence_refs:
            mapping = context.mapping_by_id(ref)
            if not mapping:
                problems.append(problem(
                    "CONTRACT_EVIDENCE_MAPPING_MISSING", f"$.request.evidence_refs.{ref}",
                    f"referenced evidence identifier {ref!r} does not exist in the trusted registry"))
                continue
            if target_contract_id and mapping.get("contract_id") != target_contract_id:
                problems.append(problem(
                    "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", f"$.request.evidence_refs.{ref}",
                    "referenced evidence belongs to a different contract"))
                continue
            problems.extend(revalidate_mapping(mapping, context))
    for item in changed_props:
        cid = item.get("contract_id")
        pid = item.get("proposition_id")
        at = f"$.evidence.{cid}.{pid}"
        applicable = [m for m in all_mappings
                      if m.get("status") == "ACTIVE" and m.get("proposition_id") == pid]
        integrity_failed = False
        valid_mappings = []
        for mapping in applicable:
            mapping_problems = revalidate_mapping(mapping, context) if context is not None else []
            if mapping_problems:
                integrity_failed = True
                problems.extend(mapping_problems)
            else:
                valid_mappings.append(mapping)
        supports = [m for m in valid_mappings
                    if m.get("classification") == "SUPPORTS" and _review_is_valid(m, mode)[0]]
        contract = contracts.get(cid, {})
        prop = next((p for p in contract.get("propositions", []) if p["id"] == pid), {})
        if integrity_failed:
            continue
        if supports:
            prop_systems = set(prop.get("scope", {}).get("systems", []))
            map_systems = set(supports[0].get("scope", {}).get("systems", []))
            if prop_systems and not prop_systems.issubset(map_systems):
                problems.append(problem(
                    "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", at,
                    f"SUPPORTS scope {sorted(map_systems)} does not cover proposition scope {sorted(prop_systems)}"))
            continue
        reviewed = [m for m in valid_mappings if m.get("review", {}).get("review_status") == "REVIEWED"]
        contradictory = [m for m in reviewed if m.get("classification") == "CONTRADICTS"]
        not_established = [m for m in applicable
                           if m.get("classification") in ("NOT_ESTABLISHED", "CONTEXT_ONLY", "QUALIFIES")]
        if pid in provisional_ids and allow_provisional:
            provisional_open.append(pid)
            continue
        if contradictory:
            problems.append(problem(
                "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS", at,
                "the reviewed evidence CONTRADICTS the changed proposition"))
        elif not applicable:
            problems.append(problem(
                "CONTRACT_EVIDENCE_MAPPING_MISSING", at,
                "no governed evidence mapping exists for the changed proposition"))
        elif not_established:
            problems.append(problem(
                "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS", at,
                "the only evidence is NOT_ESTABLISHED/CONTEXT_ONLY and does not establish the changed proposition"))
        elif not supports:
            problems.append(problem(
                "CONTRACT_EVIDENCE_NOT_REVIEWED", at,
                "no independently reviewed SUPPORTS mapping exists for the changed proposition"))
    return {"passed": not problems, "problems": problems,
            "provisional_open": provisional_open}


# ---------------------------------------------------------------------------
# authority gate
# ---------------------------------------------------------------------------
def _owner_authorization_problems(decision_id, changed_props, owner_authorizations,
                                  mode="production"):
    problems = []
    for item in changed_props:
        pid = item.get("proposition_id")
        systems = set(item.get("systems", []))
        matched = []
        for auth in owner_authorizations:
            if auth.get("decision_id") != decision_id or auth.get("status") != "ACTIVE":
                continue
            if pid not in auth.get("scope", {}).get("propositions", []):
                continue
            if not systems.issubset(set(auth.get("scope", {}).get("systems", []))):
                continue
            matched.append(auth)
        if not matched:
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}",
                f"no ACTIVE owner authorization for {decision_id} covers proposition {pid}"))
            continue
        auth = matched[0]
        if mode == "production" and auth.get("fixture_only"):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}",
                "a test-fixture owner authorization cannot authorize a production amendment"))
            continue
        source = auth.get("instruction_source", "")
        path = os.path.join(DOCS, source) if source.startswith("qa_backups/") else os.path.join(REPO, source)
        if not os.path.isfile(path):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}.instruction_source",
                "the original owner-instruction source does not resolve"))
            continue
        if auth.get("instruction_sha256") != sha256_file(path):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}.instruction_sha256",
                "the owner-instruction source hash does not match"))
        quote = norm_text(auth.get("quoted_instruction", ""))
        if not quote or quote not in norm_text(read(path)):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}.quoted_instruction",
                "the quoted owner instruction does not appear in the source"))
        if any(t in (auth.get("quoted_instruction") or "").upper()
               for t in ("TEMP-OWNER", "PLACEHOLDER", "NOT A REAL OWNER INSTRUCTION")):
            problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", f"$.owner_authorizations.{pid}",
                "placeholder owner authorization is not authentic"))
    return problems


def authority_gate(decision_id, changed_props, base_contract, candidate_contract,
                   decisions_text, owner_authorizations,
                   mode="production", typed=False):
    problems = []
    headers, records, malformed, dupes = parse_decisions(decisions_text)
    matches = [r for r in records if r["_id"] == decision_id]
    if decision_id in dupes:
        return {"passed": False, "category": "", "problems": [problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
            f"decision {decision_id} appears more than once")]}
    if len(matches) != 1:
        return {"passed": False, "category": "", "problems": [problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
            f"decision {decision_id} does not exist exactly once")]}
    rec = matches[0]
    state = decision_state(rec)
    category = state["category"]
    status = state["status"]
    combined = " ".join(decision_cell(rec, k) for k in ("topic", "decision", "reason", "source", "consequences"))
    if not category:
        problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
                                f"decision {decision_id} has no explicit D-014 category"))
    if state["inactive"]:
        problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
                                f"decision {decision_id} is pending, rejected, deferred or superseded"))
    if base_contract.get("clause_id") not in combined and base_contract.get("contract_id") not in combined:
        problems.append(problem("CONTRACT_SCOPE_MISMATCH", "$.decisions",
                                f"decision {decision_id} does not name {base_contract.get('clause_id')} or {base_contract.get('contract_id')}"))
    if typed and candidate_contract.get("effective_decision") != decision_id:
        problems.append(problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.request.candidate_contract.effective_decision",
            f"candidate effective_decision {candidate_contract.get('effective_decision')!r} does not match decision_ref {decision_id!r}"))
    if typed:
        previous = marker(decision_cell(rec, "decision"), r"previous contract", [r"replacement contract", r"alternatives", r"consequences", r"reopening"])
        replacement = marker(decision_cell(rec, "decision"), r"replacement contract", [r"alternatives", r"consequences", r"reopening"])
        alternatives = marker(decision_cell(rec, "decision"), r"alternatives", [r"consequences", r"reopening"])
        consequences = decision_cell(rec, "consequences")
        reopening = marker(decision_cell(rec, "decision"), r"reopening", [r"consequences", r"alternatives"]) or \
            marker(consequences, r"reopening", [r"$"])
        if base_contract.get("contract_id") not in previous or base_contract.get("contract_version") not in previous:
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.previous_contract",
                                    "decision does not state the previous contract ID and version"))
        if candidate_contract.get("contract_id") not in replacement or candidate_contract.get("contract_version") not in replacement:
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.replacement_contract",
                                    "decision does not state the replacement contract ID and version"))
        if not substantive(alternatives, 20):
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.alternatives",
                                    "decision does not record substantive alternatives"))
        if not substantive(decision_cell(rec, "reason"), 30):
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.rationale",
                                    "decision rationale/evidence is missing or generic"))
        if "evidence:" not in decision_cell(rec, "reason").lower():
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.evidence",
                                    "decision does not reference governed evidence"))
        if not substantive(consequences, 30):
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.consequences",
                                    "decision does not record substantive consequences"))
        if not substantive(reopening, 15):
            problems.append(problem("CONTRACT_AUTHORITY_MISMATCH", "$.decisions.reopening",
                                    "decision does not record reopening conditions"))
    for item in changed_props:
        pid = item["proposition_id"]
        base_prop = next((p for p in base_contract.get("propositions", []) if p["id"] == pid), None)
        cand_prop = next((p for p in candidate_contract.get("propositions", []) if p["id"] == pid), None)
        base_auth = (base_prop or {}).get("authority", {})
        cand_auth = (cand_prop or {}).get("authority", {})
        policy = (base_contract.get("change_policy", {}).get("propositions", {}).get(pid) or
                  candidate_contract.get("change_policy", {}).get("propositions", {}).get(pid, {}))
        owner_change = (base_auth.get("owner_reserved") or cand_auth.get("owner_reserved") or
                        base_auth.get("category") in ("A", "D") or cand_auth.get("category") in ("A", "D"))
        if owner_change and category not in ("A", "D"):
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                f"owner-reserved or Category A/D proposition {pid} cannot be changed by a Category {category or '?'} decision"))
            continue
        classification_change = (base_prop is not None and cand_prop is not None and
                                 (base_auth.get("owner_reserved") != cand_auth.get("owner_reserved") or
                                  base_auth.get("category") != cand_auth.get("category") or
                                  base_auth.get("classification_status") != cand_auth.get("classification_status")))
        if classification_change and category != "A":
            problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                f"authority-classification change for {pid} requires authentic Category A owner authorization"))
        if category == "B":
            if policy.get("category") != "B" or base_auth.get("owner_reserved") or cand_auth.get("owner_reserved"):
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                    f"Category B cannot change owner-reserved proposition {pid}"))
            if not state["confirmed"]:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.status",
                    "Category B decision is not Confirmed"))
            if candidate_contract.get("lifecycle_status") != base_contract.get("lifecycle_status"):
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.candidate_contract.lifecycle_status",
                    "Category B cannot change the contract lifecycle status"))
            for did in set(cand_auth.get("basis_decisions", [])) | set(base_auth.get("basis_decisions", [])):
                if did == decision_id:
                    problems.append(problem(
                        "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}.authority",
                        "a proposition cannot cite the amendment decision as its own authority"))
        elif category == "C":
            if not state["provisional"]:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.status",
                    "Category C decision is not Provisional"))
            if not any(w in combined.lower() for w in ("missing evidence", "test:", "owner:")):
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.decisions",
                    "Category C decision does not name the missing evidence or confirming test"))
            if typed and candidate_contract.get("lifecycle_status") != "ADOPTED_PROVISIONAL":
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.contract.lifecycle_status",
                    "Category C typed amendment must remain ADOPTED_PROVISIONAL"))
            if cand_auth.get("classification_status") == "RESOLVED":
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                    "Category C cannot promote a provisional proposition to RESOLVED"))
            if base_auth.get("owner_reserved"):
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                    "Category C cannot change an owner-reserved proposition"))
        elif category in ("A", "D"):
            if not state["owner"]:
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.status",
                    "Category A/D decision lacks explicit owner authorization in its status"))
            if not cand_auth.get("owner_reserved") and not base_auth.get("owner_reserved"):
                problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{pid}",
                    "Category A/D decision targets a proposition that is not owner-reserved"))
            problems.extend(_owner_authorization_problems(
                decision_id, [{"proposition_id": pid,
                               "systems": (cand_prop or base_prop or {}).get("scope", {}).get("systems", [])}],
                owner_authorizations, mode))
    return {"passed": not problems, "category": category, "problems": problems}


# ---------------------------------------------------------------------------
# manifest
# ---------------------------------------------------------------------------
ALLOWED_MANIFEST_KEYS = {
    "clause", "source_document", "previous_hash", "new_hash", "decision_id",
    "category", "decision_status", "authorization_evidence", "rationale",
    "regression_evidence", "owner_reserved", "required_phrases",
    "previous_contract_version", "new_contract_version",
    "previous_contract_sha256", "new_contract_sha256", "new_projection_sha256",
}


def validate_manifest_entry(entry, fid, base_contract, candidate_contract,
                            candidate_clause, candidate_projection,
                            manifest_sha_known=True):
    problems = []
    at = "$.manifest"
    if not isinstance(entry, dict):
        return [problem("CONTRACT_MANIFEST_INVALID", at, "manifest entry is not an object")]
    for key in entry:
        if key not in ALLOWED_MANIFEST_KEYS:
            problems.append(problem(
                "CONTRACT_MANIFEST_INVALID", f"{at}.{key}",
                f"manifest field {key!r} is not permitted; an amendment cannot supply evidence, a lexicon or a contract definition"))
    for field in ("clause", "source_document", "previous_hash", "new_hash",
                  "decision_id", "category", "decision_status",
                  "authorization_evidence", "rationale", "regression_evidence"):
        if not entry.get(field):
            problems.append(problem("CONTRACT_MANIFEST_INVALID", f"{at}.{field}",
                                    "mandatory manifest field is empty"))
    if entry.get("clause") != fid:
        problems.append(problem("CONTRACT_MANIFEST_INVALID", f"{at}.clause",
                                f"manifest clause {entry.get('clause')!r} does not match {fid}"))
    if entry.get("source_document") != base_contract.get("source_document"):
        problems.append(problem("CONTRACT_MANIFEST_INVALID", f"{at}.source_document",
                                "manifest source document is not the contract source document"))
    if entry.get("previous_hash") != base_contract.get("baseline_source_hash"):
        problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.previous_hash",
                                "manifest previous_hash is not the preserved baseline hash"))
    if entry.get("new_hash") != source_clause_sha256(candidate_clause):
        problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.new_hash",
                                "manifest new_hash does not match the candidate source clause"))
    if entry.get("new_contract_version"):
        if entry.get("previous_contract_version") != base_contract.get("contract_version"):
            problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.previous_contract_version",
                                    "manifest previous_contract_version is not the baseline contract version"))
        if entry.get("new_contract_version") != candidate_contract.get("contract_version"):
            problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.new_contract_version",
                                    "manifest new_contract_version does not match the candidate contract"))
        if entry.get("previous_contract_sha256") != contract_sha256(base_contract):
            problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.previous_contract_sha256",
                                    "manifest previous_contract_sha256 does not match the baseline contract"))
        if entry.get("new_contract_sha256") != contract_sha256(candidate_contract):
            problems.append(problem("CONTRACT_FINGERPRINT_MISMATCH", f"{at}.new_contract_sha256",
                                    "manifest new_contract_sha256 does not match the candidate contract"))
        if entry.get("new_projection_sha256") and \
                entry["new_projection_sha256"] != projection_sha256(candidate_projection):
            problems.append(problem("CONTRACT_PROJECTION_MISMATCH", f"{at}.new_projection_sha256",
                                    "manifest projection fingerprint does not match the rendered candidate"))
    return problems


# ---------------------------------------------------------------------------
# context evidence (legacy decision Evidence block)
# ---------------------------------------------------------------------------
def _evidence_block(reason_cell):
    m = re.search(r"Evidence:\s*(.*?)(?=\bRationale\b|$)", reason_cell or "", re.I | re.S)
    return m.group(1) if m else ""


def _authorized_loci(contract_id, mappings_doc):
    return {(m.get("document_path"), m.get("section"))
            for m in mappings_doc.get("mappings", [])
            if m.get("contract_id") == contract_id and m.get("status") == "ACTIVE"}


def context_evidence_problems(contract, decision_record, lexicon, mappings_doc):
    problems = []
    reason = decision_cell(decision_record, "reason")
    block = _evidence_block(reason)
    if not block:
        return [problem("CONTRACT_EVIDENCE_MAPPING_MISSING", "$.decisions.reason",
                        "no structured Evidence block")]
    path_m = re.search(r"path\s*=\s*([^;]+)", block, re.I)
    section_m = re.search(r"section\s*=\s*([^;]+)", block, re.I)
    quote_m = re.search(r"quote\s*=\s*[\"“](.+?)[\"”]", block, re.I | re.S)
    supports_m = re.search(r"supports\s*=\s*([^;]+)", block, re.I)
    stance_m = re.search(r"stance\s*=\s*([a-z_]+)", block, re.I)
    if not (path_m and section_m and quote_m and supports_m and stance_m):
        return [problem("CONTRACT_EVIDENCE_MAPPING_MISSING", "$.decisions.reason",
                        "Evidence block must state path, section, quote, supports and stance")]
    path = path_m.group(1).strip()
    section = section_m.group(1).strip()
    quote = quote_m.group(1).strip()
    supports = supports_m.group(1).strip()
    stance = stance_m.group(1).strip().lower()
    loci = _authorized_loci(contract["contract_id"], mappings_doc)
    if (path, section) not in loci:
        return [problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", "$.decisions.reason.path",
                        f"evidence locus is not an authorized source for {contract['clause_id']}: {path} section {section}")]
    if stance != "supports":
        problems.append(problem("CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                                "$.decisions.reason.stance",
                                f"declared evidence stance is {stance!r}, not 'supports'"))
    full = os.path.join(REPO, path)
    if not os.path.isfile(full):
        return [problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", "$.decisions.reason.path",
                        f"evidence path does not resolve: {path}")]
    block = section_block(read(full), section)
    if not block or norm_text(quote) not in norm_text(block):
        problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
                                "$.decisions.reason.quote",
                                "quoted evidence does not appear in the cited section"))
    quote_concepts = {c["concept_id"] for c in concept_matches(quote, lexicon)}
    support_concepts = {c["concept_id"] for c in concept_matches(supports, lexicon)}
    if not quote_concepts or not (quote_concepts & support_concepts):
        problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
                                "$.decisions.reason.supports",
                                "supports-claim is not substantiated by the quoted evidence; the cited evidence does not establish the claimed proposition"))
    elif support_concepts - quote_concepts:
        problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
                                "$.decisions.reason.supports",
                                "the supports-claim introduces concepts absent from the quote and does not establish the claimed proposition"))
    low_support = supports.lower()
    low_quote = quote.lower()
    for term in FOREIGN_DOMAIN_TERMS:
        if term in low_support and term not in low_quote:
            problems.append(problem("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
                                    "$.decisions.reason.supports",
                                    f"unrelated domain term {term!r} in the supports-claim does not establish the claimed proposition"))
            break
    q_rel = _basis_relation(quote)
    s_rel = _basis_relation(supports)
    if q_rel and s_rel and q_rel != s_rel:
        problems.append(problem("CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                                "$.decisions.reason.supports",
                                "the basis-point relationship contradicts the cited evidence"))
    quote_mod = normalize_modality(quote)
    support_mod = normalize_modality(supports)
    shared = quote_concepts & support_concepts
    if shared and quote_mod and support_mod:
        if quote_mod == "PROHIBIT" and support_mod in ("PERMIT", "MANDATE"):
            problems.append(problem("CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                                    "$.decisions.reason.supports",
                                    "the cited passage prohibits what the supports-claim asserts"))
        if quote_mod == "PERMIT" and support_mod == "PROHIBIT":
            problems.append(problem("CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                                    "$.decisions.reason.supports",
                                    "the cited passage permits what the supports-claim denies"))
    return problems


# ---------------------------------------------------------------------------
# amendment validator
# ---------------------------------------------------------------------------
def _changed_for_gate(changed_ids, contracts, candidate_contract, base_contract):
    out = []
    for pid in changed_ids:
        prop = next((p for p in candidate_contract.get("propositions", []) if p["id"] == pid), None)
        base_prop = next((p for p in base_contract.get("propositions", []) if p["id"] == pid), None)
        cid = candidate_contract.get("contract_id") or base_contract.get("contract_id")
        out.append({
            "contract_id": cid,
            "proposition_id": pid,
            "systems": (prop or base_prop or {}).get("scope", {}).get("systems", []),
        })
    return out


def _reject_report(problems, gate="contract_gate"):
    gate_obj = {"passed": False, "problems": list(problems)}
    return {
        "accepted": False,
        "request_gate": gate_obj if gate == "request_gate" else {"passed": True, "problems": []},
        "contract_gate": gate_obj if gate == "contract_gate" else {"passed": False, "problems": []},
        "evidence_gate": {"passed": False, "problems": [], "provisional_open": []},
        "authority_gate": {"passed": False, "problems": []},
        "comparison_gate": gate_obj if gate == "comparison_gate" else {"passed": False, "problems": []},
        "diff": {"added": [], "removed": [], "changed": [], "unchanged": []},
        "coverage": {},
        "ingestion": {},
    }


def _candidate_identity_problems(base, candidate, decision_id, context):
    problems = []
    checks = (
        ("contract_id", "CONTRACT_SCOPE_MISMATCH"),
        ("clause_id", "CONTRACT_SCOPE_MISMATCH"),
        ("source_document", "CONTRACT_SCOPE_MISMATCH"),
        ("baseline_source_hash", "CONTRACT_FINGERPRINT_MISMATCH"),
        ("schema_version", "CONTRACT_SCHEMA_INVALID"),
    )
    for field, code in checks:
        if candidate.get(field) != base.get(field):
            problems.append(problem(
                code, f"$.request.candidate_contract.{field}",
                f"candidate {field} does not match the trusted baseline"))
    if candidate.get("rendering", {}).get("template_path") != \
            base.get("rendering", {}).get("template_path"):
        problems.append(problem(
            "CONTRACT_TRUSTED_INPUT_OVERRIDE",
            "$.request.candidate_contract.rendering.template_path",
            "a candidate amendment may not substitute a different projection template path"))
    if candidate.get("effective_decision") != decision_id:
        problems.append(problem(
            "CONTRACT_AUTHORITY_MISMATCH",
            "$.request.candidate_contract.effective_decision",
            "candidate effective_decision does not equal the request decision_ref"))
    if candidate.get("contract_version") == base.get("contract_version"):
        problems.append(problem(
            "CONTRACT_SCHEMA_INVALID",
            "$.request.candidate_contract.contract_version",
            "a changed contract must carry a new contract version"))
    for rel, label in ((candidate.get("source_document", ""), "source_document"),
                       (candidate.get("rendering", {}).get("template_path", ""), "template_path")):
        try:
            if label == "template_path":
                context.resolve_contract_artifact(rel)
            else:
                context.resolve(rel)
        except TrustedPathError as exc:
            problems.append(problem(
                "CONTRACT_UNAUTHORIZED_PATH",
                f"$.request.candidate_contract.{label}", str(exc)))
    return problems


def _comparison_gate(base, candidate, diff):
    problems = []
    for change in diff.get("material_contract_changes", []):
        problems.append(problem(
            "CONTRACT_CONTRACT_FIELD_CHANGE",
            f"$.request.candidate_contract.{change['field']}",
            f"material contract-level field {change['field']!r} changed and requires a governed extension; this path fails closed"))
    if not diff.get("all_changed") and not diff.get("wording_contract_changes"):
        problems.append(problem(
            "CONTRACT_CONTRACT_FIELD_CHANGE", "$.request.candidate_contract",
            "the candidate contract changes no proposition and no projection wording"))
    return problems


def _classify_metadata_changes(diff, contract_ok, authority_passed, category,
                               decision_ref, context, base, candidate):
    """Reporting classification only; it never makes a metadata change valid."""
    for item in diff.get("metadata_changes", []):
        if not item.get("changed"):
            item["classification"] = "UNCHANGED"
            continue
        field = item["field"]
        proposed = item.get("proposed")
        if field == "contract_version":
            if not isinstance(proposed, str) or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", proposed)                     or proposed == item.get("previous"):
                item["classification"] = "INVALID"
            elif not authority_passed:
                item["classification"] = "UNAUTHORIZED"
            elif category == "C":
                item["classification"] = "PROVISIONAL"
            else:
                item["classification"] = "AUTHORIZED"
        elif field == "effective_decision":
            proposed_row = context.decision_row(proposed) if isinstance(proposed, str) else None
            if not isinstance(proposed, str) or not re.fullmatch(r"D-[0-9]{3}", proposed)                     or proposed_row is None:
                item["classification"] = "INVALID"
            elif proposed != decision_ref:
                item["classification"] = "UNAUTHORIZED"
            elif not authority_passed:
                item["classification"] = "UNAUTHORIZED"
            elif category == "C":
                item["classification"] = "PROVISIONAL"
            else:
                item["classification"] = "AUTHORIZED"
        elif field == "lifecycle_status":
            if proposed not in {"SHADOW", "ADOPTED", "ADOPTED_PROVISIONAL",
                                "SUPERSEDED", "RETIRED"}:
                item["classification"] = "INVALID"
            elif not authority_passed:
                item["classification"] = "UNAUTHORIZED"
            elif category == "C" and proposed == "ADOPTED_PROVISIONAL":
                item["classification"] = "PROVISIONAL"
            elif proposed == "ADOPTED":
                item["classification"] = "AUTHORIZED"
            else:
                item["classification"] = "UNAUTHORIZED"
        else:
            item["classification"] = "UNAUTHORIZED" if not authority_passed else "AUTHORIZED"
    return diff


def _validate_amendment_with_context(request, context):
    fid = context.contract_for_target(request.get("target_contract"))
    if not fid:
        return _reject_report([problem(
            "CONTRACT_SCOPE_MISMATCH", "$.request.target_contract",
            f"target contract {request.get('target_contract')!r} is not in the trusted registry")],
            gate="request_gate")
    base = context.contracts[fid]
    clause = extract_clause(request.get("candidate_document", ""), fid)
    if not clause:
        return _reject_report([problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request.candidate_document",
            f"candidate document does not contain clause {fid}")], gate="request_gate")
    decision_id = request["decision_ref"]
    mode = "test" if context.fixture_mode else "production"
    candidate = request.get("candidate_contract")
    contract_problems = []
    comparison_problems = []
    evidence_result = {"passed": False, "problems": [], "provisional_open": []}
    authority_result = {"passed": False, "category": "", "problems": []}
    coverage = {}
    ingestion = {}
    diff = {"added": [], "removed": [], "changed": [], "unchanged": [],
            "all_changed": [], "material_contract_changes": []}
    report = {
        "accepted": False,
        "request_gate": {"passed": True, "problems": []},
        "contract_gate": {"passed": False, "problems": contract_problems},
        "evidence_gate": evidence_result,
        "authority_gate": authority_result,
        "comparison_gate": {"passed": False, "problems": comparison_problems},
        "diff": diff,
        "coverage": coverage,
        "ingestion": ingestion,
        "mode": mode,
    }
    if candidate is None:
        # Prose ingestion: accepted only as a restatement of the same typed propositions.
        ingestion = ingest_clause(base, clause, context.lexicon)
        report["ingestion"] = ingestion
        coverage = ingestion["coverage"]
        report["coverage"] = coverage
        contract_problems.extend(ingestion["problems"])
        if ingestion["status"] == "CHANGED":
            contract_problems.append(problem(
                "CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.request.candidate_document",
                "a semantic change must be expressed as a typed candidate contract; prose alone is not an acceptance route"))
            comparison_problems.append(problem(
                "CONTRACT_UNPARSED_MATERIAL_SEGMENT", "$.request.candidate_document",
                "the candidate changes the proposition set without a typed contract patch"))
        if ingestion["status"] == "REJECTED":
            comparison_problems.append(problem(
                "CONTRACT_COVERAGE_GAP", "$.request.candidate_document",
                "the candidate clause does not completely account for the controlled material"))
        changed = []
        for item in ingestion.get("changed", []):
            changed.append({
                "contract_id": base["contract_id"],
                "proposition_id": item["proposition_id"],
                "systems": next((p.get("scope", {}).get("systems", [])
                                 for p in base.get("propositions", [])
                                 if p["id"] == item["proposition_id"]), []),
            })
        for added in ingestion.get("added", []):
            changed.append({
                "contract_id": base["contract_id"],
                "proposition_id": "NC-F-EC-000b/P-005" if fid == "F-EC-000b" else "NC-F-EC-000f/P-006",
                "systems": base.get("scope", {}).get("systems", []),
            })
        report["diff"] = {
            "added": [], "removed": [r["proposition_id"] for r in ingestion.get("removed", [])],
            "changed": [c["proposition_id"] for c in ingestion.get("changed", [])],
            "unchanged": [], "all_changed": sorted({c["proposition_id"] for c in changed}),
            "material_contract_changes": [], "metadata_changes": [],
        }
        evidence_result = evidence_gate(
            changed, context.mappings, {base["contract_id"]: base}, mode,
            context=context, evidence_refs=request.get("evidence_refs"))
        authority_result = authority_gate(
            decision_id, changed, base, base, context.decisions_text,
            context.owner_authorizations, mode, typed=False)
        if ingestion["status"] in ("BASELINE", "WORDING_ONLY"):
            row = context.decision_row(decision_id)
            if ingestion["status"] == "BASELINE":
                authority_result = {"passed": True, "category": "", "problems": []}
                evidence_result = {"passed": True, "problems": [], "provisional_open": []}
            elif row:
                authority_result["problems"].extend(
                    context_evidence_problems(base, row, context.lexicon, context.mappings))
                authority_result["passed"] = not authority_result["problems"]
            else:
                authority_result["problems"].append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.request.decision_ref",
                    f"decision {decision_id} does not exist exactly once in the trusted decision register"))
                authority_result["passed"] = False
        report["evidence_gate"] = evidence_result
        report["authority_gate"] = authority_result
        report["contract_gate"] = {"passed": not contract_problems,
                                   "problems": contract_problems}
        report["comparison_gate"] = {"passed": not comparison_problems,
                                     "problems": comparison_problems}
        report["accepted"] = (report["contract_gate"]["passed"] and
                              report["comparison_gate"]["passed"] and
                              evidence_result["passed"] and authority_result["passed"])
        return report

    # Typed candidate contract.
    schema_problems = validate_schema(
        candidate, {"$ref": "#/$defs/contract"}, context.schema,
        "$.request.candidate_contract")
    contract_problems.extend(schema_problems)
    contract_problems.extend(_candidate_identity_problems(
        base, candidate, decision_id, context))
    contract_problems.extend(validate_contract_semantics(
        candidate, context.schema, context.lexicon, context.decisions_text,
        request.get("candidate_document"), mode="test"))
    rendered, render_problems = render_contract(candidate)
    contract_problems.extend(render_problems)
    if norm_text(rendered) != norm_text(clause):
        contract_problems.append(problem(
            "CONTRACT_PROJECTION_MISMATCH", "$.request.candidate_document",
            "the candidate document does not equal the projection rendered from the typed contract"))
    coverage = material_coverage(candidate, clause)
    report["coverage"] = coverage
    if not coverage["exact"] or coverage["uncovered_material"]:
        contract_problems.append(problem(
            "CONTRACT_COVERAGE_GAP", "$.request.candidate_document",
            f"complete material coverage failed; uncovered={coverage['uncovered_material']}"))
    diff = diff_contracts(base, candidate)
    report["diff"] = diff
    comparison_problems.extend(_comparison_gate(base, candidate, diff))
    if not diff["all_changed"]:
        wording_ingest = ingest_clause(base, clause, context.lexicon)
        report["ingestion"] = wording_ingest
        if wording_ingest["status"] not in ("BASELINE", "WORDING_ONLY") or wording_ingest["problems"]:
            comparison_problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", "$.request.candidate_document",
                "a rendering-only change must parse to the same typed proposition set; "
                + "; ".join(fmt(p) for p in wording_ingest["problems"])))
    gate_contracts = {base["contract_id"]: base}
    gate_contracts[candidate.get("contract_id", base["contract_id"])] = candidate
    gate_context = copy.copy(context)
    gate_context.contracts_by_id = dict(context.contracts_by_id)
    gate_context.contracts_by_id[candidate.get("contract_id", base["contract_id"])] = candidate
    changed = _changed_for_gate(diff["all_changed"], gate_contracts, candidate, base)
    row = context.decision_row(decision_id)
    category = decision_state(row)["category"] if row else ""
    provisional = diff["all_changed"] if category == "C" else []
    evidence_result = evidence_gate(
        changed, context.mappings, gate_contracts, mode,
        provisional, allow_provisional=bool(provisional),
        context=gate_context, evidence_refs=request.get("evidence_refs"))
    authority_result = authority_gate(
        decision_id, changed, base, candidate, context.decisions_text,
        context.owner_authorizations, mode, typed=True)
    _classify_metadata_changes(
        diff, report["contract_gate"]["passed"], authority_result["passed"],
        authority_result.get("category", ""), decision_id, context, base, candidate)
    report["evidence_gate"] = evidence_result
    report["authority_gate"] = authority_result
    report["contract_gate"] = {"passed": not contract_problems,
                               "problems": contract_problems}
    report["comparison_gate"] = {"passed": not comparison_problems,
                                 "problems": comparison_problems}
    report["accepted"] = (report["contract_gate"]["passed"] and
                          report["comparison_gate"]["passed"] and
                          evidence_result["passed"] and authority_result["passed"])
    return report


def validate_amendment(request):
    """Production amendment entry point.

    Plain dictionaries are strictly schema-checked and validated against the
    cached trusted repository context. FixtureRequest instances are created only
    by the regression harness and carry an explicitly constructed fixture
    context; they are never produced by production JSON input.
    """
    if isinstance(request, FixtureRequest):
        context = request.fixture_context
        if not getattr(context, "fixture_mode", False):
            return _reject_report([problem(
                "CONTRACT_FIXTURE_MODE_FORBIDDEN", "$.request",
                "a fixture context may not be used outside the regression harness")],
                gate="request_gate")
        return _validate_amendment_with_context(dict(request), context)
    if not isinstance(request, dict):
        return _reject_report([problem(
            "CONTRACT_REQUEST_SCHEMA_INVALID", "$.request",
            "amendment request must be an object")], gate="request_gate")
    request_problems = validate_request_schema(request)
    if request_problems:
        return _reject_report(request_problems, gate="request_gate")
    context = get_trusted_context()
    if context.problems:
        return _reject_report(context.problems, gate="contract_gate")
    return _validate_amendment_with_context(request, context)

# ---------------------------------------------------------------------------
# production validation
# ---------------------------------------------------------------------------
def _check(cid, description, problems):
    return {"id": cid, "description": description,
            "passed": not problems, "problems": problems}


def _fmt_problems(problems):
    return [fmt(p) for p in problems]


def validate_production(contracts_dir=CONTRACTS, decisions_path=DECISIONS,
                        b04_path=B04, b14_path=B14, b09_path=B09,
                        policy_path=POLICY, mode="production"):
    artifacts = load_artifacts(contracts_dir, mode)
    problems = list(artifacts.get("problems", []))
    index = artifacts.get("index", {})
    schema = artifacts.get("schema", {})
    lexicon = artifacts.get("lexicon", {})
    mappings = artifacts.get("mappings", {})
    contracts = artifacts.get("contracts", {})
    decisions_text = read(decisions_path)
    b04_text = read(b04_path)
    b14_text = read(b14_path)
    b09_text = read(b09_path)
    policy_text = read(policy_path)
    checks = []
    # C-01 registry + schema
    registry_problems = validate_registry(artifacts, decisions_text, mode)
    checks.append(_check("C-01", "Contract registry, strict schema, lexicon and closed enumerations validate", registry_problems))
    # C-02 contract semantics and authority metadata
    semantics = list(problems)
    for clause, contract in contracts.items():
        source_text = b04_text if clause.startswith("F-EC-") else None
        semantics.extend(validate_contract_semantics(
            contract, schema, lexicon, decisions_text, source_text, mode))
    checks.append(_check("C-02", "Both controlled contracts satisfy the typed schema and semantic rules", semantics))
    # C-03 projection equivalence and coverage
    projection_problems = []
    coverage_report = {}
    for clause, contract in contracts.items():
        clause_text = extract_clause(b04_text, clause)
        rendered, render_problems = render_contract(contract)
        projection_problems.extend(render_problems)
        if norm_text(rendered) != norm_text(clause_text):
            projection_problems.append(problem(
                "CONTRACT_PROJECTION_MISMATCH", f"$.contracts.{clause}",
                "rendered projection does not equal the preserved B-04 clause"))
        if source_clause_sha256(clause_text) != BASELINE_HASHES[clause]:
            projection_problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.source.{clause}",
                "source clause hash is not the preserved baseline hash"))
        cov = material_coverage(contract, clause_text)
        coverage_report[clause] = cov
        if cov["missing"] or cov["leftover"] or cov["ratio"] != 1.0:
            projection_problems.append(problem(
                "CONTRACT_UNPARSED_MATERIAL_SEGMENT", f"$.coverage.{clause}",
                f"material coverage is {cov['covered']}/{cov['segments']}; "
                f"missing={cov['missing']} leftover={cov['leftover']!r}"))
    checks.append(_check("C-03", "B-04 projections match the preserved clauses with 100% material coverage", projection_problems))
    # C-04 fingerprints and determinism
    fingerprint_problems = []
    for clause, contract in contracts.items():
        ref = artifacts.get("referenced", {}).get(contract["contract_id"], {})
        rendered, _ = render_contract(contract)
        if ref.get("contract_sha256") != contract_sha256(contract):
            fingerprint_problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.contracts.{contract['contract_id']}",
                "contract fingerprint mismatch"))
        if ref.get("projection_sha256") != projection_sha256(rendered):
            fingerprint_problems.append(problem(
                "CONTRACT_PROJECTION_MISMATCH", f"$.index.contracts.{contract['contract_id']}.projection_sha256",
                "projection fingerprint mismatch"))
        if ref.get("material_coverage", {}).get("ratio") != coverage_report.get(clause, {}).get("ratio"):
            fingerprint_problems.append(problem(
                "CONTRACT_FINGERPRINT_MISMATCH", f"$.index.contracts.{contract['contract_id']}",
                "recorded coverage does not match the recomputed coverage"))
    first = json.dumps(_report_payload(contracts, coverage_report, mappings), sort_keys=True)
    second = json.dumps(_report_payload(contracts, coverage_report, mappings), sort_keys=True)
    if first != second:
        fingerprint_problems.append(problem(
            "CONTRACT_FINGERPRINT_MISMATCH", "$.determinism",
            "repeated canonical serialization differs"))
    if not re.search(r"^\s*(?:import|from)\s+(?:socket|urllib|http|requests|random|asyncio)",
                     read(__file__), re.M):
        pass
    else:
        fingerprint_problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", "$.runtime",
            "a network, model or randomness dependency was imported"))
    checks.append(_check("C-04", "Contract, projection and source fingerprints are recomputed deterministically", fingerprint_problems))
    # C-05 evidence integrity
    evidence_problems, evidence_stats = evidence_integrity(mappings, contracts, mode)
    checks.append(_check("C-05", "Evidence mappings are source-verified, scoped and honestly unreviewed", evidence_problems))
    # C-06 D-014 authority
    authority_problems = []
    headers, records, malformed, dupes = parse_decisions(decisions_text)
    by_decision = {r["_id"]: r for r in records}
    adoption = by_decision.get(ADOPTION_DECISION)
    if ADOPTION_DECISION in dupes or not adoption:
        authority_problems.append(problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.D-238",
            "the contract-adoption decision does not exist exactly once"))
    else:
        state = decision_state(adoption)
        if state["category"] != "B" or not state["confirmed"]:
            authority_problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.D-238",
                "the contract-adoption decision is not Confirmed Category B"))
        combined = " ".join(decision_cell(adoption, k) for k in ("topic", "decision", "reason", "source", "consequences"))
        for token in ("NC-F-EC-000b", "NC-F-EC-000f", "alternatives", "reopening"):
            if token.lower() not in combined.lower():
                authority_problems.append(problem(
                    "CONTRACT_AUTHORITY_MISMATCH", "$.decisions.D-238",
                    f"the adoption decision does not record {token}"))
    for did in ("D-014", "D-045", "D-064"):
        rec = by_decision.get(did)
        if not rec:
            authority_problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{did}",
                f"{did} is missing from DECISIONS.md"))
        elif decision_state(rec)["inactive"]:
            authority_problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.decisions.{did}",
                f"{did} is inactive"))
    if index.get("adoption_decision") != ADOPTION_DECISION:
        authority_problems.append(problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.index.adoption_decision",
            "index adoption decision does not match D-238"))
    if index.get("preserved_baseline", {}).get("d014_policy_sha256") != sha256_file(policy_path):
        authority_problems.append(problem(
            "CONTRACT_FINGERPRINT_MISMATCH", "$.index.preserved_baseline.d014_policy_sha256",
            "D-014 policy file bytes have changed"))
    for clause, contract in contracts.items():
        if contract.get("effective_decision") != ADOPTION_DECISION:
            authority_problems.append(problem(
                "CONTRACT_AUTHORITY_MISMATCH", f"$.contracts.{clause}.effective_decision",
                "contract effective_decision is not the adoption decision"))
    for entry in index.get("owner_authorizations", []):
        if entry.get("fixture_only") and mode == "production":
            authority_problems.append(problem(
                "CONTRACT_OWNER_AUTHORIZATION_MISSING", "$.index.owner_authorizations",
                "production owner_authorizations may not contain test fixtures"))
    checks.append(_check("C-06", "D-014 authority, adoption decision and owner-authorization provenance are separate and enforced", authority_problems))
    # C-07 gate regression matrix
    reg_problems, reg_results = regression_matrix()
    checks.append(_check("C-07", "Evidence and authority gates operate independently on the mandatory regression matrix", reg_problems))
    # C-08 scope isolation and preservation
    scope_problems = []
    if "B-09" in contracts.get("F-EC-000b", {}).get("scope", {}).get("systems", []):
        scope_problems.append(problem(
            "CONTRACT_SCOPE_MISMATCH", "$.contracts.F-EC-000b.scope.systems",
            "F-EC-000b must not be widened to B-09"))
    p005 = next((p for p in contracts.get("F-EC-000b", {}).get("propositions", [])
                 if p["id"].endswith("P-005")), None)
    if not p005 or "CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN" not in \
            p005.get("scope", {}).get("distinct_from", []):
        scope_problems.append(problem(
            "CONTRACT_SCOPE_MISMATCH", "$.contracts.F-EC-000b.P-005",
            "cross-turn remainder persistence is not kept distinct from within-turn cumulative accrual"))
    if "F-AL-006 — Automatic Per-Turn Production Tax Arithmetic" not in b09_text:
        scope_problems.append(problem(
            "CONTRACT_SCOPE_MISMATCH", "$.source.B-09",
            "B-09 F-AL-006 heading is missing"))
    for needle in ("cumulative", "10{,}000", "Different assets keep separate accumulators"):
        if needle.lower() not in b09_text.lower():
            scope_problems.append(problem(
                "CONTRACT_SCOPE_MISMATCH", "$.source.B-09",
                f"B-09 F-AL-006 no longer contains {needle!r}"))
    if "amendments" in read(MANIFEST) and json.loads(read(MANIFEST)).get("amendments") != []:
        scope_problems.append(problem(
            "CONTRACT_MANIFEST_INVALID", "$.manifest.amendments",
            "the production amendment manifest must remain empty"))
    if index.get("preserved_baseline", {}).get("active_formulas") != 295 or \
            index.get("preserved_baseline", {}).get("parameter_records") != 393 or \
            index.get("preserved_baseline", {}).get("b03_carry_ins") != 20:
        scope_problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", "$.index.preserved_baseline",
            "preserved baseline counts are not 295/393/20"))
    checks.append(_check("C-08", "Contract scope is isolated from B-09 and the numerical foundation is preserved", scope_problems))
    # C-09 offline/determinism declaration
    runtime_problems = []
    source = read(__file__)
    for banned in ("import socket", "import urllib", "import requests", "import random",
                   "from socket", "from urllib", "from requests"):
        if re.search(r"^\s*" + re.escape(banned), source, re.M):
            runtime_problems.append(problem(
                "CONTRACT_SCHEMA_INVALID", "$.runtime",
                f"forbidden runtime dependency: {banned}"))
    if index.get("validation", {}).get("offline") is not True:
        runtime_problems.append(problem(
            "CONTRACT_SCHEMA_INVALID", "$.index.validation.offline",
            "the registry must declare offline validation"))
    checks.append(_check("C-09", "Validation is deterministic, offline and standard-library only", runtime_problems))
    failed = [c for c in checks if not c["passed"]]
    return {
        "status": "PASS" if not failed else "FAIL",
        "checks": checks,
        "coverage": coverage_report,
        "evidence": evidence_stats,
        "regression": reg_results,
        "contracts": sorted(contracts),
        "report_sha256": sha256_bytes(canonical_json([{k: c[k] for k in ("id", "passed", "problems")} for c in checks])),
    }


def _report_payload(contracts, coverage, mappings):
    return {
        "contracts": sorted(contracts),
        "hashes": {c: contract_sha256(v) for c, v in sorted(contracts.items())},
        "coverage": {c: {"segments": v["segments"], "covered": v["covered"]}
                     for c, v in sorted(coverage.items())},
        "mappings": len(mappings.get("mappings", [])),
    }


# ---------------------------------------------------------------------------
# regression fixtures
# ---------------------------------------------------------------------------
def _fixture_decisions_text():
    base = read(DECISIONS)
    rows = []
    def add(did, contract, clause, category, status, body, reason, consequences):
        rows.append(f"| {did} | 2026-11-16 | TEST FIXTURE ONLY — {clause} contract validation | "
                    f"{body} | {status} | {reason} | docs/stage-2/10_economic_formula_and_balance_register.md | {consequences} |")
    add("D-940", "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.1.0; "
        "Alternatives: retain the baseline only; add the derived-calculation restatement; "
        "Consequences: the integer convention is restated for derived economic calculations. Reopening: reopen if D-064 changes.",
        "Evidence: governed evidence mapping EV-TEST-D064; Rationale: D-064 states that all economic arithmetic is integer.",
        "Consequences: the derived-calculation restatement is explicit. Reopening: reopen if D-064 changes.")
    add("D-941", "NC-F-EC-000f", "F-EC-000f", "C", "**Provisional** (Category C; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000f 1.0.0; Replacement contract: NC-F-EC-000f 1.1.0; "
        "Alternatives: leave the evidence state unstated; add a provisional evidence-state proposition; "
        "Consequences: the missing calibration evidence is now explicit. Reopening: reopen when calibrated evidence exists.",
        "Evidence: governed evidence mapping EV-TEST-CALIBRATION; Rationale: calibration evidence is not established. Missing evidence: calibrated integer-arithmetic review; Test: Prompt 14E calibration; Owner: Prompt 14.",
        "Consequences: the proposition stays provisional. Reopening: reopen when the named test completes.")
    add("D-942", "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.0.1; "
        "Alternatives: retain wording; add a derived-calculation clarification; Consequences: wording-only clarification. Reopening: reopen on any semantic change.",
        "Evidence: path=docs/stage-2/20_fair_play_and_player_protection.md; section=Fair-play; quote=\"Fair-play rules apply to all accounts\"; supports=\"integer arithmetic policy\"; stance=supports; Rationale: The fair-play document describes account rules.",
        "Consequences: a wording clarification is proposed. Reopening: reopen on any semantic change.")
    add("D-943", "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.0.1; Alternatives: retain prohibition; permit binary floating point; Consequences: representation changes. Reopening: reopen on any change.",
        "Evidence: governed evidence mapping EV-NC-F-EC-000b-P-003-01; Rationale: the fixture tests a prohibited permission.",
        "Consequences: the representation rule would change. Reopening: reopen on any change.")
    add("D-944", "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.0.1; Alternatives: retain prohibition; add a treasury exception; Consequences: an exception would apply. Reopening: reopen on any change.",
        "Evidence: governed evidence mapping EV-NC-F-EC-000b-P-003-01; Rationale: the fixture tests an unsupported exception.",
        "Consequences: an exception would apply. Reopening: reopen on any change.")
    for did, num in (("D-945", "1"), ("D-946", "2"), ("D-947", "3"),
                     ("D-948", "1"), ("D-949", "2"), ("D-950", "3"),
                     ("D-951", "1"), ("D-952", "2"), ("D-953", "3")):
        add(did, "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
            f"Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.0.{num}; Alternatives: retain baseline; adopt the proposed wording; Consequences: representation or accumulation change. Reopening: reopen on any change.",
            "Evidence: governed evidence mapping EV-NC-F-EC-000b-P-003-01; Rationale: mandatory negative fixture.",
            "Consequences: the proposed rule would change. Reopening: reopen on any change.")
    add("D-954", "NC-F-EC-000b", "F-EC-000b", "A", "**Owner-approved** (Category A; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.1.0; "
        "Alternatives: do not add the test proposition; add it under owner authorization; "
        "Consequences: a test-only owner-reserved proposition is added. Reopening: reopen if the owner withdraws the authorization. "
        "Owner authorization: OA-TEST-001 (TEST FIXTURE ONLY).",
        "Evidence: governed evidence mapping EV-TEST-OWNER-AUTH; Rationale: the fixture exercises the Category A path with a synthetic authorization source.",
        "Consequences: a test-only proposition is added. Reopening: reopen if the authorization is withdrawn.")
    add("D-957", "NC-F-EC-000b", "F-EC-000b", "B", "**Confirmed** (Category B; TEST FIXTURE)",
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.0.0 (wording-only clarification); "
        "Alternatives: retain the current wording; restate the prohibition without changing its proposition; "
        "Consequences: the clause wording changes and the typed proposition set is unchanged. Reopening: reopen on any semantic change.",
        "Evidence: path=docs/stage-2/22_formulas_and_balance.md; section=8.2; "
        "quote=\"No binary floating point; no fractional carry stated\"; "
        "supports=\"the register prohibits binary floating point\"; stance=supports; "
        "Rationale: B-14 section 8.2 records the register floating-point prohibition.",
        "Consequences: a wording-only clarification is accepted. Reopening: reopen on any semantic change.")
    return base + "\n" + "\n".join(rows) + "\n"


def _decision_row_text(did):
    for line in _fixture_decisions_text().splitlines():
        if line.startswith("| " + did + " |"):
            return line
    return ""


def _manifest_for(fid, prev_hash, new_hash, decision_id, category="B",
                  status="Confirmed", prev_version=None, new_version=None,
                  prev_sha=None, new_sha=None, **extra):
    entry = {
        "clause": fid,
        "source_document": "docs/stage-2/10_economic_formula_and_balance_register.md",
        "previous_hash": prev_hash,
        "new_hash": new_hash,
        "decision_id": decision_id,
        "category": category,
        "decision_status": status,
        "authorization_evidence": f"DECISIONS.md {decision_id} (TEST FIXTURE ONLY)",
        "rationale": "Fixture rationale: the test exercises the controlled amendment gate.",
        "regression_evidence": "14A_contract_validator fixture",
        "owner_reserved": category in ("A", "D"),
    }
    if prev_version:
        entry["previous_contract_version"] = prev_version
    if new_version:
        entry["new_contract_version"] = new_version
    if prev_sha:
        entry["previous_contract_sha256"] = prev_sha
    if new_sha:
        entry["new_contract_sha256"] = new_sha
    entry.update(extra)
    return {"baseline": {fid: {"hash": prev_hash}}, "amendments": [entry]}


def _candidate_proposal(fid, sentence, replace=None):
    base_clause = BASELINE_CLAUSES[fid]
    if replace:
        old, new = replace
        candidate_clause = base_clause.replace(old, new)
    else:
        candidate_clause = base_clause + " " + sentence
    document = replace_clause(read(B04), fid, candidate_clause)
    return document, candidate_clause


def _test_mapping(proposition_id, contract_id, excerpt="All economic arithmetic is integer",
                  classification="SUPPORTS", reviewed=True, review_status=None,
                  document_path="docs/DECISIONS.md", section="D-064"):
    review_status = review_status or ("REVIEWED" if reviewed else "NOT_REVIEWED")
    return {
        "evidence_id": "EV-TEST-" + proposition_id.split("/")[-1],
        "contract_id": contract_id,
        "proposition_id": proposition_id,
        "document_path": document_path,
        "section": section,
        "document_sha256": sha256_file(os.path.join(REPO, document_path)),
        "excerpt": excerpt,
        "classification": classification if reviewed else "NOT_REVIEWED",
        "proposed_classification": classification,
        "scope": {"systems": ["B-04"], "conditions": []},
        "review": {
            "review_status": review_status,
            "reviewed_by": "SYNTHETIC_TEST_FIXTURE" if reviewed else None,
            "reviewer_role": "TEST FIXTURE — NOT A HUMAN REVIEW" if reviewed else None,
            "reviewed_at": "2026-11-16" if reviewed else None,
            "review_rationale": ("Synthetic fixture used to exercise the reviewed-SUPPORTS path; "
                                 "this is not a claim of human review.") if reviewed else None,
        },
        "implementation_actor": "Prompt 14A contract implementation session (AI)",
        "reviewer_independence_required": True,
        "status": "ACTIVE",
    }


def _fixture_request(context, **fields):
    return FixtureRequest(fields, context)


def _fixture_ctx(mappings=None, owner_authorizations=None, decisions_text=None):
    return make_fixture_context(
        decisions_text=decisions_text if decisions_text is not None else _fixture_decisions_text(),
        mappings=mappings,
        owner_authorizations=owner_authorizations or [])


def build_typed_positive():
    base = get_trusted_context().contracts["F-EC-000b"]
    candidate = copy.deepcopy(base)
    candidate["contract_version"] = "1.1.0"
    candidate["effective_decision"] = "D-940"
    prop = {
        "id": "NC-F-EC-000b/P-007",
        "kind": "NUMERIC_DOMAIN",
        "subject": "DERIVED_CALCULATIONS",
        "predicate": "HAS_TYPE",
        "object": {"type": "NUMERIC_TYPE", "value": "INTEGER"},
        "modality": "MUST", "polarity": "AFFIRM",
        "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                  "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
        "conditions": [], "exceptions": [],
        "units": {"dimension": "DIMENSIONLESS", "unit": "NONE"},
        "timing": {"boundary": "TWO_HOUR_UTC", "phase": "ALL", "persistence": "WITHIN_TURN"},
        "numeric": {"representation": "INTEGER", "rounding": [],
                    "precision": "WHOLE_UNIT", "basis_point_relation": None},
        "authority": {"category": "B", "owner_reserved": False,
                      "classification_status": "RESOLVED",
                      "basis_decisions": ["D-045", "D-064"],
                      "basis_note": "D-064 states that all economic arithmetic is integer; derived calculations are economic arithmetic in the B-04 scope."},
        "source_anchor": {"document": "docs/stage-2/10_economic_formula_and_balance_register.md",
                          "section": "F-EC-000b", "excerpt": "All quantities are integers.",
                          "source_kind": "CLAUSE"},
        "status": "ACTIVE", "projection_visibility": "CLAUSE",
    }
    candidate["propositions"].append(prop)
    candidate["change_policy"]["propositions"]["NC-F-EC-000b/P-007"] = {
        "category": "B", "owner_reserved": False,
        "evidence_required_on_change": True, "baseline_unresolved": False,
        "exceptions_allowed": False,
    }
    candidate["rendering"]["fragments"].append({
        "proposition_id": "NC-F-EC-000b/P-007",
        "template": "Derived economic calculations are included in the integer-quantity rule."})
    rendered, _ = render_contract(candidate)
    document = replace_clause(read(B04), "F-EC-000b", rendered)
    mappings = copy.deepcopy(get_trusted_context().mappings)
    mappings["mappings"].append(_test_mapping("NC-F-EC-000b/P-007", "NC-F-EC-000b"))
    context = _fixture_ctx(mappings=mappings)
    return _fixture_request(
        context,
        amendment_id="TEST-TYPED-B",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=candidate,
        evidence_refs=["EV-TEST-P-007"],
        decision_ref="D-940",
        notes="Typed Category B positive fixture; test-only decision and synthetic review.")


def build_typed_unsupported_evidence():
    request = build_typed_positive()
    candidate = copy.deepcopy(request["candidate_contract"])
    candidate["effective_decision"] = "D-956"
    rendered, _ = render_contract(candidate)
    document = replace_clause(read(B04), "F-EC-000b", rendered)
    context = copy.copy(request.fixture_context)
    context.mappings = copy.deepcopy(get_trusted_context().mappings)
    context.decisions_text = _fixture_decisions_text() + "\n" + (
        "| D-956 | 2026-11-16 | TEST FIXTURE ONLY — evidence-gate independence | "
        "Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.1.0; "
        "Alternatives: retain the baseline only; add the derived-calculation restatement; "
        "Consequences: a derived-calculation restatement is proposed; Reopening: reopen if D-064 changes. | "
        "**Confirmed** (Category B; TEST FIXTURE) | "
        "Evidence: governed evidence mapping EV-TEST-D064; Rationale: the fixture isolates an evidence failure while authority remains valid. | "
        "docs/stage-2/10_economic_formula_and_balance_register.md | "
        "Consequences: the restatement is explicit; Reopening: reopen if D-064 changes. |") + "\n"
    return _fixture_request(
        context,
        amendment_id="TEST-UNSUPPORTED-EVIDENCE",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=candidate,
        evidence_refs=[],
        decision_ref="D-956",
        notes="Authority valid; evidence must fail independently.")


def build_missing_authority():
    request = build_typed_positive()
    candidate = copy.deepcopy(request["candidate_contract"])
    candidate["effective_decision"] = "D-955"
    rendered, _ = render_contract(candidate)
    document = replace_clause(read(B04), "F-EC-000b", rendered)
    context = copy.copy(request.fixture_context)
    context.decisions_text = _fixture_decisions_text()
    return _fixture_request(
        context,
        amendment_id="TEST-MISSING-AUTHORITY",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=candidate,
        evidence_refs=["EV-TEST-P-007"],
        decision_ref="D-955",
        notes="Evidence valid; authority must fail independently.")


def build_wording_positive():
    candidate_clause = BASELINE_CLAUSES["F-EC-000b"].replace(
        "No formula uses binary floating point.",
        "The binary floating-point prohibition applies to every formula calculation.")
    document = replace_clause(read(B04), "F-EC-000b", candidate_clause)
    context = _fixture_ctx()
    return _fixture_request(
        context,
        amendment_id="TEST-WORDING",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=None,
        evidence_refs=[],
        decision_ref="D-957",
        notes="Wording-only clarification with an unchanged typed proposition set.")


def build_typed_provisional():
    base = get_trusted_context().contracts["F-EC-000f"]
    candidate = copy.deepcopy(base)
    candidate["contract_version"] = "1.1.0"
    candidate["lifecycle_status"] = "ADOPTED_PROVISIONAL"
    candidate["effective_decision"] = "D-941"
    prop = {
        "id": "NC-F-EC-000f/P-006",
        "kind": "CONSTANT_CLASSIFICATION",
        "subject": "CONSTANT_SET",
        "predicate": "HAS_EVIDENCE_STATE",
        "object": {"type": "CALIBRATION_EVIDENCE", "value": "NOT_ESTABLISHED"},
        "modality": "NOT_ESTABLISHED", "polarity": "NEUTRAL",
        "scope": {"systems": ["B-04"], "domain": "CONSTANT_VERSIONING",
                  "persistence": "NONE", "inheritance": "NONE", "distinct_from": []},
        "conditions": [], "exceptions": [],
        "units": {"dimension": "DIMENSIONLESS", "unit": "NONE"},
        "timing": {"boundary": "NONE", "phase": "ALL", "persistence": "NONE"},
        "numeric": {"representation": "NONE", "rounding": [],
                    "precision": "NONE", "basis_point_relation": None},
        "authority": {"category": "C", "owner_reserved": False,
                      "classification_status": "PROVISIONAL",
                      "basis_decisions": ["D-014"],
                      "basis_note": "The calibration-evidence state is provisional and names its missing evidence and confirming test; it changes no numerical value."},
        "source_anchor": {"document": "docs/stage-2/10_economic_formula_and_balance_register.md",
                          "section": "F-EC-000f",
                          "excerpt": "The constants below are the v1.0 provisional calibration",
                          "source_kind": "CLAUSE"},
        "status": "ACTIVE", "projection_visibility": "CLAUSE",
    }
    candidate["propositions"].append(prop)
    candidate["change_policy"]["propositions"]["NC-F-EC-000f/P-006"] = {
        "category": "C", "owner_reserved": False,
        "evidence_required_on_change": True, "baseline_unresolved": True,
        "exceptions_allowed": False,
    }
    candidate["rendering"]["fragments"].append({
        "proposition_id": "NC-F-EC-000f/P-006",
        "template": "No calibration-evidence state is established for these provisional constants."})
    rendered, _ = render_contract(candidate)
    document = replace_clause(read(B04), "F-EC-000f", rendered)
    mappings = copy.deepcopy(get_trusted_context().mappings)
    mappings["mappings"].append(_test_mapping(
        "NC-F-EC-000f/P-006", "NC-F-EC-000f",
        excerpt="The constants are the v1.0 provisional calibration",
        classification="NOT_ESTABLISHED", reviewed=False,
        document_path="docs/stage-2/10_economic_formula_and_balance_register.md",
        section="F-EC-044"))
    context = _fixture_ctx(mappings=mappings)
    return _fixture_request(
        context,
        amendment_id="TEST-TYPED-C",
        target_contract="NC-F-EC-000f",
        candidate_document=document,
        candidate_contract=candidate,
        evidence_refs=["EV-TEST-P-006"],
        decision_ref="D-941",
        notes="Category C provisional positive fixture; remains ADOPTED_PROVISIONAL.")


def build_owner_authorized():
    base = get_trusted_context().contracts["F-EC-000b"]
    candidate = copy.deepcopy(base)
    candidate["contract_version"] = "1.1.0"
    candidate["effective_decision"] = "D-954"
    prop = {
        "id": "NC-F-EC-000b/P-007",
        "kind": "NUMERIC_DOMAIN",
        "subject": "CATEGORY_A_TEST_PROPOSITION",
        "predicate": "HAS_TYPE",
        "object": {"type": "NUMERIC_TYPE", "value": "INTEGER"},
        "modality": "MUST", "polarity": "AFFIRM",
        "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                  "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
        "conditions": [], "exceptions": [],
        "units": {"dimension": "DIMENSIONLESS", "unit": "NONE"},
        "timing": {"boundary": "TWO_HOUR_UTC", "phase": "ALL", "persistence": "WITHIN_TURN"},
        "numeric": {"representation": "INTEGER", "rounding": [],
                    "precision": "WHOLE_UNIT", "basis_point_relation": None},
        "authority": {"category": "A", "owner_reserved": True,
                      "classification_status": "OWNER_RESERVED",
                      "basis_decisions": ["D-014"],
                      "basis_note": "Test-only owner-reserved proposition used to prove that a Category A change requires an authentic, traceable owner authorization."},
        "source_anchor": {"document": "docs/stage-2/10_economic_formula_and_balance_register.md",
                          "section": "F-EC-000b", "excerpt": "All quantities are integers.",
                          "source_kind": "CLAUSE"},
        "status": "ACTIVE", "projection_visibility": "CLAUSE",
    }
    candidate["propositions"].append(prop)
    candidate["change_policy"]["propositions"]["NC-F-EC-000b/P-007"] = {
        "category": "A", "owner_reserved": True,
        "evidence_required_on_change": True, "baseline_unresolved": False,
        "exceptions_allowed": False,
    }
    candidate["rendering"]["fragments"].append({
        "proposition_id": "NC-F-EC-000b/P-007",
        "template": "The test-only owner-reserved proposition applies to integer arithmetic."})
    rendered, _ = render_contract(candidate)
    document = replace_clause(read(B04), "F-EC-000b", rendered)
    mappings = copy.deepcopy(get_trusted_context().mappings)
    mappings["mappings"].append(_test_mapping(
        "NC-F-EC-000b/P-007", "NC-F-EC-000b",
        excerpt="Every resource is a whole unit and every crown is a whole crown",
        classification="SUPPORTS", reviewed=True,
        document_path="docs/DECISIONS.md", section="D-045"))
    auth_path = os.path.join(FIXTURES, "owner_authorization_TEST_FIXTURE.md")
    authorization = {
        "authorization_id": "OA-TEST-001",
        "decision_id": "D-954",
        "instruction_source": "qa_backups/14A_contract_fixtures/owner_authorization_TEST_FIXTURE.md",
        "instruction_sha256": sha256_file(auth_path),
        "quoted_instruction": "Owner authorization (TEST FIXTURE ONLY): authorize the test-only proposition NC-F-EC-000b/P-007 for validator regression testing.",
        "authorized_at": "2026-11-16",
        "scope": {"systems": ["B-04"], "propositions": ["NC-F-EC-000b/P-007"]},
        "status": "ACTIVE",
        "provenance": "OWNER_INSTRUCTION_DOCUMENT",
        "fixture_only": True,
    }
    context = _fixture_ctx(mappings=mappings, owner_authorizations=[authorization])
    return _fixture_request(
        context,
        amendment_id="TEST-OWNER-A",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=candidate,
        evidence_refs=["EV-TEST-P-007"],
        decision_ref="D-954",
        notes="Category A test-only positive fixture; fixture context only.")


def build_b09_within_turn():
    artifacts = load_artifacts()
    b09_text = read(B09)
    block = section_block(b09_text, "F-AL-006")
    contract = {
        "schema_version": "1.0.0",
        "contract_id": "NC-F-AL-006",
        "clause_id": "F-AL-006",
        "title": "Automatic Per-Turn Production Tax Arithmetic",
        "source_document": "docs/stage-2/16_alliances_formula_register.md",
        "source_version": "B-09 alliance formula register",
        "baseline_source_hash": source_clause_sha256(block),
        "contract_version": "1.0.0",
        "lifecycle_status": "ADOPTED",
        "numerical_status": "PROVISIONAL VALUE",
        "numerical_status_display": "Provisional",
        "effective_decision": "D-140",
        "scope": {
            "systems": ["B-09"], "domain": "FORMULA_ARITHMETIC",
            "turn_phases": ["P3"], "persistence": "WITHIN_TURN",
            "inheritance": "EXPLICIT_PER_PROPOSITION",
            "excluded_systems": [], "excluded_concepts": ["CROSS_TURN_REMAINDER_PERSISTENCE"],
            "scope_authority": ["D-140"],
        },
        "propositions": [{
            "id": "NC-F-AL-006/P-001",
            "kind": "FRACTIONAL_ACCUMULATION",
            "subject": "WITHIN_TURN_CUMULATIVE_ACCRUAL",
            "predicate": "PERSISTS_WITHIN_TURN",
            "object": {"type": "ACCUMULATION_SCOPE", "value": "WITHIN_TURN"},
            "modality": "MUST", "polarity": "AFFIRM",
            "scope": {"systems": ["B-09"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE",
                      "distinct_from": ["CROSS_TURN_REMAINDER_PERSISTENCE"]},
            "conditions": [], "exceptions": [],
            "units": {"dimension": "DIMENSIONLESS", "unit": "NONE"},
            "timing": {"boundary": "TWO_HOUR_UTC", "phase": "P3", "persistence": "WITHIN_TURN"},
            "numeric": {"representation": "INTEGER", "rounding": ["FLOOR"],
                        "precision": "WHOLE_UNIT", "basis_point_relation": None},
            "authority": {"category": "B", "owner_reserved": False,
                          "classification_status": "RESOLVED",
                          "basis_decisions": ["D-140"],
                          "basis_note": "D-140 authorizes the F-AL-006 arithmetic model; every rate, bracket and assignment remains player-supplied."},
            "source_anchor": {"document": "docs/stage-2/16_alliances_formula_register.md",
                              "section": "F-AL-006",
                              "excerpt": "Different assets keep separate accumulators",
                              "source_kind": "BASELINE_EVIDENCE"},
            "status": "ACTIVE",
            "projection_visibility": "DERIVED_FROM_BASELINE_EVIDENCE",
        }],
        "change_policy": {
            "default_category": "B",
            "propositions": {
                "NC-F-AL-006/P-001": {
                    "category": "B", "owner_reserved": False,
                    "evidence_required_on_change": True, "baseline_unresolved": False,
                    "exceptions_allowed": False,
                }
            },
        },
        "rendering": {
            "template_id": "B04-F-AL-006",
            "version": "1.0.0",
            "template_path": "projections/F-AL-006.md.tpl",
            "fragment_separator": " ",
            "structural_prefix": "**F-AL-006 — Automatic Per-Turn Production Tax Arithmetic.** *{{numerical_status_display}}.*",
            "fragments": [],
        },
    }
    schema_problems = validate_schema(contract, {"$ref": "#/$defs/contract"},
                                      artifacts["schema"], "$.b09")
    semantic_problems = validate_contract_semantics(
        contract, artifacts["schema"], artifacts["lexicon"],
        _fixture_decisions_text(), None, mode="test")
    return contract, schema_problems + semantic_problems


def build_negative(kind, variant=0):
    base = get_trusted_context().contracts["F-EC-000b"]
    texts = {
        "D-998": [
            "including derived calculations",
            "including derived calculations and related calculations",
            "including derived and downstream calculations",
        ],
        "D-999": [
            "Binary floating point calculations are permitted.",
            "Formula calculations may use binary-floating-point representation.",
            "Binary floating point is not prohibited.",
        ],
        "D-990": [
            "An exception applies only when numeric calculations use an alternative representation within the treasury carry subsystem, subject to separate fractional ledger handling; the subsystem may use IEEE-754 binary representation.",
            "An exception applies for IEEE-754 representation.",
            "Only when the treasury subsystem calculates may it use an alternative representation.",
        ],
        "D-991": [
            "A radix-two encoding with a separate exponent and significand is permitted.",
            "Numeric values may be stored in a base-2 form with exponent and significand parts.",
            "Calculations may use a two-part power-and-coefficient number layout.",
        ],
        "D-992": [
            "Numeric values may be stored as sign, exponent and mantissa fields.",
            "A value may be split into mantissa, exponent and sign components.",
            "Storage may use a three-field sign-mantissa-exponent tuple.",
        ],
        "D-993": [
            "Residual sub-unit amounts between turns are preserved.",
            "Sub-unit remainders carry across turns.",
            "A leftover fraction from one turn is retained into the next turn.",
        ],
    }
    decision_map = {
        "D-998": "D-942", "D-999": "D-943", "D-990": "D-944",
        "D-991": ["D-945", "D-946", "D-947"],
        "D-992": ["D-948", "D-949", "D-950"],
        "D-993": ["D-951", "D-952", "D-953"],
    }
    sentence = texts[kind][variant]
    if kind == "D-998":
        document, clause = _candidate_proposal(
            "F-EC-000b", "",
            replace=("No formula uses binary floating point.",
                     "No formula uses binary floating point, " + sentence + "."))
    elif kind == "D-999":
        document, clause = _candidate_proposal(
            "F-EC-000b", "",
            replace=("No formula uses binary floating point.", sentence))
    else:
        document, clause = _candidate_proposal("F-EC-000b", sentence)
    did = decision_map[kind]
    if isinstance(did, list):
        did = did[variant]
    context = _fixture_ctx()
    return _fixture_request(
        context,
        amendment_id=f"TEST-{kind}-V{variant}",
        target_contract="NC-F-EC-000b",
        candidate_document=document,
        candidate_contract=None,
        evidence_refs=[],
        decision_ref=did,
        notes=f"Mandatory negative fixture {kind} variant {variant}.")


def _all_report_codes(report):
    codes = set()
    for gate in ("request_gate", "contract_gate", "evidence_gate",
                 "authority_gate", "comparison_gate"):
        codes.update(p["code"] for p in report.get(gate, {}).get("problems", []))
    return codes


def regression_matrix():
    """Return (problems, results) for the mandatory gate and C2 matrix."""
    results = []
    problems = []
    cases = [
        ("D-998", 0, {"CONTRACT_EVIDENCE_PROPOSITION_MISMATCH"}),
        ("D-999", 0, {"CONTRACT_PROPOSITION_CONFLICT"}),
        ("D-990", 0, {"CONTRACT_EXCEPTION_UNSUPPORTED"}),
        ("D-991", 0, {"CONTRACT_PROPOSITION_CONFLICT", "CONTRACT_UNMAPPED_TERM"}),
        ("D-992", 0, {"CONTRACT_PROPOSITION_CONFLICT", "CONTRACT_UNMAPPED_TERM"}),
        ("D-993", 0, {"CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                       "CONTRACT_EVIDENCE_NOT_REVIEWED", "CONTRACT_EVIDENCE_MAPPING_MISSING"}),
    ]
    for kind, variant, expected in cases:
        report = validate_amendment(build_negative(kind, variant))
        codes = _all_report_codes(report)
        ok = not report["accepted"] and bool(codes & expected)
        results.append({"case": kind, "variant": variant, "accepted": report["accepted"],
                        "codes": sorted(codes), "passed": ok})
        if not ok:
            problems.append(problem(
                "CONTRACT_PROPOSITION_CONFLICT", f"$.regression.{kind}",
                f"mandatory negative case did not reject with the required semantic code; codes={sorted(codes)}"))
    positive = build_typed_positive()
    report = validate_amendment(positive)
    codes = _all_report_codes(report)
    results.append({"case": "positive-typed-B", "accepted": report["accepted"],
                    "codes": sorted(codes), "passed": report["accepted"]})
    if not report["accepted"]:
        problems.append(problem(
            "CONTRACT_EVIDENCE_NOT_REVIEWED", "$.regression.positive-typed-B",
            "the typed Category B positive fixture did not pass: " +
            "; ".join(fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate", "comparison_gate")
                      for p in report.get(gate, {}).get("problems", []))))
    for label, builder in (("positive-wording", build_wording_positive),
                           ("positive-typed-C", build_typed_provisional),
                           ("positive-owner-A", build_owner_authorized)):
        report = validate_amendment(builder())
        results.append({"case": label, "accepted": report["accepted"],
                        "codes": sorted(_all_report_codes(report)),
                        "passed": report["accepted"]})
        if not report["accepted"]:
            problems.append(problem(
                "CONTRACT_EVIDENCE_NOT_REVIEWED", f"$.regression.{label}",
                f"{label} did not pass: " +
                "; ".join(fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate", "comparison_gate")
                          for p in report.get(gate, {}).get("problems", []))))
    unsupported = validate_amendment(build_typed_unsupported_evidence())
    results.append({"case": "independence-authority-pass-evidence-fail",
                    "accepted": unsupported["accepted"],
                    "evidence_passed": unsupported["evidence_gate"]["passed"],
                    "authority_passed": unsupported["authority_gate"]["passed"],
                    "passed": (not unsupported["accepted"] and
                               not unsupported["evidence_gate"]["passed"] and
                               unsupported["authority_gate"]["passed"])})
    if not results[-1]["passed"]:
        problems.append(problem(
            "CONTRACT_EVIDENCE_NOT_REVIEWED", "$.regression.independence-1",
            "the evidence gate did not fail independently while authority passed"))
    missing = validate_amendment(build_missing_authority())
    results.append({"case": "independence-evidence-pass-authority-fail",
                    "accepted": missing["accepted"],
                    "evidence_passed": missing["evidence_gate"]["passed"],
                    "authority_passed": missing["authority_gate"]["passed"],
                    "passed": (not missing["accepted"] and
                               missing["evidence_gate"]["passed"] and
                               not missing["authority_gate"]["passed"])})
    if not results[-1]["passed"]:
        problems.append(problem(
            "CONTRACT_AUTHORITY_MISMATCH", "$.regression.independence-2",
            "the authority gate did not fail independently while evidence passed"))
    # C2 trusted-input override attacks: plain dictionaries, production entry point.
    base_request = dict(build_negative("D-998", 0))
    override_attacks = {
        "override-baseline": {"base_contract": {}},
        "override-schema": {"schema": {}},
        "override-lexicon": {"lexicon": {}},
        "override-evidence": {"evidence_mappings": {"mappings": []}},
        "override-decisions": {"decisions_text": "| D-940 | fabricated |"},
        "override-owner": {"owner_authorizations": []},
        "override-template": {"candidate_template_text": "literal"},
        "override-manifest": {"manifest": {"amendments": []}},
    }
    for label, extra in override_attacks.items():
        attack = dict(base_request)
        attack.update(extra)
        attack_report = validate_amendment(attack)
        codes = _all_report_codes(attack_report)
        ok = (not attack_report["accepted"] and
              "CONTRACT_TRUSTED_INPUT_OVERRIDE" in codes)
        results.append({"case": label, "accepted": attack_report["accepted"],
                        "codes": sorted(codes), "passed": ok})
        if not ok:
            problems.append(problem(
                "CONTRACT_TRUSTED_INPUT_OVERRIDE", f"$.regression.{label}",
                f"trusted-input override attack was not rejected with the trusted-input code; codes={sorted(codes)}"))
    # C2 projection insertion attack: valid typed contract, contradictory inserted text.
    insertion_request = build_typed_positive()
    inserted = ("B-04 binary floating-point calculations are permitted.")
    clause = extract_clause(insertion_request["candidate_document"], "F-EC-000b")
    insertion_request["candidate_document"] = replace_clause(
        read(B04), "F-EC-000b", clause + " " + inserted)
    insertion_report = validate_amendment(insertion_request)
    codes = _all_report_codes(insertion_report)
    ok = (not insertion_report["accepted"] and bool(
        codes & {"CONTRACT_PROJECTION_MISMATCH", "CONTRACT_COVERAGE_GAP",
                 "CONTRACT_PROPOSITION_CONFLICT"}))
    results.append({"case": "projection-insertion", "accepted": insertion_report["accepted"],
                    "codes": sorted(codes), "passed": ok})
    if not ok:
        problems.append(problem(
            "CONTRACT_COVERAGE_GAP", "$.regression.projection-insertion",
            f"inserted contradictory projection text was not rejected; codes={sorted(codes)}"))
    return problems, results


# ---------------------------------------------------------------------------
# sealing
# ---------------------------------------------------------------------------
def seal_registry(contracts_dir=CONTRACTS, b04_path=B04, b14_path=B14,
                  policy_path=POLICY, decisions_path=DECISIONS):
    artifacts = load_artifacts(contracts_dir)
    index = artifacts["index"]
    mappings = artifacts["mappings"]
    # refresh only unreviewed draft evidence hashes; reviewed evidence is never silently re-based
    for mapping in mappings.get("mappings", []):
        if mapping.get("review", {}).get("review_status") == "REVIEWED":
            continue
        path = os.path.join(REPO, mapping.get("document_path", ""))
        mapping["document_sha256"] = sha256_file(path)
    write_json(os.path.join(contracts_dir, "evidence_mappings.json"), mappings)
    index["schema"]["sha256"] = sha256_file(os.path.join(contracts_dir, "schema.json"))
    index["lexicon"]["sha256"] = sha256_file(os.path.join(contracts_dir, "lexicon.json"))
    index["evidence_mappings"]["sha256"] = sha256_file(os.path.join(contracts_dir, "evidence_mappings.json"))
    source_hashes = {
        "docs/stage-2/10_economic_formula_and_balance_register.md": sha256_file(b04_path),
        "docs/stage-2/22_formulas_and_balance.md": sha256_file(b14_path),
        "docs/DECISIONS.md": sha256_file(decisions_path),
        "docs/AUTONOMOUS_DECISION_POLICY.md": sha256_file(policy_path),
    }
    for entry in index.get("source_documents", []):
        if entry.get("path") in source_hashes:
            entry["sha256"] = source_hashes[entry["path"]]
    index["preserved_baseline"]["d014_policy_sha256"] = sha256_file(policy_path)
    for ref in index.get("contracts", []):
        contract = artifacts["contracts"].get(ref["clause_id"])
        if not contract:
            continue
        rendered, _ = render_contract(contract)
        ref["contract_sha256"] = contract_sha256(contract)
        ref["projection_sha256"] = projection_sha256(rendered)
        cov = material_coverage(contract, extract_clause(read(b04_path), ref["clause_id"]))
        ref["material_coverage"] = {"segments": cov["segments"],
                                    "covered": cov["covered"], "ratio": cov["ratio"]}
    write_json(os.path.join(contracts_dir, "index.json"), index)
    return {"sealed": True, "contracts": sorted(artifacts["contracts"]),
            "evidence_mappings": len(mappings.get("mappings", []))}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def print_report(report):
    print("=" * 78)
    print("14A CONTROLLED NUMERICAL-CONTRACT VALIDATOR — documentation QA only")
    print("=" * 78)
    for check in report["checks"]:
        print(f"[{'PASS' if check['passed'] else 'FAIL'}] {check['id']} {check['description']}")
        for p in check["problems"][:10]:
            print("      - " + fmt(p))
        if len(check["problems"]) > 10:
            print(f"      - … {len(check['problems']) - 10} more")
    print("-" * 78)
    print(f"CHECKS: {len(report['checks'])}  FAILED: {sum(1 for c in report['checks'] if not c['passed'])}")
    print(f"EVIDENCE MAPPINGS: {report['evidence']['mappings']}  REVIEWED: {report['evidence']['reviewed']}  "
          f"NOT_REVIEWED: {report['evidence']['not_reviewed']}  REVIEWED_SUPPORTS: {report['evidence']['supports']}")
    print("RESULT:", "PASS — documentary consistency only." if report["status"] == "PASS" else "FAIL")
    print("NOT PROVEN: human semantic judgment, gameplay, balance, simulation, runtime or owner acceptance.")
    print("REPORT SHA-256:", report["report_sha256"])
    return 0 if report["status"] == "PASS" else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--seal" in argv:
        result = seal_registry()
        print(json.dumps(result, indent=2))
        return 0
    if "--self-test" in argv:
        problems, results = regression_matrix()
        print(json.dumps({"problems": [fmt(p) for p in problems], "results": results}, indent=2))
        return 0 if not problems else 1
    report = validate_production()
    if "--json" in argv:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_report(report)
    if "--write-report" in argv:
        target = argv[argv.index("--write-report") + 1]
        write_json(target, report)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
