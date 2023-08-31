import pytest
import requests
import json

def test_delete_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = 1
    request['category'] = {}
    request['category']['id'] = 2
    request['category']['name'] = "cats"
    request['name'] = "sberCat"
    request['photoUrls'] = ["photoSberCat"]
 #   request['tags'] = [{'id':3,'name':"sberTag"}]
    request['tags'] = [{}]
    request['tags'][0]['id'] = 3
    request['tags'][0]['name'] = "sberTag"
    request['status'] = "avalible"
    print(request)
    responce_post = requests.post(url, json=request)
    print("result = ", responce_post.json())

    url_delete = url + "/" + str(responce_post.json()['id'])
    print("url_delete", url_delete)

    responce_delete = requests.delete(url_delete)
    print("result_delete =", responce_delete.json())

    assert responce_delete.json()['code'] == 200

    url_get = url + "/" + str(responce_post.json()['id'])
    print ("url_get ", url_get )

    responce_get = requests.get(url_get)
    print("result_get = ", responce_get.json())
    assert responce_get.json()['message'] == "Pet not found"


def test_delete_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = 1
    request['category'] = {}
    request['category']['id'] = 2
    request['category']['name'] = "cats"
    request['name'] = "sberCat"
    request['photoUrls'] = ["photoSberCat"]
 #   request['tags'] = [{'id':3,'name':"sberTag"}]
    request['tags'] = [{}]
    request['tags'][0]['id'] = 3
    request['tags'][0]['name'] = "sberTag"
    request['status'] = "avalible"
    print(request)
    responce_post = requests.post(url, json=request)
    print("result = ", responce_post.json())

    url_delete = url + "/" + "12345"
    print("url_delete", url_delete)

    responce_delete = requests.delete(url_delete)
    print("result_delete =", responce_delete)
    assert str(responce_delete).__contains__("404")