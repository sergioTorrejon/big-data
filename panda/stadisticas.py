import pandas as pd
df = pd.read_csv('data.csv', header=None)

x = df[3].mean()

df[3].fillna(x, inplace = True) 
print(df)

df1 = pd.read_csv('data.csv', header=None)

x = df1[3].median()

df1[3].fillna(x, inplace = True) 
print(df1)

df2 = pd.read_csv('data.csv', header=None)

x = df2[3].mode()[0]

df2[3].fillna(x, inplace = True) 
print(df2)
input('presione enter para salir')