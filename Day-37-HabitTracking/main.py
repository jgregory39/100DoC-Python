import requests
from configparser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read('config.ini')
pixela_token = config['PIXELA']['PIXELA_TOKEN']
pixela_user = config['PIXELA']['PIXELA_USER']
graph_id = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": pixela_token,
    "username": pixela_user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_user}/graphs"

graph_config = {
    'id': graph_id,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': pixela_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{graph_id}"

date = datetime(year=2022, month=10, day=10).strftime('%Y%m%d')

pixel_body = {
    'date': date,
    'quantity': '8.541',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_body, headers=headers)
# print(response.text)

pixel_edit_endpoint = f"{pixel_creation_endpoint}/{date}"

pixel_edit_body = {
    'quantity': '5.15'
}

# response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_body, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_edit_endpoint, headers=headers)
print(response.text)
