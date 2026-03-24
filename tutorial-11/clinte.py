import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(url=URL, data=json.dumps(data))
    return resp.json()

data = get_data(id=2)
print(data)
# data = get_data()
# for i in data:
#     print(i)