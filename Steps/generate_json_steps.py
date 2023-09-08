import Steps.support_steps as support_steps
import allure

# Создаем JSON для метода POST /pet с обязательными параметрами
def create_json_pet_required_param():
    with allure.step("Создаем JSON для метода POST /pet с обязательными параметрами"):
        request = {}
        request['name'] = support_steps.generate_random_letter_strings(6)
        request['category'] = {}
        request['category']['name'] = support_steps.generate_random_letter_strings(6)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(6)]
        print("request =", request)
        return request

# Создаем JSON для метода POST /pet со всеми параметрами c генерацией ID
def create_json_pet_all_param():
    with allure.step("Создаем JSON для метода POST /pet со всеми параметрами c генерацией ID"):
        request = {}
        request['id'] = support_steps.generate_random_number_strings(7)
        request['category'] = {}
        request['category']['id'] = support_steps.generate_random_number_strings(7)
        request['category']['name'] = support_steps.generate_random_letter_strings(7)
        request['name'] = support_steps.generate_random_letter_strings(7)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(7)]
        request['tags'] = [{}]
        request['tags'][0]['id'] = support_steps.generate_random_number_strings(7)
        request['tags'][0]['name'] = support_steps.generate_random_letter_strings(7)
        request['status'] = "sold"
        print("request =", request)
        return request

# Создаем JSON для метода POST /pet со всеми параметрами для заданного ID
def create_json_pet_all_param_id(id_num):
    with allure.step("Создаем JSON для метода POST /pet со всеми параметрами для заданного ID"):
        request = {}
        request['id'] = id_num
        request['category'] = {}
        request['category']['id'] = support_steps.generate_random_number_strings(7)
        request['category']['name'] = support_steps.generate_random_letter_strings(7)
        request['name'] = support_steps.generate_random_letter_strings(7)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(7)]
        request['tags'] = [{}]
        request['tags'][0]['id'] = support_steps.generate_random_number_strings(7)
        request['tags'][0]['name'] = support_steps.generate_random_letter_strings(7)
        request['status'] = "sold"
        print("request =", request)
        return request