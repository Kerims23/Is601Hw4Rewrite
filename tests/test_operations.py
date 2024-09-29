"""Test operations for the calculator."""

from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    """Test addition."""
    assert add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    """Test subtraction."""
    assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply():
    """Test multiplication."""
    assert multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide():
    """Test division."""
    assert divide(Decimal('6'), Decimal('3')) == Decimal('2')

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError):
        divide(Decimal('1'), Decimal('0'))
