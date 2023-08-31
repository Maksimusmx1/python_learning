import pytest
import requests
import json

def test_post_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = 1
    request['category'] = {}
    request['category']['id'] = 2
    request['category']['name'] = "cats"
    request['name'] = "sberCat"
    request['photoUrls'] = ["photoSberCat1"]
    request['tags'] = [{'id':3,'name':"sberTag"}]
    request['status'] = "avalible"
    print(request)
    responce_post = requests.post(url, json=request)
    print("result = ", responce_post.json())

    request_put = {}
    request_put['id'] = str(responce_post.json()['id'])
    request_put['name'] = "sberWowKitten"
    print(request_put)
    responce_put = requests.put(url, json=request_put)
    print("result =", responce_put.json())

    assert responce_put.json()['photoUrls'] == []

    url_get = url + "/" + str(responce_put.json()['id'])
    print ("url_get ", url_get )

    responce_get = requests.get(url_get)
    print("result_get = ", responce_get.json())
    assert responce_get.json()['id'] == responce_put.json()['id']

def test_post_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = "name"
    request['category'] = {}
    request['category']['id'] = 2
    request['category']['name'] = "cats"
    request['name'] = "sberCat"
    request['photoUrls'] = ["photoSberCat1"]
    request['tags'] = [{'id': 3, 'name': "sberTag"}]
    request['status'] = "avalible"
    print(request)
    responce_put = requests.put(url, json=request)
    print("result = ", responce_put.json())
    assert responce_put.json()['message'] == 'something bad happened'