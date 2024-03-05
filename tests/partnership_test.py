import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def upload_url():
    return f"{BASE_URL}/partnership/"

def test_upload_docx(upload_url):
    with open("./data/partnership.docx", "rb") as file:
        response = requests.post(upload_url, files={"file": file})
    
    assert response.status_code == 200
    
    assert isinstance(response.json(), list)
    for item in response.json():
        assert "nome" in item
        assert "cotas" in item


def test_upload_invalid_file(upload_url):
    with open("./data/vendas.csv", "rb") as file:
        response = requests.post(upload_url, files={"file": file})
    
    assert response.status_code == 400
    assert "Only .docx files allowed" in response.text

