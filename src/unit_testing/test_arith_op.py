import pytest
import arith_op as arith_op
def test_add():
    result = arith_op.add(2, 3)
    assert result == 5
def test_subtract():
    result = arith_op.subtract(5, 2)
    assert result == 3
def test_multiply():
    result = arith_op.multiply(4, 3)
    assert result == 12
def test_divide():
    result = arith_op.divide(10, 2)
    assert result == 5
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        arith_op.divide(10, 0)
def test_add_strings():
    result=arith_op.add("Hello, ", "World!")
    assert result == "Hello, World!"
