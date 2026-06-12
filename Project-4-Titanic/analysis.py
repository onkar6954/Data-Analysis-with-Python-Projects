import pandas as pd

data = pd.read_csv('titanic.csv')

# print(data)

""" Display Top 5 Rows of The Dataset """
# print(data.head())

""" Check the Last 3 Rows of The Dataset """
# print(data.tail(3))

""" Find Shape of Our Dataset (Number of Rows & Number of Columns) """
# print("Number of Rows:",data.shape[0])
# print("Number of Columns:",data.shape[1])

""" Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement """
# print(data.info())

""" Get Overall Statistics About The Dataframe """
print(data.describe())