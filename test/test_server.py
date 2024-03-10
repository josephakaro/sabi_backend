import requests

BASE = "http://127.0.0.1:8000/"
prompt = "/Who are you?"

message = requests.get(BASE + '/chat' + prompt)
print(message.json())
