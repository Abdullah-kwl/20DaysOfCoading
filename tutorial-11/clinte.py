import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(url=URL, data=json.dumps(data))
    return resp.json()

# data = get_data(id=2)
# print(data)
# data = get_data()
# for i in data:
#     print(i)

def post_data(data):
    data = json.dumps(data)
    resp = requests.post(url=URL, data=data)
    return resp.json()

# data = {
#     'name': 'Rahan',
#     'roll': 107,
#     'city': 'Multan'
# }
# resp = post_data(data)
# print(resp)

def update_data(data):
    data = json.dumps(data)
    resp = requests.put(url=URL, data=data)
    return resp.json()

# data = {
#     'id': 7,
#     'city': 'Karachi'
# }
# resp = update_data(data)
# print(resp)

def delete_data(id):
    data = {'id': id}
    resp = requests.delete(url=URL, data=json.dumps(data))
    return resp.json()

# resp = delete_data(id=7)
# print(resp)