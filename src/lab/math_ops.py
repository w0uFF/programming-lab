"""Number theory and elementary arithmetic practice."""

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def multiples(start: int, stop: int, divisor: int) -> list[int]:
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    return [n for n in range(start, stop + 1) if n % divisor == 0]


def fibonacci_terms(count: int) -> list[int]:
    if count < 0:
        raise ValueError("count cannot be negative")
    values = []
    a, b = 0, 1
    for _ in range(count):
        values.append(a)
        a, b = b, a + b
    return values
