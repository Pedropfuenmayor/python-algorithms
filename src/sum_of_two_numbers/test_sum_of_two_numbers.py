from sum_of_two_numbers import sum_of_two_numbers

def test_positive_numbers():
    assert sum_of_two_numbers(1, 2) == 3
    assert sum_of_two_numbers(10, 20) == 30

def test_negative_numbers():
    assert sum_of_two_numbers(-1, -2) == -3
    assert sum_of_two_numbers(-10, -20) == -30

def test_mixed_numbers():
    assert sum_of_two_numbers(-1, 2) == 1
    assert sum_of_two_numbers(10, -5) == 5

def test_zero():
    assert sum_of_two_numbers(0, 0) == 0
    assert sum_of_two_numbers(0, 5) == 5
    assert sum_of_two_numbers(-3, 0) == -3