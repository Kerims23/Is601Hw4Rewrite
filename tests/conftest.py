from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide
import pytest

fake = Faker()

# This method generates test data based on the num_records input
def generate_test_data(num_records):
    """Generate a set of random calculations and expected results."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure b is not zero when the operation is divide to prevent division by zero.
        if operation_func == divide and b == Decimal('0'):
            b = Decimal('1')

        expected = operation_func(a, b)
        yield a, b, operation_name, operation_func, expected


# Add the num_records option
def pytest_addoption(parser):
    """Add command-line option for pytest to control the number of test records."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")


# Generate dynamic tests based on the num_records option
def pytest_generate_tests(metafunc):
    """Generate test data dynamically based on the --num_records option."""
    if {"a", "b", "operation", "expected"}.intersection(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        
        # Ensure 'operation_name' or 'operation' is used correctly in tests
        parameters = list(generate_test_data(num_records))
        
        # Parametrize the test with the appropriate arguments
        metafunc.parametrize(
            "a,b,operation,expected", 
            [(a, b, op_func, expected) for a, b, op_name, op_func, expected in parameters]
        )
