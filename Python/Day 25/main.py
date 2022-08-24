# with open("weather-data.csv",'r') as file:
#     forecast=file.readlines()
#     print(forecast)

# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# Starting
# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# print(type(data))

# Dictionary
# data_dict=data.to_dict()
# print(data_dict)

# List
# temp_list=data["temp"].to_list()
# print(temp_list)

# Mean exercise
# average=data["temp"].mean()
# print(average)

# Max exercise
# max = data["temp"].max()
# print(max)

#Getting hold of columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Get row with condition
# print(data[data.temp == data["temp"].max()])


# Temperature on monday converted to fahren
# monday = data[data.day == "Monday"]
# temperature = int(monday["temp"]) * 1.8 + 32
# print(temperature)

# Creating data frames
# data_dict = {
#     "studens" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# Squirrel census

import pandas

sqrl = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

sqrl_dict = {
    "Fur Color" : [],
    "Count" : [],

}

colors = sqrl["Primary Fur Color"]
for color_table in colors:
    color = str(color_table).lower()
    if color not in sqrl_dict["Fur Color"] and color != "nan":
        sqrl_dict["Fur Color"].append(color)
        total = len(sqrl[sqrl["Primary Fur Color"] == color_table])
        sqrl_dict["Count"].append(total)
print(sqrl_dict)

df = pandas.DataFrame(sqrl_dict)
df.to_csv("Squirrels by color.csv")