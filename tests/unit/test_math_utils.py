"""Unit tests for the MathUtils class."""

import pytest
from src.utils.math_utils import MathUtils


class TestMathUtils:
    """Unit tests for MathUtils."""

    @pytest.mark.sanity
    @pytest.mark.math
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert MathUtils.add(2, 3) == 5

    @pytest.mark.math
    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        assert MathUtils.add(-1, 1) == 0

    @pytest.mark.sanity
    @pytest.mark.math
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert MathUtils.subtract(5, 3) == 2

    @pytest.mark.math
    def test_subtract_same_numbers(self):
        """Test subtracting same numbers."""
        assert MathUtils.subtract(0, 0) == 0

    @pytest.mark.sanity
    @pytest.mark.math
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert MathUtils.multiply(2, 3) == 6

    @pytest.mark.math
    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        assert MathUtils.multiply(-1, 1) == -1

    @pytest.mark.sanity
    @pytest.mark.math
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert MathUtils.divide(6, 3) == 2

    @pytest.mark.math
    def test_divide_fails(self):
        """Test the divide method for failure cases."""
        with pytest.raises(Exception):
            assert MathUtils.divide(9, 5) == 1.5, "failed test intentionally"

    @pytest.mark.sanity
    @pytest.mark.math
    def test_divide_by_zero_try_except(self):
        """Test division by zero using try-except."""
        try:
            MathUtils.divide(1, 0)
        except ZeroDivisionError:
            assert True
        else:
            assert False

    @pytest.mark.math
    def test_divide_by_zero_pytest_raises(self):
        """Test division by zero using pytest.raises."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
            MathUtils.divide(10, 0)

    @pytest.mark.math
    @pytest.mark.xfail(
        raises=ZeroDivisionError,
        reason="This test is expected to fail due to division by zero.",
    )
    def test_divide_by_zero_pytest_raises_xfail(self):
        """Test division by zero using pytest.raises."""
        assert MathUtils.divide(10, 0)
