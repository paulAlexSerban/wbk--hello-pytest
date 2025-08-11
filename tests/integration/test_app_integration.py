import pytest
from unittest.mock import patch, MagicMock
from src.app import create_app


class TestAppIntegration:
    @pytest.fixture
    def app(self):
        return create_app("testing")

    @pytest.fixture
    def client(self, app):
        return app.test_client()

    def test_items_endpoint_integration(self, client):
        with patch(
            "src.controllers.item_controller.ItemController.get_items"
        ) as mock_controller:
            mock_controller.return_value = MagicMock(
                status_code=200, data='[{"id": 1, "name": "test"}]'
            )
            response = client.get("/items")
            assert response.status_code == 200
            mock_controller.assert_called_once()
