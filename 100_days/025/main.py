# with open("weather_data.csv") as f:
#     data = f.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as f:
#      data = csv.reader(f)
#      temperatures = []
#      for row in data:
#          if row[1] != 'temp':
#              temperatures.append(int(row[1]))
#
# print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
# print(temp_list)
# avg_temp = data['temp'].mean()
# print(avg_temp)
#
# max_temp = data['temp'].max()
# print(max_temp)
#
# print(data[data.day == 'Monday'])
#
# print(data[data.temp == max_temp])
# print(f"In Far.: {data[data.day == 'Monday'].temp[0]*9/5+32}")

import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251026.csv')
print(data.head())

grouped_data = data.groupby('Primary Fur Color')['Primary Fur Color'].count()
print(grouped_data)
grouped_data.to_csv('sq_by_colors.csv')