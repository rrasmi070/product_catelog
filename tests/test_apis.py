import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "A product for testing",
        "price": 10.0,
        "inventory_count": 100,
        "category": "Test"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_read_product():
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product():
    response = client.put("/products/1", json={
        "name": "Updated Product",
        "description": "An updated product",
        "price": 15.0,
        "inventory_count": 80,
        "category": "Test"
    })
    assert response.status_code == 200

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
