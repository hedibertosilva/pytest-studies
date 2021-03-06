import math_func
import pytest


@pytest.mark.parametrize('x, y, result',
                         [
                             (1, 2, 3),
                             ("Hello ", "World", "Hello World"),
                             (1.0, 2.0, 3.0)
                         ])
def test_add(x, y, result):
    assert math_func.add(x, y) == result

