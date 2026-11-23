"""Small text-processing functions for exercise worksheets."""
import re
from collections import Counter


def normalize_spaces(value: str) -> str:
    return " ".join(value.split())


def words(value: str) -> list[str]:
    return re.findall(r"[^\W_]+(?:'[^\W_]+)?", value.casefold(), flags=re.UNICODE)


def word_counts(value: str) -> dict[str, int]:
    return dict(Counter(words(value)))


def is_palindrome(value: str) -> bool:
    cleaned = "".join(char.casefold() for char in value if char.isalnum())
    return cleaned == cleaned[::-1]


def rotate_ascii(value: str, shift: int) -> str:
    shift %= 26
    result = []
    for char in value:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - 97 + shift) % 26 + 97))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        else:
            result.append(char)
    return "".join(result)
