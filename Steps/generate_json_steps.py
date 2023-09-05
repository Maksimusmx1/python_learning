import Steps.support_steps as support_steps

# Создаем JSON для метода POST /pet с обязательными параметрами
def create_json_pet_required_param():
    request = {}
    request['name'] = support_steps.generate_random_letter_strings(6)
    request['category'] = {}
    request['category']['name'] = support_steps.generate_random_letter_strings(6)
    request['photoUrls'] = [support_steps.generate_random_letter_strings(6)]
    print("request =", request)
    return request

# Создаем JSON для метода POST /pet со всеми параметрами
def create_json_pet_all_param():
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