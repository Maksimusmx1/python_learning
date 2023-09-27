import Steps.support_steps as support_steps
import Steps.assert_steps as assert_steps
import Steps.request_steps as request_steps
import Steps.generate_json_steps as generate_json_steps
import resources.urls as urls
import pytest

# Тест для загрузки картинки для выбранного ID
@pytest.mark.smoke_API
def test_post_pet_id_uploadImage():
    # Генерируем ID
    id_num = support_steps.generate_random_number_strings(5)
    # Формируем URL запроса для добавления животного
    url_post = urls.url_pet_post
    # Отправляем запрос создание животтного с нужным ID
    response_post = request_steps.request_post(url_post, generate_json_steps.create_json_pet_all_param_id(id_num))
    # Анализируем ответ
    assert_steps.assert_note_none_id(response_post)
    # Формируем URL запроса для загрузки картинки
    url_upload = urls.url_pet_post_uploadimage(id_num)
    # Открываем файл на чтение
    fp = open('files/send.txt', 'rb')
    files = {'file': fp}
    # Отправляем запрос на загрузку картинки
    resp = request_steps.request_post_files(url_upload, files)
    # Проверяем, что загрузка выполнилась
    assert_steps.assert_equals_response_value(resp, "code", 200)
    # Закрываем файл на чтение
    fp.close()