import requests
import json


endpoint = "http://localhost:8000/api/dog-list"


data = {
    "breed": "German Shepherd",
    "name": "local",
    "age": 14,
    "gender": "M",
    "color": "black",
    "favorite_food": "api",
    "favorite_toy": "apis"
}

auth = {"username": "Admin", "password": "12345"}

resp = requests.post(endpoint, data=data, auth=auth)
print(resp.json())