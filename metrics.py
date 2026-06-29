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