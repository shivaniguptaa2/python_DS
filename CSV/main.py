# with open("CSV/weather_data.csv") as file:
#     rows = file.readlines()
#     print(rows)

"""We can use this to read the data from CSV """

# import csv

# with open(r"e:\python_DS\CSV\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#         # print(row)
#     print(temperature)

"""Here it is good number of lines, but pandas can be used very efficiently to handle csv data"""

import pandas

data = pandas.read_csv("CSV/weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data_dict["temp"]
print(sum(temp_list)/len(temp_list))
print(data_dict["temp"].mean())
"""The number of lines reduced plus the formatting as table is wonderful"""