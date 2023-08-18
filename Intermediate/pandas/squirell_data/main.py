import pandas as pd

data = pd.read_csv('Intermediate/pandas/squirell_data/squirell_data.csv')
# print(data)

gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
# print(gray_squirrel_count)
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# print(cinnamon_squirrel_count)
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
# print(black_squirrel_count)

color_count_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}

print(color_count_dict)

df = pd.DataFrame(data=color_count_dict)

# print(df)
df.to_csv('Intermediate/pandas/squirell_data/squirell_count.csv')