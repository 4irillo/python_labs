import argparse
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx
except ImportError:
    print(
        "Error: lab05/json_csv.py or lab05/cvs_xlsx not found or broken",
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="cli_convert", description="Convert between JSON, CSV, and XLSX formats"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # json2csv
    j2c = subparsers.add_parser("json2csv", help="Convert JSON to CSV")
    j2c.add_argument("--in", dest="input", required=True, help="Input JSON file")
    j2c.add_argument("--out", dest="output", required=True, help="Output CSV file")

    # csv2json
    c2j = subparsers.add_parser("csv2json", help="Convert CSV to JSON")
    c2j.add_argument("--in", dest="input", required=True, help="Input CSV file")
    c2j.add_argument("--out", dest="output", required=True, help="Output JSON file")

    # csv2xlsx
    c2x = subparsers.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    c2x.add_argument("--in", dest="input", required=True, help="Input CSV file")
    c2x.add_argument("--out", dest="output", required=True, help="Output XLSX file")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        else:
            parser.print_help()
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: File not found — '{e}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
