"""CreativeCode CLI, stdlib-only. Run `python -m creativecode --help`."""

from __future__ import annotations
import argparse
import json
import sys
from .concepts import generate, load_json, save_json
from .originality import compare
from .critic import prepare


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="creativecode", description="Structural concept discovery and review toolkit (no AI API)")
    sub = parser.add_subparsers(dest="command", required=True)
    p1 = sub.add_parser("concepts", help="Generate three curated concept blueprints from a JSON brief")
    p1.add_argument("--brief", required=True)
    p1.add_argument("--out", required=True)
    p2 = sub.add_parser("originality", help="Compare declared concept structures; not a visual originality check")
    p2.add_argument("--concepts", required=True)
    p2.add_argument("--out", required=True)
    p3 = sub.add_parser("critique", help="Prepare evidence-gated critic packet; no automatic aesthetic score")
    p3.add_argument("--brief", required=True)
    p3.add_argument("--concepts", required=True)
    p3.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "concepts":
            result = generate(load_json(args.brief))
        elif args.command == "originality":
            result = compare(load_json(args.concepts))
        else:
            result = prepare(load_json(args.brief), load_json(args.concepts))
        save_json(args.out, result)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
