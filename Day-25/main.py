# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# #
# # # data_dict = data.to_dict()
# # # print(data_dict)
# # #
# # # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # #
# # # print(data["temp"].max())
# # #
# # # print(data.condition)
# #
# # # get data in row
# # # print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# #
# #
# # # Create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")
import pandas
data = pandas.read_csv("Squirrel_Data.csv")
fur_color_count = data["Primary Fur Color"].value_counts()

grey = fur_color_count.Gray
red = fur_color_count.Cinnamon
black = fur_color_count.Black

fur_dict = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [grey, red, black]
}

pandas.DataFrame(fur_dict).to_csv("squirrel_count")