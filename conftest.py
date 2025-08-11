from unittest.mock import patch
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