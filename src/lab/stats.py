"""Descriptive statistics exercises."""
from collections.abc import Iterable
from math import sqrt


def mean(values: Iterable[float]) -> float:
    items = list(values)
    if not items:
        raise ValueError("cannot calculate mean of empty sequence")
    return sum(items) / len(items)


def median(values: Iterable[float]) -> float:
    items = sorted(values)
    if not items:
        raise ValueError("cannot calculate median of empty sequence")
    center = len(items) // 2
    if len(items) % 2:
        return float(items[center])
    return (items[center - 1] + items[center]) / 2


def population_stddev(values: Iterable[float]) -> float:
    items = list(values)
    center = mean(items)
    return sqrt(sum((item - center) ** 2 for item in items) / len(items))
