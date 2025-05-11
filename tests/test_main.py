from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/items", json={
        "id": 1,
        "name": "Stylo",
        "price": 2.5,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Stylo"


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_by_id():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_item():
    response = client.put("/items/1", json={
        "id": 1,
        "name": "Stylo bleu",
        "price": 3.0,
        "in_stock": False
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Stylo bleu"


def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
