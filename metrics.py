def compute_average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def compute_median(numbers):
    """Return the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return float(sorted_numbers[mid])
