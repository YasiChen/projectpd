# import pandas as pd
# df =pd.read_csv(".../PythonPractice/pokemon_data.csv")
# print(df)

import pprint
pprint.pprint()

import pandas as pd
import numpy as np
df =pd.read_csv("/Users/chenyasi/Documents/PythonPractice/pokemon_data.csv")
print(df.head(10)) #show the first 10

# read headers
print(df.columns)
# read each column
print(df[['Name','Type 1']][0:5])
# read each row
print(df.head(4))
print(df.iloc[0:4])
print(df.iloc[2,1])

for index,row in df.iterrows():
    print(index,row['Name'])

df.loc[df['Type 1']=="Fire"]


# describe
df.describe()
df.sort_values(['Type 1', 'HP'],ascending=[True,False])

# col sum
df['Total'] = df['HP']+df['Attack']+df['Defense']

# drop col
df.drop(columns=['Total'])

df['Total']=df.iloc[:,4:10].sum(axis=1)

# arrange the order
cols=list(df.columns.values)
df[cols[0:4]+[cols[-1]]+cols[4:12]]
# or
df=df[['HP','Name','Type 1']]

# get rid of the index
df.to_csv('modified.csv',index=False)

df.to_excel('modified.elsx',index=False)

df.to_csv('modified.txt', index=False, sep='\t')

# filter data
newdf = df.loc[(df['Type1']=='Grass') & (df['Type 2']=='Aggressive')]

newdf=newdf.reset_index(drop=True, inplace=True)

# like, contains
df.loc[df['Name'].str.contains('Mega')]
# not contains
df.loc[~df['Name'].str.contains('Mega')]


# ignore the capital, contains fire or grass
import re
df.loc[df['Type 1'].str.contains('Fire|Grass', flags=re.I, regex=True)]

# the name start with pi
df.loc[df['Name'].str.contains('^pi[a-z]', flags=re.I, regex=True)]


# conditional change
df.loc[df['Type 1']=='Fire','Type 1']='Flamer'
df.loc[df['Type 1']=='Fire',['Gerenation','Total']]=['Flamer', True]


# groupby
df.groupby('Type 1').mean().sort_values('Defense',ascending=False)
df.groupby('Type 1').sum()
df.groupby('Type 1').count()#not count null
# clear up, only bring up the count
df['count']=1
df.groupby(['Type 1','Type 2']).count()['count']

# read trunck at a time
df= pd.read_csv("/Users/chenyasi/Documents/PythonPractice/pokemon_data.csv", chunksize=1000)



for df in pd.read_csv("/Users/chenyasi/Documents/PythonPractice/pokemon_data.csv", chunksize=5):
    print("Chunk df")
    print(df)

# big data set analysis
new_df=pd.DataFrame(columns=df.columns)

for df in pd.read_csv("/Users/chenyasi/Documents/PythonPractice/pokemon_data.csv", chunksize=5):
    results=df.groupby(['Type 1']).count()
    new_df=pd.concat(new_df,results)


















