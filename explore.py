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
