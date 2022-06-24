import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]

gray = (len(data[color == "Gray"]))
red = (len(data[color == "Cinnamon"]))
black = (len(data[color == "Black"]))


dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}


total = pandas.DataFrame(dict)
total_csv = total.to_csv("total_num.csv")
print(total_csv)



#print(type(data["Primary Fur Color"]))
