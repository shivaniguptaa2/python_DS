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
print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data_dict["temp"]
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
"""The number of lines reduced plus the formatting as table is wonderful"""

# print(data[data.day =='Monday'])
maxtemp = data["temp"].max()
print(maxtemp)
print(data[data["temp"] == maxtemp])

"""Iterating over a DataFrame gives you column names, not rows."""
"""In dataframe when we are putting the condition then it prints entire row  """

new_dict = {
    "Students": ['Shiv','Durga','Raj'],
    "scores":[20,34,56]
}
print(new_dict)
new_df = pandas.DataFrame(new_dict)
print(new_df)
# new_df.to_csv('CSV/new_csv.csv')
# this to create dataframe from dictionary and converting that to csv file