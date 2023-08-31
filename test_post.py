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
    request['photoUrls'] = ["photoSberCat"]
  #  request['tags'] = [{'id':3,'name':"sberTag"}]
    request['tags'] = [{}]
    request['tags'][0]['id'] = 3
    request['tags'][0]['name'] = "sberTag"
    request['status'] = "sold"
    print(request)
    responce_post = requests.post(url, json=request)
    print("result = ", responce_post.json())
    assert responce_post.json()['id'] is not None

    url_get = url + "/" + str(responce_post.json()['id'])
    print ("url_get ", url_get )

    responce_get = requests.get(url_get)
    print("result_get = ", responce_get.json())
    assert responce_get.json()['id'] == responce_post.json()['id']