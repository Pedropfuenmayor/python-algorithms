from two_sum import two_sum_v1, two_sum_v2


def test_target_found():
    assert two_sum_v1([1, 3, 4, 6, 8, 10, 13], 13) is True


def test_target_not_found():
    assert two_sum_v1([1, 3, 4, 6, 8, 10, 13], 6) is False


def test_length_less_than_two():
    assert two_sum_v2([1], 13) is False


def test_target_less_than_minimal_sum():
    assert two_sum_v2([2, 3], 1) is False


def test_target_greater_than_maximal_sum():
    assert two_sum_v2([1, 3], 10) is False


def test_target_found_v2():
    assert two_sum_v2([1, 3, 4, 6, 8, 10, 13], 13) is True


def test_target_not_found_v2():
    assert two_sum_v2([1, 3, 4, 6, 8, 10, 13], 6) is False
