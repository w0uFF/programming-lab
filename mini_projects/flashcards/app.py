#!/usr/bin/env python3
"""A short terminal flashcard exercise with synthetic content."""
import json
from pathlib import Path


def main() -> None:
    path = Path(__file__).with_name("cards.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    print(payload["title"])
    for index, card in enumerate(payload["cards"], start=1):
        print(f"\n{index}. {card['question']}")
        input("Press Enter to reveal the answer...")
        print(card["answer"])


if __name__ == "__main__":
    main()
