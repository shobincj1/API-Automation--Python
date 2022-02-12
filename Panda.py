import pandas as pd
df= pd.read_csv('Utilities/pokemon_data.csv')
print(df)
print(df.head())
print(df.tail())
print(type(df))
print(df.columns)
print(type(df.columns))