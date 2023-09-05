import requests
import resources.urls as urls

def test_get_user():
    userName = "Catty"
    url_get = urls.url_pet_user + "/" + userName
    responce_get = requests.get(url_get)
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['userStatus'] == 0

