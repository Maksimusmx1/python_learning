import pytest
import requests
import json

def test_post_user():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = 1
    request['username'] = "Catty"
    request['firstname'] = "Cat"
    request['lastname'] = "Sber"
    request['email'] = "SberCat@sber.ru"
    request['password'] = "sber_pass"
    request['phone'] = "123-45-67"
    request['userstatus'] = "0"
    print(request)
    responce_post = requests.post(url, json=request)
    print("result = ", responce_post.json())

