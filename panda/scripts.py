import pandas as pd
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)

f= pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(f)

size = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(size)

df = pd.read_csv('dataset.csv')

print(df.to_string())

df1 = pd.read_csv('dataset.csv')

print(df1) 
print('-------------------------------------------')
print(pd.options.display.max_rows)
print('-------------------------------------------')
pd.options.display.max_rows = 10

df = pd.read_csv('dataset.csv')

print(df)
print('-------------------------------------------')
df = pd.read_csv('dataset.csv')

print(df.head(10)) 
print('-------------------------------------------')

print(df.tail(8)) 
print('-------------------------------------------')

print(df.info())

df3 = pd.read_csv('data.csv')

new_df = df3.dropna()
print(new_df) 

df4 = pd.read_csv('data.csv')
df4.dropna(inplace = True)

print(df4)

df5 = pd.read_csv('data.csv')

df5.fillna(130, inplace = True) 
print(df5)

df6 = pd.read_csv('data.csv', header=None)

df6[3].fillna(130, inplace = True) 
print(df6)


input('presione enter para salir')