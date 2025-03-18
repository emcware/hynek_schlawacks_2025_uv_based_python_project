from fastapi.testclient import TestClient
import pytest
from src.hello_svc.views import app


@pytest.fixture(name="client")
def _client():
    return TestClient(app)

def test_hello(client):
    """
    Root URL greets the world
    :param client:
    :return:
    """
    response = client.get("/")
    assert response.status_code == 200
    assert {
        "message": "Hello World",
    } == response.json()

