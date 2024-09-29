"""Test main program for the calculator."""

#import pytest
from main import main

def test_main(capfd):
    """Test the main function output."""
    main()
    # Capture stdout
    out, _ = capfd.readouterr()

    # Check if the output contains expected strings
    assert "Simple Calculator" in out
    assert "Addition: 10 + 5 = 15" in out
    assert "Subtraction: 10 - 5 = 5" in out
    assert "Calculation History:" in out
    assert "History cleared." in out
