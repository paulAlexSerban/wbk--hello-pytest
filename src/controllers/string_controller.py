from flask import jsonify, request


class StringController:
    @staticmethod
    def reverse_string():
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Invalid input"}), 400
        reversed_text = data["text"][::-1]
        return jsonify({"reversed": reversed_text}), 200
