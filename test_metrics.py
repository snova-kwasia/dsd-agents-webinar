"""Tests for metrics module."""

from metrics import compute_average


def test_compute_average():
    """Test that compute_average returns the correct arithmetic mean."""
    assert compute_average([1, 2, 3]) == 2


if __name__ == "__main__":
    test_compute_average()
    print("All tests passed!")