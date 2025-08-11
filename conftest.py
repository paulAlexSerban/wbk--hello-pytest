from unittest.mock import patch
import pytest
from src.app import create_app


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
