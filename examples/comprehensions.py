"""Comprehension drills."""
names = ["  Maple", "oak", "BIRCH ", "maple"]
normalized = [name.strip().casefold() for name in names]
unique = sorted(set(normalized))
lengths = {name: len(name) for name in unique}

if __name__ == "__main__":
    print("Raw:", names)
    print("Unique:", unique)
    print("Lengths:", lengths)
