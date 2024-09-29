"""Main program for the calculator."""

from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from calculator.transactions import Calculations

def main():
    """Main function to demonstrate the calculator."""
    print("Simple Calculator:")
    
    # Example calculations
    a, b = Decimal('10'), Decimal('5')
    
    # Add calculation
    addition = Calculation.create(a, b, add)
    result = addition.perform()
    Calculations.add_calculation(addition)
    print(f"Addition: {a} + {b} = {result}")
    
    # Subtract calculation
    subtraction = Calculation.create(a, b, subtract)
    result = subtraction.perform()
    Calculations.add_calculation(subtraction)
    print(f"Subtraction: {a} - {b} = {result}")
    
    # View history
    print("\nCalculation History:")
    for calc in Calculations.get_history():
        print(f"{calc.a} {calc.operation.__name__} {calc.b} = {calc.perform()}")
    
    # Clear history
    Calculations.clear_history()
    print("\nHistory cleared.")
    
if __name__ == "__main__":
    main()
