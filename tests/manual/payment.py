import requests

BASE_URL = "http://localhost:8000"

def test_payment():
    url = f"{BASE_URL}/payment/"
    with open("./data/vendas.csv", "rb") as file:
        response = requests.post(url, files={"file": file})

    print(response.json())

test_payment()
