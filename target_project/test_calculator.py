from calculator import average


def test_average_positive_numbers():
    assert average([2, 4, 6]) == 4


def test_average_negative_numbers():
    assert average([-2, 4]) == 1
