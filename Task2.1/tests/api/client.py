import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str, headers: dict = None, params: dict = None, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.get(url, headers=headers, params=params, **kwargs)

    def post(self, path: str, json: dict = None, headers: dict = None, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.post(url, json=json, headers=headers, **kwargs)
