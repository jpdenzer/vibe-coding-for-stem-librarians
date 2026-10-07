"""
compare_az_lists.py
===================

A small demo for "Vibe Coding for STEM Librarians."

It compares two A-Z database lists (CSV files) and reports:
  * titles found only in list A
  * titles found only in list B
  * titles found in both

The sample data in fake_data/ is MADE UP. None of the titles or providers
are real. This is a simplified stand-in for a real library project.

How to run (from the examples/ folder):
    python compare_az_lists.py

Or point it at your own (de-identified!) files:
    python compare_az_lists.py my_list_a.csv my_list_b.csv --out results.csv

Each CSV needs a column called "title". Other columns are ignored.

Uses only Python's standard library, so there is nothing to install.

License: MIT (see LICENSE-CODE in the repository root).
"""

import argparse
import csv
import re
import sys
from pathlib import Path

# The fake sample files live next to this script, in fake_data/.
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_A = SCRIPT_DIR / "fake_data" / "list_a_fake.csv"
DEFAULT_B = SCRIPT_DIR / "fake_data" / "list_b_fake.csv"


def normalize(title):
    """Turn a title into a "match key" so small differences don't count.

    IMPORTANT: these rules are ASSUMPTIONS. They decide what counts as
    "the same title." Change them to fit your own data, and check the
    results by hand.

      * ignore upper/lower case        "PHYSICS" == "physics"
      * treat "&" the same as "and"    "A & B"   == "A and B"
      * ignore a leading "The"         "The Annals" == "Annals"
      * ignore punctuation             "Letters." == "Letters"
      * ignore extra spaces            "A   B"   == "A B"
    """
    key = title.casefold()
    key = key.replace("&", " and ")
    key = re.sub(r"[^\w\s]", " ", key)      # punctuation -> space
    key = re.sub(r"\s+", " ", key).strip()  # collapse spaces
    if key.startswith("the "):
        key = key[4:]
    return key


def read_titles(path):
    """Read a CSV and return {match_key: original_title}.

    Blank titles are skipped. If the same title appears twice in one file,
    the first spelling is kept and a note is printed.
    """
    titles = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        # Find the "title" column, ignoring capitalization ("Title", "TITLE").
        columns = {name.strip().casefold(): name for name in (reader.fieldnames or [])}
        if "title" not in columns:
            sys.exit(
                f"Error: {path} has no 'title' column. "
                f"Columns found: {reader.fieldnames}"
            )
        title_col = columns["title"]

        for row in reader:
            original = (row.get(title_col) or "").strip()
            if not original:
                continue
            key = normalize(original)
            if key in titles:
                print(f"  Note: duplicate in {Path(path).name}: "
                      f"'{original}' (same as '{titles[key]}')")
                continue
            titles[key] = original
    return titles


def print_group(heading, names):
    print(f"\n{heading} ({len(names)})")
    print("-" * (len(heading) + len(str(len(names))) + 3))
    for name in names:
        print(f"  {name}")
    if not names:
        print("  (none)")


def main():
    parser = argparse.ArgumentParser(
        description="Compare two A-Z database lists and report titles unique to each."
    )
    parser.add_argument("list_a", nargs="?", default=DEFAULT_A,
                        help="CSV file for list A (default: fake sample data)")
    parser.add_argument("list_b", nargs="?", default=DEFAULT_B,
                        help="CSV file for list B (default: fake sample data)")
    parser.add_argument("--out", help="optional: save results to this CSV file")
    args = parser.parse_args()

    print(f"List A: {args.list_a}")
    print(f"List B: {args.list_b}")

    a = read_titles(args.list_a)
    b = read_titles(args.list_b)

    only_a = sorted((a[k] for k in a.keys() - b.keys()), key=str.casefold)
    only_b = sorted((b[k] for k in b.keys() - a.keys()), key=str.casefold)
    both = sorted((a[k] for k in a.keys() & b.keys()), key=str.casefold)

    print(f"\nList A has {len(a)} unique titles; list B has {len(b)}.")
    print_group("Only in list A", only_a)
    print_group("Only in list B", only_b)
    print_group("In both lists", both)

    # A quick sanity check: every title should land in exactly one group.
    assert len(only_a) + len(both) == len(a), "List A totals don't add up!"
    assert len(only_b) + len(both) == len(b), "List B totals don't add up!"

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "where"])
            writer.writerows([t, "only in A"] for t in only_a)
            writer.writerows([t, "only in B"] for t in only_b)
            writer.writerows([t, "in both"] for t in both)
        print(f"\nSaved results to {args.out}")


if __name__ == "__main__":
    main()
