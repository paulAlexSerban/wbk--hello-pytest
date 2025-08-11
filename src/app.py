"""Register routes for the Flask application.

Returns:
    None
"""

from flask import Flask

from src.controllers.item_controller import ItemController

def register_routes(flask_app: Flask):
    """Register routes for the Flask application.

    Args:
        flask_app (Flask): The Flask application instance.

    Returns:
        None
    """
    # Health check
    @flask_app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}

    # Item routes
    @flask_app.route("/items", methods=["GET"])
    def items():
        return ItemController().get_items()

app = Flask(__name__)

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
