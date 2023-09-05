import requests

# Отправка запросов и получение ответа для метода POST
# URL - эндпоинт
# request - JSON
def request_post(url, request):
    response = requests.post(url, json=request, verify=False)
    return response

# Отправка запросов и получение ответа для метода POST передача файла
# URL - эндпоинт
# request - файл
def request_post_files(url, files):
    response = requests.post(url, files=files, verify=False)
    return response

# Отправка запросов и получение ответа для метода GET
# URL - эндпоинт
def request_get(url):
    response = requests.get(url, verify=False)
    return response