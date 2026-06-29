from metrics import compute_average

def test_compute_average():
    assert compute_average([1, 2, 3]) == 2
