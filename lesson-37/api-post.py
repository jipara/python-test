import requests
from datetime import datetime


USERNAME = "jipara"
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint: str = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_post_endpoint: str = f"{graph_endpoint}/graph2"

user_params = {
    "token": "",
    "username": "jipara",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_config = {
    "id": "graph2",
    "name": "Studying graph",
    "unit": "commit",
    "type": "float",
    "color": "ajisai",
}

headers = {
   "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
####https://pixe.la/v1/users/jipara/graphs/graph2.html

now = datetime.now()
yesterday = datetime(year=2022, month=7, day=26)
# pixela_config = {
#     "date": now.strftime("%Y%m%d"),
#     "quantity": "3.5",
# }
pixela_config = {
    "date": now.strftime("%Y%m%d"),
    "quantity": input("how many hours did you study?"),
}

###This line of code will create pixel
# response = requests.post(url=pixela_post_endpoint, json=pixela_config, headers=headers)
# print(response.text)
# ###This will update your pixel

update_endpoint: str = f"{pixela_post_endpoint}/20220727"
response = requests.put(url=update_endpoint, json=pixela_config, headers=headers)
print(response.text)
###This line will delete your pixel, user, graph
# response2 = requests.delete(url=pixela_post_endpoint, headers=headers)
# print(response2.text)

