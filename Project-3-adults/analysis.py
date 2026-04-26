import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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