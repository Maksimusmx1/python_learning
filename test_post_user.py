import requests
import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps

def test_post_user_runner():
    test_post_user('')

def test_post_user(userName):
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


