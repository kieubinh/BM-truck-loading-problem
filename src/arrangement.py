import pandas as pd

truck_df = pd.read_csv('data/trucks.csv')
item_df = pd.read_csv('data/items.csv')
input_df = pd.read_csv('data/input.csv')

## check data
print(truck_df)
print(item_df)
print(input_df)

## optimization
total_cost = 0
