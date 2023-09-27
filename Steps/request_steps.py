import requests
import allure
import json

# Отправка запросов и получение ответа для метода POST
# URL - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        response = requests.post(url, json=request, verify=False)
        # переводим тип 'dict' в набор байт для прикрепления
        request_encode = json.dumps(request, indent=2, sort_keys=True).encode('utf-8')
        response_encode = json.dumps(response.json(), indent=2, sort_keys=True).encode('utf-8')
        # выводим в отчет тело запроса
        allure.attach(request_encode, 'REQUEST_BODY', allure.attachment_type.JSON)
        # выводим в отчет тело ответа
        allure.attach(response_encode, 'RESPONSE_BODY', allure.attachment_type.JSON)
        return response

# Отправка запросов и получение ответа для метода POST передача файла
# URL - эндпоинт
# request - файл
def request_post_files(url, files):
    with allure.step("Отправка запросов и получение ответа для метода POST передача файла"):
        response = requests.post(url, files=files, verify=False)
        return response

# Отправка запросов и получение ответа для метода GET
# URL - эндпоинт
def request_get(url):
    with allure.step("Отправка запросов и получение ответа для метода GET"):
        response = requests.get(url, verify=False)
        return response

# Удаление пользователя
# URL - эндпоинт
def delete_user(url):
    with allure.step("Удаление пользователя"):
        response = requests.delete(url)
        return response

# Изменение данных методом PUT
# URL - эндпоинт
def request_put(url, request):
    with allure.step("Изменение данных методом PUT"):
        response = requests.put(url, json=request, verify=False)
        # переводим тип 'dict' в набор байт для прикрепления
        request_encode = json.dumps(request, indent=2, sort_keys=True).encode('utf-8')
        response_encode = json.dumps(response.json(), indent=2, sort_keys=True).encode('utf-8')
        # выводим в отчет тело запроса
        allure.attach(request_encode, 'REQUEST_BODY', allure.attachment_type.JSON)
        # выводим в отчет тело ответа
        allure.attach(response_encode, 'RESPONSE_BODY', allure.attachment_type.JSON)
        return response