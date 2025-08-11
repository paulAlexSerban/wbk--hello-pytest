import pytest
import time
from concurrent.futures import ThreadPoolExecutor
from src.app import create_app


class TestPerformance:
    @pytest.fixture
    def client(self):
        app = create_app("testing")
        return app.test_client()

    def test_health_endpoint_response_time(self, client):
        start_time = time.time()
        response = client.get("/health")
        end_time = time.time()

        assert response.status_code == 200
        assert (end_time - start_time) < 0.1  # Should respond in less than 100ms

    def test_concurrent_requests(self, client):
        def make_request():
            return client.get("/health")

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(50)]
            results = [future.result() for future in futures]

        assert all(r.status_code == 200 for r in results)
