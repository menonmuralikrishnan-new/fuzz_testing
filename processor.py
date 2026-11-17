"""Hardened input processors for Lab 7 fuzz testing."""


def parse_int_list(value):
    """Convert valid comma-separated integer tokens; reject unsafe input quietly."""
    if not isinstance(value, str):
        return []
    result = []
    for item in value.split(","):
        token = item.strip()
        if not token:
            continue
        try:
            result.append(int(token))
        except (TypeError, ValueError):
            continue
    return result


def is_palindrome(value):
    """Return whether text reads the same forwards and backwards."""
    if not isinstance(value, str):
        return False
    normalized = "".join(value.lower().split())
    return normalized == normalized[::-1]


def calculate_average(values):
    """Average integer/float values, returning 0.0 when no valid values exist."""
    if not isinstance(values, (list, tuple)):
        return 0.0
    numbers = [item for item in values if isinstance(item, (int, float)) and not isinstance(item, bool)]
    return sum(numbers) / len(numbers) if numbers else 0.0


def demo():
    cases = [
        ("parse_int_list('10, 20, 30')", lambda: parse_int_list("10, 20, 30")),
        ("parse_int_list(None)", lambda: parse_int_list(None)),
        ("is_palindrome('Never odd or even')", lambda: is_palindrome("Never odd or even")),
        ("is_palindrome(None)", lambda: is_palindrome(None)),
        ("calculate_average([10, 20, 30])", lambda: calculate_average([10, 20, 30])),
        ("calculate_average([])", lambda: calculate_average([])),
    ]
    print("Lab 7 - Fixed processor demonstration")
    for label, action in cases:
        try:
            print(f"{label} -> {action()!r}")
        except Exception as exc:
            print(f"{label} -> ERROR: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    demo()
