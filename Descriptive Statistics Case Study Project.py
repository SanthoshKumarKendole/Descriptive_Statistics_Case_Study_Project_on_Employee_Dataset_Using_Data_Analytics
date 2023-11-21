# Descriptive Statistics Case Study Project on Employee Data

# Task-1 Load and Study the data

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as pt

data=pd.read_csv("C:/Users/KENDOLESANTHOSHKUMAR/Downloads/Employee Info.csv")

data.head()

data.index

data.columns

data.describe()

data.info()

# Task-2 Visualize the distributions of ratings and Compensations

# Relationship between Age and Salary using Scatterplot

pt.figure(figsize=(8,4))
sb.scatterplot(data=data,x='age',y='salary',color='b',edgecolor='yellow',alpha=.8)
pt.title("Scatterplot between Age V/S Salary")
pt.xlabel("Employee Age")
pt.ylabel("Employee Salary")
pt.show()

# Relationship between Healthy Eating vs Active Lifestyle

pt.figure(figsize=(8,4))
sb.scatterplot(data=data,x='healthy_eating',y='active_lifestyle',color='g',edgecolor='red',alpha=.8)
pt.title("Scatterplot between Healthy Eating V/S Active Lifestyle")
pt.xlabel("Healthy Eating")
pt.ylabel('Active Lifestyle')
pt.show()

# Relationship between Healthy Eating vs Salary

pt.figure(figsize=(8,4))
sb.scatterplot(data=data,x='healthy_eating',y='salary',color='red',edgecolor='black',alpha=.8)
pt.title("Scatterplot between Healthy Eating V/S Salary")
pt.xlabel("Healthy Eating")
pt.ylabel('Employee Salary')
pt.show()

# Countplot for the Blood Groups of Employee

pt.figure(figsize=(8,4))
sb.countplot(data=data,x='groups',alpha=.8)
pt.xlabel("Blood Groups of Employee")
pt.ylabel("Count")
pt.show()

# Perform a histogram on Employee Salary

pt.figure(figsize=(8,4))
sb.histplot(data=data,x='salary',color='green',edgecolor='green',bins=6)
pt.xlabel("Employee Salary")
pt.ylabel("Count")
pt.show()

# Task-3 Subset the data based on the Thresholds

# Employee with Healthy _Eating is greather than 8

x=data[data['healthy_eating']>8]

x

# Employee Salary is Less than 1000

sal=data[data['salary']<1000]

sal

# Relationship between the both healthy eating and salary

both=data[(data['healthy_eating']>8) & (data['salary']<1000)]

both

# Conclusion
# Finally only one employee seemingly facing a discrepency in salary as well as compared to healthy _eating who is having id=26.

