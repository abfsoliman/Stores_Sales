# imports and load data
import pandas as pd
% matplotlib inline
df=pd.read_csv('store_data.csv')

# explore data
df.hist(figsize=(8,8));

# sales for the last month
df.tail(4).plot(kind='bar',figsize=(8,8));

# average sales
df.mean().plot(kind='bar',figsize=(8,8));

# sales for the week of March 13th, 2016
df[df['week']=='2016-03-13'].plot(kind='bar',figsize=(8,8));

# share of sales for the latest 3-month periods
df.iloc[188:,1:].sum().plot.pie(y='Sales',x='Stores',autopct='%1.1f%%',shadow=True,figsize=(8,8),explode=(0,0,0.2,0,0));
