import requests

# Отправка запросов и получение ответа для метода POST
# URL - эндпоинт
# request - JSON
def request_post(url, request):
    response = requests.post(url, json=request)
    return response

# Отправка запросов и получение ответа для метода GET
# URL - эндпоинт
def request_get(url):
    response = requests.get(url)
    return response