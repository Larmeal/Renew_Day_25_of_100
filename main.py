# version csv 

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         number = row[1]
#         if number != "temp":
#             temperature.append(int(number))

#     print(temperature)

# version pandas

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_temp_list = data["temp"].to_list()

# หาค่าเฉลี่ย
# answer = 0
# for n in data_temp_list:
#     answer += n

# result = answer / len(data_temp_list)

# print(result)

# หาค่า maximum
# maximum_temp = 0
# for n in data_temp_list:
#     if n > maximum_temp:
#         maximum_temp = n

# print(maximum_temp)

# print(row) ที่มา temp สูงที่สุด

# print(data[data.temp == data.temp.max()])

# เปลี่ยนอุณหภูมิเป็น Fahrenheit

# monday = data[data.day == "Monday"]
# temperature_Celsius = monday.temp
# temperature_Fahrenheit = (temperature_Celsius * 9 / 5) + 32 
# print(temperature_Fahrenheit)

# การบันทึก DataFrame

# data_dict = {
#     "students": ["Ammy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

# หาปริมาณสีของกระรอก

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = 0
gray = 0
cinnamon = 0

for n in data["Primary Fur Color"]:
    if n == "Black":
        black += 1
    elif n == "Gray":
        gray += 1
    else:
        cinnamon += 1

squirrel_colors = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

record_squirrel = pandas.DataFrame(squirrel_colors)
record_squirrel.to_csv("squirrel_count")