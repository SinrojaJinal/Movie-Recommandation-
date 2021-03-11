import pandas as pd

df = pd.read_csv('movie_dataset.csv')

print(df.head(3)['title'])