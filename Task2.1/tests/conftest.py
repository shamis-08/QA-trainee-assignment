# tests/conftest.py
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.api.client import ApiClient

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://qa-internship.avito.com")

@pytest.fixture(scope="session")
def api_client(base_url):
    return ApiClient(base_url)
