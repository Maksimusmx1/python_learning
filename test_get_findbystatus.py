import pytest
import requests
import json

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
    responce_get = requests.get(url)
    print("responce =", responce_get.json())
    assert responce_get.json()[0]['status'] == "sold"