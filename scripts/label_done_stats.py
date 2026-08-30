#!/usr/bin/env python3
"""Report % of Done tasks per label, and per label combined with frontend/backend.

Usage: python3 scripts/label_done_stats.py [workitems_dir]
"""
import sys
import re
from pathlib import Path
from collections import defaultdict

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def parse_labels(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    if not raw:
        return []
    return [label.strip() for label in raw.split(",") if label.strip()]


def main() -> None:
    workitems_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("PET/workitems")
    files = sorted(workitems_dir.glob("*.md"))

    # label -> [total, done]
    stats: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    pair_stats: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0])

    for path in files:
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
        state = fields.get("state", "")
        labels = parse_labels(fields.get("labels", ""))
        is_done = state == "Done"

        has_frontend = "frontend" in labels
        has_backend = "backend" in labels

        for label in labels:
            if label in ("frontend", "backend"):
                continue
            stats[label][0] += 1
            if is_done:
                stats[label][1] += 1

            if has_frontend:
                key = (label, "frontend")
                pair_stats[key][0] += 1
                if is_done:
                    pair_stats[key][1] += 1
            if has_backend:
                key = (label, "backend")
                pair_stats[key][0] += 1
                if is_done:
                    pair_stats[key][1] += 1

    def pct(done: int, total: int) -> str:
        return f"{(done / total * 100):.0f}%" if total else "n/a"

    print("=== % Done по лейблам (кроме frontend/backend) ===")
    for label in sorted(stats):
        total, done = stats[label]
        print(f"{label:20s} {pct(done, total):>5s}  ({done}/{total})")

    print()
    print("=== % Done по парам label + frontend / label + backend ===")
    for label, side in sorted(pair_stats):
        total, done = pair_stats[(label, side)]
        print(f"{label:20s} + {side:8s} {pct(done, total):>5s}  ({done}/{total})")


if __name__ == "__main__":
    main()
