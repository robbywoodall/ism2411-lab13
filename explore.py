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