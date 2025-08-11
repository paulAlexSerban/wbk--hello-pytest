from flask import jsonify, request

from src.utils.math_utils import MathUtils

class MathController:
    """Controller for math operations."""
    @staticmethod
    def add():
        """Add two numbers."""
        data = request.get_json()
        if not data or "a" not in data or "b" not in data:
            return jsonify({"error": "Invalid input"}), 400
        result = MathUtils.add(data["a"], data["b"])
        return jsonify({"result": result}), 200

    @staticmethod
    def subtract():
        """Subtract two numbers."""
        data = request.get_json()
        if not data or "a" not in data or "b" not in data:
            return jsonify({"error": "Invalid input"}), 400
        result = MathUtils.subtract(data["a"], data["b"])
        return jsonify({"result": result}), 200

    @staticmethod
    def multiply():
        """Multiply two numbers."""
        data = request.get_json()
        if not data or "a" not in data or "b" not in data:
            return jsonify({"error": "Invalid input"}), 400
        result = MathUtils.multiply(data["a"], data["b"])
        return jsonify({"result": result}), 200

    @staticmethod
    def divide():
        """Divide two numbers."""
        data = request.get_json()
        if not data or "a" not in data or "b" not in data:
            return jsonify({"error": "Invalid input"}), 400
        if data["b"] == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = MathUtils.divide(data["a"], data["b"])
        return jsonify({"result": result}), 200
