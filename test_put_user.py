import pytest
import requests
import json

def test_put_user():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = 1
    request['username'] = "Catty"
    request['firstname'] = "Cat"
    request['lastname'] = "Sber"
    request['email'] = "SberCat@sber.ru"
    request['password'] = "sber_pass"
    request['phone'] = "999-99-99"
    request['userstatus'] = "0"
    print("request =", request)
    url_put = url + "/" + str(request['username'])
    print("url_put =",url_put)
    responce_post = requests.put(url_put, json=request)
    print("result = ", responce_post.json())

    responce_get = requests.get(url_put)
    print("responce =", responce_get.json())