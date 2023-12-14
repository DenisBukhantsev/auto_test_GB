import requests
import yaml

with open("config.yaml", "r", encoding="utf8") as f:
    data = yaml.safe_load(f)

def get_login():
    path = data["path"]
    post = requests.post(url=path, data={'username': data["username"], "password": data["password"]})
    if post.status_code == 200:
        return post.json()["token"]

def get_post(token):

    path = "https://test-stand.gb.ru/api/posts"
    get = requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()

def test_post_create(token, get_description):


    res = requests.post(url=data['create_post'], headers={'X-Auth-Token': token},
           data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    assert str(res) == '<Response [200]>', 'post_create FAIL'


def test_check_post_create(token, get_description):

    result = requests.get(url=data['chek_post_adress'], headers={'X-Auth-Token': token}).json()['data']
    print(result)
    list_description = [i['description'] for i in result]
    print(list_description)
    assert get_description in list_description, 'check_post_create FAIL'



if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    #test_post_create(token)
    #test_check_post_create(token)



