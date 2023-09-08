import allure

# Функия проверяет, что ID не NONE
def assert_note_none_id(responce):
    with allure.step("Функия проверяет, что ID не NONE"):
        print(responce)
        assert responce.json()['id'] is not None
        print("PASSED")

# Функия проверяет утверждение, что ID в запросах равны
def assert_equals_responce_ids(first, second):
    with allure.step("Функия проверяет утверждение, что ID в запросах равны"):
        print("first ", first.json())
        print("second ", second.json())
        assert first.json()["id"] == second.json()["id"]
        print("PASSED")

# Функия проверяет, что значение 'field' равно 'value'
def assert_equals_responce_value(responce,field,value):
    with allure.step("Функия проверяет, что значение " + field + " равно " + value):
        print("field ",field)
        print("value ", value)
        print("responce ",responce)
        print("responce json ",responce.json())
        assert responce.json()[field] == value
        print("PASSED")