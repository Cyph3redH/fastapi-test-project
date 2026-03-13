from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Добро пожаловать в FastAPI!"}

def test_create_user():
    response = client.post("/users/", json={"name": "Иван", "age": 30, "email": "ivan@example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Пользователь Иван создан"