from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def print_menu():
    """Prints the menu of operations."""
    print("\nCalculator Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_input():
    """Get numbers and operation choice from the user."""
    try:
        a = Decimal(input("Enter the first number: "))
        b = Decimal(input("Enter the second number: "))
        print_menu()
        operation_choice = input("Choose an operation (1-4): ")
        return a, b, operation_choice
    except Exception as e:
        print(f"Invalid input: {e}")
        return None, None, None

def perform_operation(a, b, operation_choice):
    """Perform the operation based on user's choice."""
    operations_map = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }

    operation_func = operations_map.get(operation_choice)
    if operation_func is None:
        print("Invalid operation choice")
        return

    try:
        calculation = Calculation.create(a, b, operation_func)
        result = calculation.perform()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    """Main function to run the interactive calculator."""
    print("Welcome to the Calculator!")

    while True:
        a, b, operation_choice = get_user_input()

        if a is None or b is None:
            continue

        if operation_choice == "5":
            print("Exiting calculator.")
            break

        perform_operation(a, b, operation_choice)

if __name__ == "__main__":
    main()
