import math_func


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(1) == 3
    assert math_func.add(0) == 2


def test_product():
    assert math_func.product(7, 3) == 21
    assert math_func.product(5, 5) == 25
    assert math_func.product(2) == 4

