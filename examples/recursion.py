"""Small recursion and memoization examples."""
from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs(steps: int) -> int:
    if steps < 0:
        return 0
    if steps <= 1:
        return 1
    return climb_stairs(steps - 1) + climb_stairs(steps - 2)


def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print("Ways to climb five steps:", climb_stairs(5))
    print("Flattened:", flatten([1, [2, 3], [[4]]]))
