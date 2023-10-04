import requests
import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps
import Steps.support_steps as support_steps
import Steps.request_steps as request_steps
import pytest

# Тест создания пользователя без указания имени
@pytest.mark.smoke_API
@pytest.mark.user
def test_post_user_runner():
    post_user('')

# Тест создания пользователя с указанием имени
@pytest.mark.smoke_API
@pytest.mark.user
def post_user(userName):
    # Создаем JSON
    request = generate_json_steps.create_json_pet_user(userName)
    # Отправляем запрос
    response_post = requests.post(urls.url_pet_user, json=request)
    # Выводим результат
    print("result = ", response_post.json())
    # Проверяем, что вернулся код ответа 200
    assert_steps.assert_equals_response_value(response_post, 'code', '200')
    # Проверяем, что вернулся тип ответа unknown
    assert_steps.assert_equals_response_value(response_post, 'type', 'unknown')

# Тест получения пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_get_user():
    # Задаем имя пользователя
    userName = support_steps.generate_random_letter_strings(5)
    # Подготавливаем тестового пользователя
    post_user(userName)
    # Формируем URL
    url_get = urls.url_pet_user + "/" + userName
    # Передаем запрос
    response_get = requests.get(url_get)
    # Печатаем ответ
    print("response =", response_get.json())
    # Проверяем статусы ответа
    assert response_get.json()['userStatus'] == 0

# Тест изменения пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_put_user():
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_user_put()
    # Сформмируем URL запроса
    url_put = urls.url_pet_user + "/" + str(request['username'])
    # Выполним PUT
    response_put = request_steps.request_put(url_put, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'code', '200')
    # Передаем запрос
    response_get = request_steps.request_get(url_put)
    # Печатаем ответ
    print("response =", response_get.json())
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_get, 'id', '1')
    assert_steps.assert_equals_response_value(response_get, 'userStatus', '0')

# Тест удаления пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_delete_user():
    # Задаем име пользователя
    userName = support_steps.generate_random_letter_strings(5)
    # Создадим пользователя для последующего удаления
    post_user(userName)
    # Создадим URL для удаления
    url_delete = urls.url_pet_user + "/" + userName
    # Удалим пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверим результат удаления
    assert_steps.assert_equals_response_value(response_delete, 'code', '200')
    # Проверим, что пользователя больше нет
    # Выполним поиск
    response_get = request_steps.request_get(url_delete)
    # Проверим ответ
    assert_steps.assert_page_not_found(response_get)