import pandas as pd
import os

# merging all the data into a single file
# df=pd.read_csv('.../PythonPractice/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv')
files=[file for file in os.listdir('.../PythonPractice/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]

all_months_data=pd.DataFrame()

for file in files:
    df=pd.read_csv('.../Documents/PythonPractice/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False)
all_months_data.head()


all_data=pd.read_csv("all_data.csv")
all_data.head()


# argument the data with extra col
# adding the month

all_data['Month']= all_data['Order Date'].str[0:2]
# define the month type
# all_data['Month']=all_data['Month'].astype('int32')
# not working coz of the messy data has things other than date
all_data['Month'].head(500)

# drop rows of NAN
nan_df= all_data[all_data.isna().any(axis=1)]
all_data=all_data.dropna(how='all')
all_data
all_data['Month'].unique()
all_data=all_data[all_data['Month']!='Or']

all_data['Month']=all_data['Month'].astype('int32')


# sales value
# collect type calculation first
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
all_data.head()

results=all_data.groupby('Month').sum()

import matplotlib.pyplot as plt

# plot monthly sales
months=range(1,13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD')
plt.xlabel('Month Number')
plt.show()

# demographic
# extract the city
# use apply()
def get_city(address):
    return  address.split(',')[1]


all_data.head()
all_data['City'].unique()

# it can also be trouble if two city named the same, but actually two places
all_data['City']=all_data['Purchase Address'].apply(lambda x: x.split(',')[1])


# apply lambda x , can apply other functions as well
all_data['City']=all_data['Purchase Address'].apply(lambda x: get_city(x))


# fix the address by state
def get_state(address):
    return  address.split(',')[2].split(' ')[1]

# State = all_data['Purchase Address'].apply(lambda x: get_state(x))
# State

# apply lambda x , can apply other functions as well
# https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13a1ea037f7
all_data['City']=all_data['Purchase Address'].apply(lambda x: get_city(x)+ ' '+ get_state(x))
# or either way is fine, f string
all_data['City']=all_data['Purchase Address'].apply(lambda x: f"{get_city(x)}({get_state(x)})")
all_data.head()
all_data['City'].unique()
# there're actually two Portland

# summary of city sales
city_sales=all_data.groupby('City').sum()
cities=all_data['City'].unique()
cities
# notice it's not the same order
# arrange it in the way it group
cities=[city for city, df in all_data.groupby('City')]

plt.bar(cities, city_sales['Sales'])
plt.xticks(cities,rotation='vertical', size=5)
plt.ylabel('Sales in USD')
plt.xlabel('City')
plt.show()

# other way, not make the group as index, so the dataframe can serve better
city_sales=all_data.groupby('City',as_index=False).sum()
city_sales

plt.bar(city_sales['City'], city_sales['Sales'])
plt.xticks(city_sales['City'],rotation='vertical', size=5)
plt.ylabel('Sales in USD')
plt.xlabel('City')
plt.show()