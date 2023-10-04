import project_root_dir
import Steps.request_steps as request_steps
import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps
import Steps.support_steps as support_steps
import pytest
import allure
import Steps.works_with_file as works_with_file


# Тест для создания нового питомца
@allure.step
@pytest.mark.smoke_API
@pytest.mark.pet
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
    response_post = request_steps.request_post(urls.url_pet_post, request)
    # Анализируем ответ
    assert_steps.assert_note_none_id(response_post)
    # Проверяем через GET что объект действительно создан
    # Формируем URL
    url_get = urls.url_pet_get_id(str(response_post.json()['id']))
    # Отправляем запрос
    response_get = request_steps.request_get(url_get)
    # Сравниваем ID
    assert_steps.assert_equals_response_ids(response_get, response_post)
    # сделаем возврат ответа
    return response_post

# Тест проверки существования животного с заданным id
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet():
    # Создадим животное
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_pet_all_param())
    # Отправляем запрос на проверку животного с id созданного животного
    response_get = request_steps.request_get(urls.url_pet_get_id(str(response_post.json()['id'])))
    # Выводим ответ
    print("response =", response_get.json())
    # Анализируем ответ
    assert_steps.assert_equals_response_value(response_get, "id", str(response_post.json()['id']))
    assert_steps.assert_equals_response_value(response_get, "status", "sold")

# Тест изменения животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_put_pet():
    # Создадим животное с заданным ID
    response_post = test_post_pet(generate_json_steps.create_json_pet_all_param())
    # Анализируем ответ
    assert_steps.assert_note_none_id(response_post)
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(str(response_post.json()['id']))
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'photoUrls', '[]')

# Негативный тест изменения животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_put_pet_id_negative():
    # Задаем ID животного
    id = support_steps.generate_random_letter_strings(5)
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(id)
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'message', 'something bad happened')

# Тест удаления животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_delete_pet():
    # Отправляем запрос
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_pet_all_param())
    # Формируем URL удаления
    url_delete = urls.url_pet_post + "/" + str(response_post.json()['id'])
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем код ответа
    assert_steps.assert_equals_response_value(response_delete, 'code', '200')
    # Делаем запрос с ID удаленного животного
    response_get = request_steps.request_get(url_delete)
    # Проверяем, что животное удалено
    assert_steps.assert_equals_response_value(response_get, 'message', 'Pet not found')

# Негативный тест удаления животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_delete_pet_id_negative():
    # Формируем URL c не существующим ID для удаления
    url_delete = urls.url_pet_post + "/" + support_steps.generate_random_number_strings(5)
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем, что такой страницы (пользователя) не существует
    assert_steps.assert_page_not_found(response_delete)

# тест поиска животного по статусу
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet_by_status():
    # Создадим животное
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_pet_all_param())
    # Анализируем ответ
    assert_steps.assert_note_none_id(response_post)
    # Проверим есть ли животное с нужным статусом
    response_get = request_steps.request_get(urls.url_pet_get_findbystatus("sold"))
    print("response =", response_get.json())
    assert response_get.json()[0]['status'] == "sold"

# Тест для загрузки картинки для выбранного ID
@pytest.mark.smoke_API
@pytest.mark.pet
def test_post_pet_id_uploadImage():
    print("1", project_root_dir.project_root_dir())
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
    files = works_with_file.open_file(project_root_dir.project_root_dir() + '/files/send.txt')
    # Отправляем запрос на загрузку картинки
    resp = request_steps.request_post_files(url_upload, files)
    # Проверяем, что загрузка выполнилась
    assert_steps.assert_equals_response_value(resp, "code", "200")
    # Закрываем файл на чтение
    works_with_file.close_file(files)
