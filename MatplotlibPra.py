# this project is for the practice of matplotlib
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd


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