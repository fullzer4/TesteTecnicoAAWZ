import requests

BASE_URL = "http://localhost:8000"

def test_partnership():
    url = f"{BASE_URL}/partnership/"
    with open("./data/partnership.docx", "rb") as file:
        response = requests.post(url, files={"file": file})
    
    print(response.json())


test_partnership()
