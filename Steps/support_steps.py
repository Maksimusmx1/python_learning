import random
import string
import allure

#функция генерирует строку чисел 0-9 заданной длинны
def generate_random_number_strings(length):
    with allure.step("функция генерирует строку чисел 0-9 заданной длинны"):
        result = ""
        for i in range(0, length):
            result += str(random.randint(0,9))
        return result

#функция генерирует текстовую строку заданной длинны
def generate_random_letter_strings(length):
    with allure.step("функция генерирует текстовую строку заданной длинны"):
        result = ""
        for i in range(0, length):
            result += str(random.choice(string.ascii_letters[random.randint(0,5)]))
        return result
