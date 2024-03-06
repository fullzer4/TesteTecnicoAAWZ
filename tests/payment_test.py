import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def url():
    return f"{BASE_URL}/payment/"

def test_payment(url):
    with open("./data/vendas.csv", "rb") as file:
        response = requests.post(url, files={"file": file})

    assert response.status_code == 200
    assert 'data' in response.json()

def test_upload_invalid_file(url):
    with open("./data/partnership.docx", "rb") as file:
        response = requests.post(url, files={"file": file})

    assert response.status_code == 400
