# Programming Fundamentals: offline data-signature examples
#
# Numeric utilities with deterministic inputs for classroom exercises.

def rolling_average(samples, window=3):
    if window < 1:
        raise ValueError("window must be positive")
    values = list(samples)
    return [
        sum(values[max(0, index - window + 1):index + 1]) /
        min(index + 1, window)
        for index in range(len(values))
    ]

def bubble_sort(values):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
    return result

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert fibonacci(7) == 13
    print("Exercises passed")
