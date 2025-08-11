"""Unit tests for the MathUtils class."""

import pytest
from src.utils.math_utils import MathUtils


class TestMathUtils:
    """Unit tests for MathUtils."""

    def test_add(self):
        """Test the add method."""
        assert MathUtils.add(2, 3) == 5
        assert MathUtils.add(-1, 1) == 0

    def test_subtract(self):
        """Test the subtract method."""
        assert MathUtils.subtract(5, 3) == 2
        assert MathUtils.subtract(0, 0) == 0

    def test_multiply(self):
        """Test the multiply method."""
        assert MathUtils.multiply(2, 3) == 6
        assert MathUtils.multiply(-1, 1) == -1

    def test_divide(self):
        """Test the divide method."""
        assert MathUtils.divide(6, 3) == 2

    def test_divide_fails(self):
        """Test the divide method for failure cases."""
        with pytest.raises(Exception):
            assert MathUtils.divide(9, 5) == 1.5, "failed test intentionally"

    def test_divide_zero(self):
        """Test the divide method with zero."""

        # Ensure that the exception is raised
        try:
            MathUtils.divide(1, 0)
        except ZeroDivisionError:
            assert True
        else:
            assert False

        # Alternatively, using pytest.raises for cleaner syntax
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
            MathUtils.divide(10, 0)
