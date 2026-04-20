""" Import libraries """
import pandas as pd

"""Load DataSet"""
data = pd.read_csv('Data-Analysis-with-Python-Projects\Project-1-Ecommerce\Ecommerce_Purchases_Data.csv')

# print(pd.DataFrame(data.columns))

""" Display Top 10 Rows of DataSet"""
# print(data.head(10))

""" Check Last 10 Rows of Dataset"""
# print(data.tail(10))

""" Check Datatype of Each Column"""
# print(data.dtypes)

""" Check Null Values in DataSet"""
# print(data.isnull().sum())

""" How many Rows and Columns are there in our Dataset"""
# print(data.shape)  # displays (num of rows, num of columns)
# print(len(data.columns))  # number of Columns
# print(len(data))  # displays number of Rows
# print(data.info())

""" Highest and Lowest Perchase price"""
# print(data['Purchase Price'].max())  # prints highest price of Purchase Price column
# print(data['Purchase Price'].min())  # prints lowest price of Purchase Price column

""" Average Perchace Price"""
# print(data['Purchase Price'].mean())

""" How many people hava French 'fr' as there language?"""
# print(len(data[data['Language']=='fr']))
# print(data[data['Language']=='fr'].count())  # another way

""" Job Title contains Engineer"""
# print(data[data['Job'].str.contains('engineer', case=False)])
# print(len(data[data['Job'].str.contains('engineer', case=False)]))   # Length

""" Find Email of the person with the following ip address: 132.207.160.22"""
# print(data.columns)
# print(data[data['IP Address'] == '132.207.160.22']['Email'])

""" How many people have Mastercard as their credit card provider and Made a purchase above 50?"""
# print(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)])
# print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))  # length
# print(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)].count())  # using count

""" Find the Email of the person with the following credit card number: 4664825258997302"""
# print(data[data['Credit Card']== 4664825258997302]['Email'])

""" How many prople purchase during the AM and how many purchase during PM"""
# print(len(data[data['AM or PM']=='AM']),"People purchase during the AM")
# print(len(data[data['AM or PM']=='PM']),"People purchase during the PM")
# print(data['AM or PM'].value_counts()) # using .value_counts()

""" How many people have a credit card that expires in 2020?"""
# print(len(data[data['CC Exp Date'].str.contains('/20')]))