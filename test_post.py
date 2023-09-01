import pytest
import requests
import json
import resources.urls as urls
import Steps.support_steps as support_steps

def test_post_pet():
    request = {}
    request['id'] = 1
    request['category'] = {}
    request['category']['id'] = 2
    request['category']['name'] = "cats"
    request['name'] = support_steps.generate_random_letter_strings(7)
    request['photoUrls'] = ["photoSberCat"]
    request['tags'] = [{}]
    request['tags'][0]['id'] = 3
    request['tags'][0]['name'] = "sberTag"
    request['status'] = "sold"
    print(request)
    responce_post = requests.post(urls.url_pet_post, json=request)
    print("result = ", responce_post.json())
    assert responce_post.json()['id'] is not None

    url_get = urls.url_pet_get_id(str(responce_post.json()['id']))
    print("url_get ", url_get)

    responce_get = requests.get(url_get)
    print("result_get = ", responce_get.json())
    assert responce_get.json()['id'] == responce_post.json()['id']