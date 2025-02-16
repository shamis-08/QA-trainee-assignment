# tests/api/item.py
class ItemAPI:
    def __init__(self, client):
        self.client = client

    def get_item_by_id(self, item_id: str):
        path = f"/api/1/item/{item_id}"
        headers = {"Accept": "application/json"}
        return self.client.get(path, headers=headers)

    def create_item(self, payload: dict):
        path = "/api/1/item"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        return self.client.post(path, json=payload, headers=headers)

    def get_items_by_seller(self, seller_id: str):
        path = f"/api/1/{seller_id}/item"
        headers = {"Accept": "application/json"}
        return self.client.get(path, headers=headers)

    def get_item_statistic(self, item_id: str):
        path = f"/api/1/statistic/{item_id}"
        headers = {"Accept": "application/json"}
        return self.client.get(path, headers=headers)
