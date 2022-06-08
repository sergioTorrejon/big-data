import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\cheot\Desktop\big data\panda\dataex.csv')


df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show() 