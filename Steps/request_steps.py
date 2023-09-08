import requests
import allure
import json

# Отправка запросов и получение ответа для метода POST
# URL - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        response = requests.post(url, json=request, verify=False)
        # переводим тип 'dict' от request в набор байт для прикрепления
        request_encode = json.dumps(request, indent=2).encode('utf-8')
        allure.attach(request_encode, 'REQUEST', allure.attachment_type.JSON)
        allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
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