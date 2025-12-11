import argparse
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from libs.text import tokenize, normalize, count_freq, top_n, summarize
except ImportError:
    print("Error: libs/text.py not found or broken", file=sys.stderr)
    sys.exit(1)


def cat_file(input_path: str, number: bool = False) -> None:
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                if number:
                    print(f"{i:4}: {line.rstrip()}")
                else:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"Error: File not found — '{input_path}'", file=sys.stderr)
        sys.exit(1)


def stats_text(input_path: str, top: int = 5) -> None:
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found — '{input_path}'", file=sys.stderr)
        sys.exit(1)
    summarize(text, top)


def main():
    parser = argparse.ArgumentParser(
        prog="cli_text",
        description="CLI tools for text processing: cat and word stats (Lab 06)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Print file content line by line")
    cat_parser.add_argument("--input", required=True, help="Path to input file")
    cat_parser.add_argument("-n", action="store_true", help="Number all output lines")

    stats_parser = subparsers.add_parser("stats", help="Show word frequency statistics")
    stats_parser.add_argument("--input", required=True, help="Path to input text file")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Number of top words to show (default: 5)"
    )

    args = parser.parse_args()

    if args.command == "cat":
        cat_file(args.input, args.n)
    elif args.command == "stats":
        stats_text(args.input, args.top)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
