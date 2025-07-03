# with open("CSV/weather_data.csv") as file:
#     rows = file.readlines()
#     print(rows)

"""We can use this to read the data from CSV """

# import csv

# with open(r"e:\python_DS\CSV\weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data) # It will return the object not the content
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#         # print(row)
#     print(temperature)

"""The csv.reader() function in your code is creating a reader object that will iterate over lines in your CSV file.
It does not read all the data at once—instead, it prepares to read the file row by row.
To actually access the data, you need to loop over data"""

"""Here it is good number of lines, but pandas can be used very efficiently to handle csv data"""

import pandas

data = pandas.read_csv("CSV/weather_data.csv")
# print(data)
# print(data["temp"])

"""A DataFrame is a two-dimensional, tabular data structure provided by the pandas library in Python.
It is similar to a spreadsheet or a SQL table, with rows and columns."""

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data_dict["temp"]
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
"""The number of lines reduced plus the formatting as table is wonderful"""

# print(data[data.day =='Monday'])
# maxtemp = data["temp"].max()
# print(maxtemp)
# print(data[data["temp"] == maxtemp])

"""Iterating over a DataFrame gives you column names, not rows."""
"""In dataframe when we are putting the condition then it prints entire row  """

new_dict = {
    "Students": ['Shivani','Durgam','Rajesh'],
    "scores":[20,34,56]
}
print(new_dict)
new_df = pandas.DataFrame(new_dict)
print(new_df)
new_df.to_csv('CSV/new_csv.csv')
# this to create dataframe from dictionary and converting that to csv file