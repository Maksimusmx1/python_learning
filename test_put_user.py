import requests
import resources.urls as urls
import test_post_user

def test_put_user():
    # Подготавливаем тестового пользователя
    test_post_user.test_post_user()
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
    url_put = urls.url_pet_user + "/" + str(request['username'])
    print("url_put =",url_put)
    responce_post = requests.put(url_put, json=request)
    print("result = ", responce_post.json())

    responce_get = requests.get(url_put)
    print("responce =", responce_get.json())