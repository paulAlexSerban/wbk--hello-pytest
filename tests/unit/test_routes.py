import pytest
from src.app import create_app


class TestRoutes:
    @pytest.fixture
    def client(self):
        app = create_app("testing")
        return app.test_client()

    def test_health_endpoint(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "ok"
        assert data["service"] == "hello-pytest-api"

    def test_index_endpoint(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.get_json()
        assert "Welcome to Hello PyTest API" in data["message"]
        assert "endpoints" in data
