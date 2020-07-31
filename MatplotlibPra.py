# this project is for the practice of matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=[1,2,3,4,5]
y=[2,4,6,8,10]

# resize the graph
plt.figure(figsize=(5,3))

# basic graph
plt.plot([1,2,3,4,5],[2,4,6,8,10],label='2x',marker=".", markersize=10)
# fmt='[color][marker][line]'
# doing the same thing, short hand ''
plt.plot(x,y,'b^--',label='2x')

# line 2
x2=np.arange(0,4,0.5)
plt.plot(x2[:5],x2[:5]**2,'r',label='x^2')
# do projection as well, differentiate with various type of lines
plt.plot(x2[4:],x2[4:]**2,'r--')

plt.title('first graph',fontdict={'fontsize':20})
plt.xlabel('horizental axis')
plt.ylabel('Vertical axis')

plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6,8])

plt.legend()

plt.savefig('MyGraph.png',dpi=100)

plt.show()

#bar chart
labels=['A','B','C']
values=[1,4,2]

bars=plt.bar(labels,values)

plt.figure(figsize=(6,4))

# change the pattern in each bar
patterns=['/','o','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
# bars[0].set_hatch('/')





gas=pd.read_csv('.../Documents/PythonPractice/gas_prices.csv')

# plt.title('Gas prices over time')
# plt.plot(gas.Year,gas['USA'])
# plt.plot(gas.Year, gas['Canada'])
# plt.plot(gas.Year,gas['South Korea'])
# print the every 3rd year
# plt.xticks(gas.Year[::3])
#
# plt.xlabel('Year')
# plt.ylabel('USD($)')
#
# plt.legend(['USA','Canada','South Korea'])

# plt.show()

# quick way to plot all the other cols if not complicated Year--Countries
# sometimes the legend would fail, identify the label first, give legend something to label
for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country],label=gas[country].name)

plt.legend()

plt.show()

plt.savefig('Gas Price throughout Years')






fifa=pd.read_csv('.../Documents/PythonPractice/fifa_data.csv')


# Distribution of Player Skills in 2008 FIFA
bins=[0,10,20,30,40,50,60,70,80,90]
plt.hist(fifa.Overall, bins=bins,color='#abcdef')

plt.ylabel("Number of Players")
plt.xlabel('Skill Level')

plt.title('Distribution of Player Skills in 2008 FIFA')

plt.show()


# pie chart of  left-right foot
left=fifa.loc[fifa['Preferred Foot']=='Left'].count()
right=fifa.loc[fifa['Preferred Foot']=='Right'].count()

plt.pie(left,right,autopct='%.2f %%')

plt.title('Distribution of Preferred Foot in 2008 FIFA')

plt.show()

# weight distribution
# strip the lbs first
fifa.Weight=[int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

# fifa['Weight'].astype('int')

# fifa['Weight'].unique()

light=fifa.loc[fifa['Weight']<125].count()[0]
Medium=fifa.loc[(fifa['Weight']>=125) & (fifa['Weight']<200)].count()[0]
Heavy=fifa.loc[fifa['Weight']>=200].count()[0]
# light
# Medium
# Heavy


weights=[light,Medium,Heavy]
labels=['Under 125lbs','125-200lbs','above 200lbs']

explode=(0.3,0.1,0.1)

plt.style.use('ggplot')

plt.pie(weights,labels=labels,autopct='%.0f %%', pctdistance=1.5,explode=explode)

plt.show()


# compare team
# box plot
barcelona=fifa.loc[fifa['Club']=='FC Barcelona']['Overall']
madrid=fifa.loc[fifa['Club']=='Real Madrid']['Overall']

labels=['FC Barcelona','Real Madrid']

plt.boxplot([barcelona, madrid],labels=labels)

plt.show()



