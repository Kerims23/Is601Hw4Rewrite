"""Test calculation history for the calculator."""

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.transactions import Calculations
from calculator.operations import add

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_clear_history():
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0
