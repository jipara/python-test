with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
dict = data.to_dict()
print(dict["temp"])

series_data = data["temp"].to_list()
print(series_data)

temp_list = len(series_data)
print(temp_list)

average = round(sum(series_data) / temp_list)
print(average)

#row

print(data["temp"].mean())

max_temp = data["temp"].max()
print(max_temp)

print(data.condition)
print(data["condition"])

temp_day = data[data.temp == "Monday"]
monday_condition = temp_day.condition
print(monday_condition)

#DataFrame
data_dict = {
    "students": ["Jipara", "Kamila", "David"],
    "scores": [97, 98, 99]
}

data_from_dict = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
