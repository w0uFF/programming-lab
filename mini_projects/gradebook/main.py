#!/usr/bin/env python3
"""Report statistics for invented score fixtures."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from lab.csv_utils import read_scores
from lab.stats import mean, median


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize sample exercise scores")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    scores = read_scores(args.csv_file)
    print("SAMPLE ID".ljust(20), "COUNT  AVERAGE  MEDIAN")
    for sample_id, values in sorted(scores.items()):
        print(sample_id.ljust(20), f"{len(values):5d}  {mean(values):7.2f}  {median(values):6.2f}")
    print(f"Total sample entries: {sum(len(x) for x in scores.values())}")


if __name__ == "__main__":
    main()
