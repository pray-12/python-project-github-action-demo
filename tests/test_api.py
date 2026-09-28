import pytest

from app.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "add" in response.get_json()["operations"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_calculate_add(client):
    response = client.get("/calculate/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_unknown_operation(client):
    response = client.get("/calculate/power?a=2&b=3")
    assert response.status_code == 404


def test_missing_params(client):
    response = client.get("/calculate/add?a=2")
    assert response.status_code == 400


def test_divide_by_zero(client):
    response = client.get("/calculate/divide?a=1&b=0")
    assert response.status_code == 400
