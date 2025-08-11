"""Unit tests for temperature conversion utilities."""

import sys
import pytest

from src.utils.temperature_utils import (
    centigrade_to_fahrenheit,
    fahrenheit_to_centigrade,
    kelvin_to_centigrade,
    centigrade_to_kelvin,
)


class TestTemperatureUtils:
    """Unit tests for temperature conversion utilities."""

    def test_centigrade_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        assert centigrade_to_fahrenheit(0) == 32
        assert centigrade_to_fahrenheit(100) == 212

    def test_fahrenheit_to_centigrade(self):
        """Test Fahrenheit to Celsius conversion."""
        assert fahrenheit_to_centigrade(32) == 0
        assert fahrenheit_to_centigrade(212) == 100

    def test_kelvin_to_centigrade(self):
        """Test Kelvin to Celsius conversion."""
        assert kelvin_to_centigrade(273.15) == 0
        assert kelvin_to_centigrade(373.15) == 100

    def test_centigrade_to_kelvin(self):
        """Test Celsius to Kelvin conversion."""
        assert centigrade_to_kelvin(0) == 273.15
        assert centigrade_to_kelvin(100) == 373.15

    @pytest.mark.skip(reason="Skipping this test for demonstration purposes")
    def test_centigrade_to_fahrenheit_one(self):
        """Test Celsius to Fahrenheit conversion."""
        assert centigrade_to_fahrenheit(0) == 32
        assert centigrade_to_fahrenheit(100) == 212

    @pytest.mark.skipif(
        condition=sys.version_info < (3, 13), reason="Requires Python 3.13 or higher"
    )
    def test_centigrade_to_fahrenheit_two(self):
        """Test Celsius to Fahrenheit conversion."""
        assert centigrade_to_fahrenheit(0) == 32
        assert centigrade_to_fahrenheit(100) == 212
