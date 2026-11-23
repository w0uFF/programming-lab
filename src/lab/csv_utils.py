"""Import fake scores without storing student personal information."""
import csv
from collections import defaultdict
from pathlib import Path


def read_scores(path: str | Path) -> dict[str, list[float]]:
    grouped: dict[str, list[float]] = defaultdict(list)
    with Path(path).open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            sample_id = row["sample_id"].strip()
            if not sample_id:
                continue
            value = float(row["score"])
            if not 0 <= value <= 100:
                raise ValueError("score outside range 0..100")
            grouped[sample_id].append(value)
    return dict(grouped)
