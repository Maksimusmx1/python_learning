import pytest
import requests
import json
import resources.urls as urls
import Steps.support_steps as support_steps

def test_get_pet():
    responce_get = requests.get(urls.url_pet_get_id("1"))
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['status'] == "sold"

def test_get_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet/12345"
    responce_get = requests.get(urls.url_pet_get_id("1234567"))
    print("responce =", responce_get.json())
    assert responce_get.json()['message'] == "Pet not found"