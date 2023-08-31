import pytest
import requests
import json

def test_get_user():
    url = "https://petstore.swagger.io/v2/user"
    userName = "Catty"
    url_get = url + "/" + userName
    responce_get = requests.get(url_get)
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['userStatus'] == 0