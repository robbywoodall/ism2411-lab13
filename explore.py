# --- Reflection 1 ---
# Boolean filters check each line to see if data meets a certain condition (True or False)
# --- Reflection 2 ---
# Single brackets return a serial, which is one dimensional. Double brackets return
# a DataFrame which is 2 dimensional. This matters when performing functions that expect
# a certain structure.
# --- Reflection 3 ---
# Pandas will allow you to create something that you can use repeatedly with consistent
# results. It will save you hours of time!
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
south = df[df['region'] == 'South']
print(len(south))
print(south.head())
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())
print(df['region'].unique())
print(df['region'].value_counts())
narrow_df = df[['region', 'product', 'revenue']]
print(narrow_df.shape)
df.to_csv("data/explored.csv", index=False)
print("\nSaved to data/explored.csv")