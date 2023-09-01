import requests
import resources.urls as urls

def test_delete_user():
    userName = "Catty"
    url_delete = urls.url_pet_user + "/" + userName
    print("URL_delete", url_delete)
    responce_delete = requests.delete(url_delete)
    print("responce =", responce_delete.json())

    responce_get = requests.get(url_delete)
    print("responce =", responce_get.json())
