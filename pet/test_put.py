import test_post
import Steps.generate_json_steps as generate_json_steps
import Steps.request_steps as request_steps
import resources.urls as urls
import Steps.assert_steps as assert_steps

def test_put_pet():
    # Задаем ID животного
    id = 123
    # Создадим животное с заданным ID
    response_post = test_post.test_post_pet(generate_json_steps.create_json_pet_all_param_id(id))
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(id)
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'photoUrls', '[]')

def test_put_pet_id_negative():
    # Задаем ID животного
    id = 'name'
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(id)
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'message', 'something bad happened')
