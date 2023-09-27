import pytest
import requests
import json
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.request_steps as request_steps
import Steps.assert_steps as assert_steps

# Тест проверки существования животного с заданным id
def test_get_pet():
    # Отправляем запрос на проверку животного с id=1
    response_get = request_steps.request_get(urls.url_pet_get_id("1"))
    # Выводим ответ
    print("response =", response_get.json())
    # Анализируем ответ
    assert_steps.assert_equals_response_value(response_get, "id", "1")
    assert_steps.assert_equals_response_value(response_get, "status", "sold")

# Тест проверки, что животное с шв =12345 не существовует
def test_get_pet_id_negative():
    # Отправляем запрос на проверку животного с id=12345
    response_get = request_steps.request_get(urls.url_pet_get_id("12345"))
    # Выводим ответ
    print("response =", response_get.json())
    # Анализируем ответ
    assert_steps.assert_equals_response_value(response_get, "message", "Pet not found")