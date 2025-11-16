import pytest
from tests.api.item import ItemAPI
from tests.helpers.data_provider import load_json_data


data = load_json_data("item_test_data.json")


# Тесты для ручки GET /api/1/item/:id
@pytest.mark.parametrize("item_case", data["test_get_item_by_id"])
def test_get_item_by_id_from_json(api_client, item_case):
    """
    Параметризованный тест для ручки GET /api/1/item/:id.
    """
    item_api = ItemAPI(api_client)
    response = item_api.get_item_by_id(item_case["item_id"])
    expected_status = item_case["expected_status"]
    description = item_case.get("description", "GET /api/1/item/:id test")
    assert response.status_code == expected_status, (
        f"{description}: expected status {expected_status}, got {response.status_code}"
    )


# Тесты для ручки POST /api/1/item (создание объявления)
@pytest.mark.parametrize("item_case", data["test_create_item"])
def test_create_item_from_json(api_client, item_case):
    """
    Параметризованный тест для ручки POST /api/1/item.
    """
    item_api = ItemAPI(api_client)
    response = item_api.create_item(item_case["payload"])
    expected_status = item_case["expected_status"]
    description = item_case.get("description", "POST /api/1/item test")
    assert response.status_code == expected_status, (
        f"{description}: expected status {expected_status}, got {response.status_code}"
    )
    # Если запись успешно создана (обычно 201 или 200), проверяем GET
    if expected_status in (200, 201):
        # ⚠️ предполагаем, что item_id возвращается в response.json()
        response_body = response.json()
        created_id = response_body.get("id") or response_body.get("item_id")

        assert created_id, f"POST succeeded but response did not contain item id: {response_body}"

        # GET для валидации
        get_response = item_api.get_item_by_id(created_id)
        assert get_response.status_code == 200, (
            f"Created item {created_id} not found via GET, status={get_response.status_code}"
        )
        assert get_response.json().get("id") == created_id, (
            f"GET returned wrong item: expected id {created_id}, got {get_response.json()}"
        )


# Тесты для ручки GET /api/1/:sellerID/item (получение объявлений по sellerID)
@pytest.mark.parametrize("item_case", data["test_get_items_by_seller"])
def test_get_items_by_seller_from_json(api_client, item_case):
    """
    Параметризованный тест для ручки GET /api/1/:sellerID/item.
    """
    item_api = ItemAPI(api_client)
    seller_id = item_case["seller_id"]
    response = item_api.get_items_by_seller(seller_id)
    expected_status = item_case["expected_status"]
    description = item_case.get("description", "GET /api/1/:sellerID/item test")
    assert response.status_code == expected_status, (
        f"{description}: expected status {expected_status}, got {response.status_code}"
    )


# Тесты для ручки GET /api/1/statistic/:id (получение статистики по объявлению)
@pytest.mark.parametrize("item_case", data["test_get_item_statistic"])
def test_get_item_statistic_from_json(api_client, item_case):
    """
    Параметризованный тест для ручки GET /api/1/statistic/:id.
    """
    item_api = ItemAPI(api_client)
    response = item_api.get_item_statistic(item_case["item_id"])
    expected_status = item_case["expected_status"]
    description = item_case.get("description", "GET /api/1/statistic/:id test")
    assert response.status_code == expected_status, (
        f"{description}: expected status {expected_status}, got {response.status_code}"
    )
