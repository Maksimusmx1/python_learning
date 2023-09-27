import requests
import resources.urls as urls

def test_get_pet():
    response_get = requests.get(urls.url_pet_get_findbystatus("sold"))
    print("response =", response_get.json())
    assert response_get.json()[0]['status'] == "sold"