import requests
import resources.urls as urls

def test_get_pet():
    responce_get = requests.get(urls.url_pet_get_findbystatus("sold"))
    print("responce =", responce_get.json())
    assert responce_get.json()[0]['status'] == "sold"