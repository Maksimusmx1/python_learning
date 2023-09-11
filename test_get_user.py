import requests
import resources.urls as urls
import test_post_user

def test_get_user():
    # Подготавливаем тестового пользователя
    test_post_user.test_post_user()
    # Задаем имя пользователя
    userName = "Catty"
    # Формируем URL
    url_get = urls.url_pet_user + "/" + userName
    # Передаем запрос
    responce_get = requests.get(url_get)
    # Печатаем ответ
    print("responce =", responce_get.json())
    # Проверяем статусы ответа
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['userStatus'] == 0

