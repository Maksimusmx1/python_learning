import requests
import resources.urls as urls
import test_post_user

def test_get_user():
    # Задаем имя пользователя
    userName = "Catty"
    # Подготавливаем тестового пользователя
    test_post_user.test_post_user(userName)
    # Формируем URL
    url_get = urls.url_pet_user + "/" + userName
    # Передаем запрос
    response_get = requests.get(url_get)
    # Печатаем ответ
    print("response =", response_get.json())
    # Проверяем статусы ответа
    assert response_get.json()['userStatus'] == 0

