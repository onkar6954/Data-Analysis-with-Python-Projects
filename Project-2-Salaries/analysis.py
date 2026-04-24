""" Import Libraries"""
import pandas as pd

""" Load DataSet"""
df = pd.read_csv('Data-Analysis-with-Python-Projects\Project-2-Salaries\Salaries.csv')

""" Display Top 10 rows of dataset"""
# print(df.head(10))

""" Display Last 10 rows of dataset"""
# print(df.tail(10))

""" Find Shape of Our Dataset (Number of Rows And Number of Columns)"""
# print(f"Number of Rows are {df.shape[0]} and Number of Columns are {df.shape[1]}")

""" Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement"""
# print(df.info())

""" Check Null Values In The Dataset"""
# print(df.isnull().sum())

""" Drop ID, Notes, Agency, and Status Columns"""
# print(pd.DataFrame(df.columns))
# df = df.drop(['Id', 'Notes', 'Agency', 'Status'], axis=1)
# print(pd.DataFrame(df.columns))

""" Get Overall Statistics About The Dataframe"""
# print(df.describe())

""" Find Occurrence of The Employee Names  (Top 5)"""
# print(df['EmployeeName'].value_counts().head())

""" Find The Number of Unique Job Titles"""
# print(df.columns)
# print(df['JobTitle'].nunique())

""" Total Number of Job Titles Contain Captain"""
# print(df['JobTitle'])
# print(df[df['JobTitle'].str.contains('CAPTAIN')])

""" Display All the Employee Names From Fire Department"""
# print(df[df['JobTitle'].str.contains('FIRE DEPARTMENT')]['EmployeeName'])