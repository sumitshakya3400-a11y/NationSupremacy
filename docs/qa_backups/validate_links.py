#!/usr/bin/env python3
"""Project-wide Markdown link validator for the documentation corpus.

Scans every ``*.md`` file under the documentation root, resolves each local
link against the containing file, checks that the target exists and (where the
target is Markdown) that a ``#fragment`` matches a heading or explicit anchor.

Usage:
    python validate_links.py [--root docs] [--verbose]
    python validate_links.py --self-test

Exit code is 0 only when every local link resolves. External URLs
(``http``/``https``/``mailto`` and similar schemes) are skipped and counted.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

SKIP_SCHEMES = ("http:", "https:", "mailto:", "tel:", "ftp:", "ftps:", "data:", "javascript:")

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)*\1")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SETEXT_RE = re.compile(r"^(=+|-+)\s*$")
HTML_ANCHOR_RE = re.compile(r"""<[^>]*\b(?:id|name)\s*=\s*["']([^"']+)["'][^>]*>""")
REF_DEF_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(\S+)")
TITLE_TAIL_RE = re.compile(r"\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\))\s*$")


@dataclass
class Issue:
    file: Path
    line: int
    target: str
    reason: str


@dataclass
class Stats:
    files: int = 0
    links: int = 0
    local: int = 0
    external: int = 0
    anchors: int = 0
    issues: list[Issue] | None = None


def strip_inline_code(line: str) -> str:
    """Blank out inline code spans while preserving character positions."""
    return INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), line)


def logical_lines(text: str):
    """Yield (line_number, line) with fenced code blanked out."""
    in_fence = False
    fence_char = ""
    for number, raw in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(raw)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                yield number, ""
                continue
            if marker[0] == fence_char and len(marker) >= 3:
                in_fence = False
                yield number, ""
                continue
        if in_fence:
            yield number, ""
        else:
            yield number, strip_inline_code(raw)


def iter_inline_links(line: str):
    """Yield (column, target) for inline links/images with balanced parentheses."""
    length = len(line)
    index = 0
    while index < length:
        close_bracket = line.find("](", index)
        if close_bracket < 0:
            return
        open_bracket = line.rfind("[", 0, close_bracket)
        if open_bracket < 0:
            index = close_bracket + 2
            continue
        depth = 1
        position = close_bracket + 2
        while position < length and depth:
            if line[position] == "(":
                depth += 1
            elif line[position] == ")":
                depth -= 1
            position += 1
        if depth:
            return
        inner = line[close_bracket + 2 : position - 1].strip()
        target = split_target(inner)
        if target is not None:
            yield open_bracket, target
        index = position


def split_target(inner: str) -> str | None:
    inner = inner.strip()
    if not inner:
        return None
    if inner.startswith("<"):
        end = inner.find(">")
        return inner[1:end] if end > 0 else None
    inner = TITLE_TAIL_RE.sub("", inner).strip()
    if not inner:
        return None
    return inner.split()[0]


def slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -_")
    return text.replace(" ", "-")


def collect_anchors(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return set()
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    previous = ""
    for _, line in logical_lines(text):
        match = HEADING_RE.match(line)
        if match:
            slug = slugify_heading(match.group(2))
            count = seen.get(slug, 0)
            anchors.add(slug if count == 0 else f"{slug}-{count}")
            seen[slug] = count + 1
            previous = ""
            continue
        if SETEXT_RE.match(line) and previous.strip():
            slug = slugify_heading(previous)
            count = seen.get(slug, 0)
            anchors.add(slug if count == 0 else f"{slug}-{count}")
            seen[slug] = count + 1
            previous = ""
            continue
        for found in HTML_ANCHOR_RE.finditer(line):
            anchors.add(found.group(1))
        previous = line
    return anchors


def is_external(target: str) -> bool:
    lowered = target.strip().lower()
    return lowered.startswith(SKIP_SCHEMES) or lowered.startswith("//")


def resolve_target(root: Path, boundary: Path, source: Path, target: str):
    """Return (resolved_path, fragment) or raise ValueError with a reason."""
    path_part, _, fragment = target.partition("#")
    path_part = path_part.partition("?")[0]
    if "\\" in path_part:
        raise ValueError("malformed relative path (backslash separator)")
    path_part = unquote(path_part)
    fragment = unquote(fragment)
    if not path_part:
        return source, fragment
    if path_part.startswith("/"):
        candidate = (root / path_part.lstrip("/")).resolve()
    else:
        candidate = (source.parent / path_part).resolve()
    try:
        candidate.relative_to(boundary)
    except ValueError:
        raise ValueError("malformed relative path (escapes repository root)") from None
    return candidate, fragment


def scan(root: Path, verbose: bool = False) -> Stats:
    root = root.resolve()
    boundary = root.parent
    stats = Stats(issues=[])
    for markdown in sorted(root.rglob("*.md")):
        stats.files += 1
        try:
            text = markdown.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            stats.issues.append(Issue(markdown, 0, str(markdown), f"unreadable: {error}"))
            continue
        for number, line in logical_lines(text):
            entries = [(column, target) for column, target in iter_inline_links(line)]
            definition = REF_DEF_RE.match(line)
            if definition:
                entries.append((definition.start(2), definition.group(2)))
            for _, target in entries:
                stats.links += 1
                if not target or target.startswith("#"):
                    if target.startswith("#") and len(target) > 1:
                        stats.local += 1
                        stats.anchors += 1
                        anchors = collect_anchors(markdown)
                        if target[1:] not in anchors:
                            stats.issues.append(
                                Issue(markdown, number, target, "missing anchor")
                            )
                    continue
                if is_external(target):
                    stats.external += 1
                    continue
                stats.local += 1
                try:
                    candidate, fragment = resolve_target(root, boundary, markdown, target)
                except ValueError as error:
                    stats.issues.append(Issue(markdown, number, target, str(error)))
                    continue
                display = candidate.relative_to(boundary).as_posix()
                if not candidate.exists():
                    stats.issues.append(Issue(markdown, number, target, f"missing target: {display}"))
                    continue
                if candidate.is_dir():
                    continue
                if fragment:
                    if candidate.suffix.lower() != ".md":
                        continue
                    stats.anchors += 1
                    if fragment not in collect_anchors(candidate):
                        stats.issues.append(
                            Issue(markdown, number, target, f"missing anchor in {display}")
                        )
        if verbose:
            print(f"scanned {markdown.relative_to(boundary).as_posix()}")
    return stats


def report(stats: Stats, boundary: Path) -> int:
    for issue in stats.issues:
        try:
            name = issue.file.resolve().relative_to(boundary).as_posix()
        except ValueError:
            name = str(issue.file)
        print(f"{name}:{issue.line}: {issue.target} ({issue.reason})")
    print()
    print(f"Markdown files scanned: {stats.files}")
    print(f"Links found: {stats.links}")
    print(f"Links checked locally: {stats.local}")
    print(f"External links skipped: {stats.external}")
    print(f"Anchors checked: {stats.anchors}")
    print(f"Unresolved: {len(stats.issues)}")
    return 1 if stats.issues else 0


def run_self_test() -> int:
    base = Path(tempfile.mkdtemp(prefix="link-validator-"))
    try:
        repo = base / "repo"
        docs = repo / "docs"
        nested = docs / "sub"
        nested.mkdir(parents=True)
        (repo / "outside.md").write_text("# Parent target\n", encoding="utf-8")
        (docs / "same.md").write_text("## Section one\n", encoding="utf-8")
        (docs / "with space.md").write_text("# Spaced\n", encoding="utf-8")
        (docs / "tool.py").write_text("print('ok')\n", encoding="utf-8")
        (nested / "deep.md").write_text("# Deep\n", encoding="utf-8")
        index = docs / "index.md"
        index.write_text(
            "\n".join(
                [
                    "[same](same.md)",
                    "[parent](../outside.md)",
                    "[nested](sub/deep.md)",
                    "[broken](missing.md)",
                    "[anchor](same.md#section-one)",
                    "[bad anchor](same.md#not-a-heading)",
                    "[space](with%20space.md)",
                    "[external](https://example.com/page)",
                    "[script](tool.py)",
                    "[directory](sub/)",
                    "[escape](../../../../escape.md)",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        stats = scan(docs)
        issues = stats.issues or []
        checks: list[tuple[str, bool]] = []
        checks.append(("valid same-directory link", not any(i.target == "same.md" for i in issues)))
        checks.append(("valid parent link", not any(i.target == "../outside.md" for i in issues)))
        checks.append(("valid nested link", not any(i.target == "sub/deep.md" for i in issues)))
        checks.append((
            "broken target detected",
            any(i.target == "missing.md" and i.reason.startswith("missing target") for i in issues),
        ))
        checks.append((
            "broken anchor detected",
            any(i.target == "same.md#not-a-heading" and i.reason.startswith("missing anchor") for i in issues),
        ))
        checks.append(("URL-encoded spaces accepted", not any("%20" in i.target for i in issues)))
        checks.append(("external URL skipped", stats.external == 1))
        checks.append(("existing script accepted", not any(i.target == "tool.py" for i in issues)))
        checks.append(("directory link permitted", not any(i.target == "sub/" for i in issues)))
        checks.append((
            "malformed relative path detected",
            any("malformed relative path" in i.reason for i in issues),
        ))
        checks.append(("exactly three fixtures fail", len(issues) == 3))
        failed = 0
        for label, passed in checks:
            print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
            failed += 0 if passed else 1
        print(f"Link-validator self-test: {len(checks) - failed}/{len(checks)} checks passed")
        if issues:
            print(f"  detected issues: {[(i.target, i.reason) for i in issues]}")
        return 1 if failed else 0
    finally:
        shutil.rmtree(base, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return run_self_test()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: root is not a directory: {root}", file=sys.stderr)
        return 2
    stats = scan(root, verbose=args.verbose)
    return report(stats, root.parent)


if __name__ == "__main__":
    sys.exit(main())
