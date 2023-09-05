import Steps.request_steps as request_steps
import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps
import pytest

# Тест для создания нового питомца
@pytest.mark.smoke_API
@pytest.mark.parametrize('type',
                         [
                             generate_json_steps.create_json_pet_required_param(),
                             generate_json_steps.create_json_pet_all_param()
                         ],
                         ids=["required_param", "all_param"]
                         )
def test_post_pet(type):
    # Создаем JSON
    request = type
    # Отправляем запрос
    responce_post = request_steps.request_post(urls.url_pet_post, request)
    # Анализируем ответ
    assert_steps.assert_note_none_id(responce_post)
    # Проверяем через GET что объект действительно создан
    # Формируем URL
    url_get = urls.url_pet_get_id(str(responce_post.json()['id']))
    # Отправляем запрос
    responce_get = request_steps.request_get(url_get)
    # Сравниваем ID
    assert_steps.assert_equals_responce_ids(responce_get, responce_post)