import resources.urls as urls
import Steps.generate_json_steps as genarate_json_steps
import Steps.assert_steps as assert_steps
import Steps.request_steps as request_steps
import json

def test_delete_pet():
    # Отправляем запрос
    response_post = request_steps.request_post(urls.url_pet_post, genarate_json_steps.create_json_pet_all_param())
    # Формируем URL удаления
    url_delete = urls.url_pet_post + "/" + str(response_post.json()['id'])
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем код ответа
    assert_steps.assert_equals_response_value(response_delete, 'code', '200')
    # Делаем запрос с ID удаленного пользователя
    response_get = request_steps.request_get(url_delete)
    # Проверяем, что пользователь удален
    assert_steps.assert_equals_response_value(response_get, 'message', 'Pet not found')


def test_delete_pet_id_negative():
    # Формируем URL c не существующим ID для удаления
    url_delete = urls.url_pet_post + "/" + '99999'
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем, что такой страницы (пользователя) не существует
    assert_steps.assert_page_not_found(response_delete)