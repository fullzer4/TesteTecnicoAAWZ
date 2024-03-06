import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def url():
    return f"{BASE_URL}/partnership/"

def test_payment():
    with open("./data/pagamentos.csv", "rb") as file:
        response = requests.post(url, files={"file": file})

    assert response.status_code == 200

    assert isinstance(response.json(), list)
    for item in reponse.json():
        assert "pago" in item

def test_upload_invalid_file(url):
    with open("./data/partnership.docx", "rb") as file:
        response = requests.post(url, files={"file": file})

    assert response.status_code == 400
