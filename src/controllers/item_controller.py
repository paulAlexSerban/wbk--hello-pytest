from flask import jsonify, request

from src.models.item_model import ItemModel


class ItemController:
    @staticmethod
    def get_items():
        return jsonify(ItemModel.get_all_items())

    @staticmethod
    def create_item_controller():
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "Invalid input"}), 400
        new_item = ItemModel.create_item(data["name"])
        return jsonify(new_item), 201

    @staticmethod
    def update_item_controller(item_id):
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "Invalid input"}), 400
        updated_item = ItemModel.update_item(item_id, data["name"])
        if updated_item:
            return jsonify(updated_item), 200
        return jsonify({"error": "Item not found"}), 404

    @staticmethod
    def delete_item_controller(item_id):
        return jsonify(ItemModel.delete_item(item_id)), 200
