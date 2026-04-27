import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('Data-Analysis-with-Python-Projects/Project-3-adults/adult.csv')

""" Display Top 10 Rows of The Dataset"""
# print(df.head(10))

""" Check Last 10 Rows of The Dataset"""
# print(df.tail(10))

""" Find Shape of Our Dataset (Number of Rows And Number of Columns)"""
# print(f"{df.shape[0]} Rows.")
# print(f"{df.shape[1]} Columns.")

""" Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement"""
# print(df.info())

""" Fetch Random Sample From the Dataset (50%)"""
# print(df.sample(frac=0.5))
# print(df.sample(frac=0.5, random_state=100))   # it will give same sequence of random number

""" Check Null Values In The Dataset"""
# print(df.isnull().sum())
# sns.heatmap(df.isnull())
# plt.show()

""" Perform Data Cleaning [ Replace '?' with NaN ]"""
# print(df.tail(20))
# print(df.isin(['?']).sum())
df['workclass']=df['workclass'].replace('?',np.nan)
df['occupation']=df['occupation'].replace('?',np.nan)
df['native-country']=df['native-country'].replace('?',np.nan)
# print(df.isin(['?']).sum())
# print(df.isnull().sum())
# sns.heatmap(df.isnull())
# plt.show()

""" Drop all The Missing Values"""
# df.dropna(how="any",inplace=True)
# print(df.isnull().sum())

""" Check For Duplicate Data and Drop Them"""
# print(df.duplicated().any())
# df=df.drop_duplicates()
# print(df.duplicated().any())