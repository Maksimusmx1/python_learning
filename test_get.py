import pytest
import requests
import json

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/1"
    responce_get = requests.get(url)
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['status'] == "OK"

def test_get_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet/12345"
    responce_get = requests.get(url)
    print("responce =", responce_get.json())
    assert responce_get.json()['message'] == "Pet not found"