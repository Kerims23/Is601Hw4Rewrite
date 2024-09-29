"""Module to handle Calculation operations."""

from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """Handles a single calculation."""

    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """Performs the operation."""
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation):
        """Factory method to create a new Calculation."""
        return Calculation(a, b, operation)
