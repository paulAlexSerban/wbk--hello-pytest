from src.app import create_app


class TestAppFactory:
    def test_create_app_development_config(self):
        app = create_app("development")
        assert app.config["DEBUG"] is True
        assert app.config["TESTING"] is False

    def test_create_app_testing_config(self):
        app = create_app("testing")
        assert app.config["TESTING"] is True
        assert app.config["DEBUG"] is False

    def test_create_app_default_config(self):
        app = create_app()
        assert app.config["JSON_SORT_KEYS"] is False
