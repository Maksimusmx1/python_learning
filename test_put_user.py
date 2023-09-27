import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.request_steps as request_steps
import Steps.assert_steps as assert_steps

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