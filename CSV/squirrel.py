import pandas as pd

sq_data = pd.read_csv("CSV/Squirrel_Data.csv")
# print(sq_data)
data = pd.DataFrame(sq_data)
# print(data["Primary Fur Color"].unique())
# print(data["Primary Fur Color"].value_counts())

data = data.rename(columns={"Primary Fur Color": "Furcolur"})
colour_count = data["Furcolur"].value_counts().reset_index()
colour_count.columns = ["Furcolur","Count"]

print(colour_count)
#    Furcolur  Count
# 0      Gray   2473
# 1  Cinnamon    392
# 2     Black    103

"""To print without the DataFrame index on the left, """
# print(colour_count.to_string(index=False))
# Furcolur  Count
#     Gray   2473
# Cinnamon    392
#    Black    103

colour_count.to_csv("CSV/sq_colors.csv")