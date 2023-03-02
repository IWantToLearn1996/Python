import csv
import pandas

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         for column in data:
#             temperature.append(int(column[1]))
#         print(temperature)


# data = pandas.read_csv("weather_data.csv")

# temperature = data["temp"]
# print(temperature)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# Data in Columns
# print(data["condition"])
# print(data.condition)

# Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday["temp"])
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

data_dict = {
    "students" : ["Nick", "Vas", "Mario"],
    "scores" : [77, 88, 33]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("created_data.csv")