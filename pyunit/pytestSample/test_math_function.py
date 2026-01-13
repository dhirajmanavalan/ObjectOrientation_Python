import math_function
import pytest


def test_add():
    assert math_function.add(5, 5) == 10
    assert math_function.add(7, 2) == 9
    assert (math_function.add(3, )== 8)



def test_mul():
    assert math_function.mul(2, 3) == 6
    assert math_function.mul(3) == 6
    assert math_function.mul(1) == 1


def test_add_string():
    result = math_function.add("Hello", "World")
    assert result == "HelloWorld"
    assert type(result) is str
    assert "Hello" in result



def test_mul_string():
    assert math_function.mul("Hello ", 3) == "Hello Hello Hello "
    result = math_function.mul("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result
