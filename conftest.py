from unittest.mock import patch
from random import randint
import pytest
from src.app import create_app


# conftest.py fixtures are automatically available to all test files
@pytest.fixture(scope="session")
def app():
    """Create application for the tests."""
    app = create_app("testing")
    return app


@pytest.fixture(scope="function")
def client(app):
    """Create a test client."""
    return app.test_client()


@pytest.fixture
def mock_item_controller():
    """Mock ItemController for testing."""
    with patch("src.controllers.item_controller.ItemController") as mock:
        yield mock


@pytest.fixture(scope="function")
def teardown_example():
    """Example fixture for teardown."""
    yield print("on yield - teardown_example fixture")
    print("after yield - teardown_example fixture completed")


def pytest_configure(config):
    """Configure pytest settings."""
    config.test_value = "test_value via config"
    print("pytest_configure called - test_value set to 'test_value'")


@pytest.fixture(scope="function")
def print_request_values(request):
    """Print the test value from the request."""
    print("\nin Fixture print_request_values - test_value")
    print(f"\nFixture scope: {request.scope}")
    print(f"\nCalling function: {request.function.__name__}")


@pytest.fixture
def numbers_generator():
    """Example fixture to demonstrate factory pattern."""

    generated_numbers = []

    def generate_numbers(n):
        """Generate a list of n random numbers."""

        numbers = [randint(1, 100) for _ in range(n)]
        generated_numbers.extend(numbers)
        return numbers

    yield generate_numbers
    print("\nGenerated numbers:", generated_numbers)
