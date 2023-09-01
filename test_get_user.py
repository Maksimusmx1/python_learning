import pytest
import requests
import json
import resources.urls as urls
import Steps.support_steps as support_steps

def test_get_user():
    userName = "Catty"
    url_get = urls.url_pet_user + "/" + userName
    responce_get = requests.get(url_get)
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['userStatus'] == 0