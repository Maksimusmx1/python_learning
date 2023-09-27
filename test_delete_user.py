import resources.urls as urls
import test_post_user
import Steps.request_steps as request_steps
import Steps.assert_steps as assert_steps

def test_delete_user():
    # Задаем име пользователя
    userName = "Catty"
    # Создадим пользователя для последующего удаления
    test_post_user.test_post_user(userName)
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
