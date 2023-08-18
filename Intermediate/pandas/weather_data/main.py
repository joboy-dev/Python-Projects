# USING CSV PACKAGE
# import csv

# with open('Intermediate/pandas/weather_data/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
    
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#     print(temperatures)
    
#     # for row in data:
#     #     print(row)


# USING PANDAS PACKAGE
import pandas as pd

# reading csv data
data = pd.read_csv('Intermediate/pandas/weather_data/weather_data.csv')

# accessing portions of data
# print(data['temp'])

# converting data to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# converting a series to a list
# temp = data['temp']
# temp_list = temp.to_list()
# print(temp_list)

# Average temperature
# print(sum(temp_list) / len(temp_list))
# OR
# print(data['temp'].mean())

# Max value
# print(data['temp'].max())
# Min value
# print(data['temp'].min())

# Another way of accessing data in a dataframe
# print(data.temp)

# getting condition data in rows
monday = data[data.day == 'Monday']
print(monday)

print(data[data.temp == data.temp.max()])

print(monday.condition)

monday_temp = int(monday.temp)
# monday temp in fahrenheit
print((monday_temp * (9/5)) + 32)


# Creating a dataframe from scratch
data_dict = {
    'students': ['Anne', 'Joe', 'Sam'],
    'score': [76, 88, 86]
}

df = pd.DataFrame(data=data_dict)
print(df)

# converting dataframe into a csv file
df.to_csv('Intermediate/pandas/weather_data/new_data.csv')