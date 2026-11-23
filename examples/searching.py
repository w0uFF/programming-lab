"""Compare linear search and binary search on a sorted list."""


def linear_search(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        center = (left + right) // 2
        value = sorted_values[center]
        if value == target:
            return center
        if value < target:
            left = center + 1
        else:
            right = center - 1
    return -1


if __name__ == "__main__":
    sample = [2, 4, 7, 12, 19, 27]
    assert linear_search(sample, 19) == 4
    assert binary_search(sample, 19) == 4
    assert binary_search(sample, 8) == -1
    print("Search examples passed")
