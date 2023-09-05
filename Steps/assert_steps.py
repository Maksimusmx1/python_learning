# Функия проверяет, что ID не NONE
def assert_note_none_id(responce):
    print(responce)
    assert responce.json()['id'] is not None
    print("PASSED")

# Функия проверяет утверждение, что ID в запросах равны
def assert_equals_responce_ids(first, second):
    print("first", first.json())
    print("second", second.json())
    assert first.json()["id"] == second.json()["id"]
    print("PASSED")