import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.fixture
def url():
    return f"{BASE_URL}/verify/"

def test_verify(url):
    csv1_path = "./data/vendas.csv"
    csv2_path = "./data/pagamentos.csv"

    with open(csv1_path, "rb") as file1, open(csv2_path, "rb") as file2:
        response = requests.post(url, files={"csv1": file1, "csv2": file2})

    assert response.status_code == 200

    data = response.json()["data"]
    assert len(data) > 0
