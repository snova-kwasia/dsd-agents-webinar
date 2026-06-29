from metrics import compute_average, compute_median

def test_compute_average():
    assert compute_average([1, 2, 3]) == 2

def test_compute_median():
    assert compute_median([1, 2, 3]) == 2
