"""Tests for metrics module."""

from metrics import compute_average, compute_median


def test_compute_average():
    """Test that compute_average returns the correct arithmetic mean."""
    assert compute_average([1, 2, 3]) == 2


def test_compute_median():
    """Test that compute_median returns the correct median."""
    assert compute_median([1, 2, 3]) == 2


if __name__ == "__main__":
    test_compute_average()
    test_compute_median()
    print("All tests passed!")