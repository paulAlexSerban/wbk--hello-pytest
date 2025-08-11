items = [
    {"id": 1, "name": "item1"},
    {"id": 2, "name": "item2"},
    {"id": 3, "name": "item3"},
]


class ItemModel:
    @staticmethod
    def get_all_items():
        return items

    @staticmethod
    def create_item(name):
        new_item = {"id": len(items) + 1, "name": name}
        items.append(new_item)
        return new_item

    @staticmethod
    def update_item(item_id, name):
        for item in items:
            if item["id"] == item_id:
                item["name"] = name
                return item
        return None

    @staticmethod
    def delete_item(item_id):
        global items
        items = [item for item in items if item["id"] != item_id]
        return {"message": f"Item {item_id} deleted"}