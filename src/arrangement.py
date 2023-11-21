import pandas as pd

truck_df = pd.read_csv('data/trucks.csv', header=1)
item_df = pd.read_csv('data/items.csv', header=1)
input_df = pd.read_csv('data/input.csv', header=1)

## check data

# print(truck_df)
# print(item_df)
# print(input_df)

## optimize total_cost
total_cost = 0
# input_df.join(item_df)
pd.concat([input_df, item_df], axis=1)
print(input_df)
