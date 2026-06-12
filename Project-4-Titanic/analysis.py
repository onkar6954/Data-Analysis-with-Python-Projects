import pandas as pd

data = pd.read_csv('titanic.csv')

# print(data)

""" Display Top 5 Rows of The Dataset """
# print(data.head())

""" Check the Last 3 Rows of The Dataset """
print(data.tail(3))