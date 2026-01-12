import math_function

def test_add():
    assert math_function.add(5,5) == 10
    assert math_function.add(7,2) == 9
    assert math_function.add(3,) == 8
    
def test_mul():
    assert math_function.mul(2,3) == 6
    assert math_function.mul(3) == 15
    assert math_function.mul(1) == 5 