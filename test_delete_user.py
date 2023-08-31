import pytest
import requests
import json

def test_delete_user():
    url = "https://petstore.swagger.io/v2/user"
    userName = "Catty"
    url_delete = url + "/" + userName
    print("URL_delete", url_delete)
    responce_delete = requests.delete(url_delete)
    print("responce =", responce_delete.json())

    responce_get = requests.get(url_delete)
    print("responce =", responce_get.json())
