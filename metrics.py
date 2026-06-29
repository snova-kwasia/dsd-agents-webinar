"""Metrics module for computing statistical measures."""


def compute_average(numbers):
    """Compute the arithmetic mean of a list of numbers.
    
    Args:
        numbers: A list of numeric values.
        
    Returns:
        The arithmetic mean as a float.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def compute_median(numbers):
    """Compute the median of a list of numbers.
    
    Args:
        numbers: A list of numeric values.
        
    Returns:
        The median as a float.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return float(sorted_numbers[mid])