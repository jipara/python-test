import requests
from datetime import datetime
MY_LAT = 41.878113
MY_LNG = -87.629799
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code != 0:
# #     raise Exception("Bad response from ISS API")
# response.raise_for_status()
#
# data = response.json()["iss_position"]["longitude"]
#
# ##OR
#
# data2 = response.json()
#
# longitude = data2["iss_position"]["longitude"]
# latitude = data2["iss_position"]["latitude"]
#
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
#print(data)
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
time_now = datetime.now()
# print(time_now.hour)
# print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":"))
# #actual hour
# print(sunrise.split("T")[1].split(":")[0])
# #find just hour in one line
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
