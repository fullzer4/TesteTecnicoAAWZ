import requests

BASE_URL = "http://localhost:8000"

def test_verify():
    url = f"{BASE_URL}/verify/"
    csv1_path = "./data/vendas.csv"
    csv2_path = "./data/pagamentos.csv"

    with open(csv1_path, "rb") as file1, open(csv2_path, "rb") as file2:
        response = requests.post(url, files={"csv1": file1, "csv2": file2})

    data = response.json()["data"]
    print(data)

test_verify()
