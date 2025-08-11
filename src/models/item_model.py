items = [
    {
        "id": 1,
        "name": "item1",
        "description": "This is item 1",
        "vat": 0.05,
        "cost": 10.0,
        "price": 12.0,
    },
    {
        "id": 2,
        "name": "item2",
        "description": "This is item 2",
        "vat": 0.021,
        "cost": 15.0,
        "price": 18.0,
    },
    {
        "id": 3,
        "name": "item3",
        "description": "This is item 3",
        "vat": 0.015,
        "cost": 20.0,
        "price": 23.0,
    },
]


class ItemModel:
    @staticmethod
    def get_all_items():
        return items
