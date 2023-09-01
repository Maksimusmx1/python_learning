import requests
import resources.urls as urls
import Steps.support_steps as support_steps

def test_post_pet_id_uploadImage():
    request = {}
    request['id'] = 1
    url_post = urls.url_pet_post + str(request['id']) + "/uploadImage"
    print("url_post =", url_post)
    fp = open('send.txt', 'rb')
    files = {'file': fp}
    resp = requests.post(url_post, files=files)
    fp.close()
    print(resp.text)

    responce_get = requests.get(urls.url_pet_get_id(str(request['id'])))
    print("responce =", responce_get.json())
    assert responce_get.json()['id'] == 1
    assert responce_get.json()['status'] == "sold"