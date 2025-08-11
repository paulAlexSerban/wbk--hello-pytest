"""Register routes for the Flask application.

Returns:
    None
"""

from flask import Flask

from src.controllers.item_controller import ItemController
from src.controllers.math_controller import MathController
from src.controllers.string_controller import StringController


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

    @flask_app.route("/items", methods=["POST"])
    def create_item():
        return ItemController().create_item_controller()

    @flask_app.route("/items/<int:item_id>", methods=["PUT"])
    def update_item(item_id):
        return ItemController().update_item_controller(item_id)

    @flask_app.route("/items/<int:item_id>", methods=["DELETE"])
    def delete_item(item_id):
        return ItemController().delete_item_controller(item_id)

    # Math routes
    @flask_app.route("/add", methods=["POST"])
    def addition():
        return MathController.add()

    # String routes
    @flask_app.route("/reverse", methods=["POST"])
    def reverse():
        return StringController.reverse_string()


app = Flask(__name__)

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
