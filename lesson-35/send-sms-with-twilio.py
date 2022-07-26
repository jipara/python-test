
####https://www.twilio.com/docs/sms/quickstart/python
import requests

MY_LAT = 41.878113
MY_LNG = -87.629799
api_key = ""


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
# weather = data["weather"]
# code = int(weather[0]["id"])
# if code < 700:
#     print("Bring your umbrella")
# else:
#     print("Today is sunny day")
print(data)
##we have to slice to get particular part of data
weather_slice = data["hourly"][:12]

will_rain: False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain: True

if will_rain:
    print("Bring an umbrella")
