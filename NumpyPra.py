import numpy as np

a=np.array([1,2,3],dtype='int32')
print(a)
a.ndim
a.dtype
a.itemsize
a.size
a.itemsize*a.size

b=np.array([[1,2,3],[4,5,6]])
print(b)
b.shape

# get specific location
a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
a[1,2]
a[0,:]
a[0,1:6]
# replace
a[1,5]=20
print(a)

# all zero matrix
np.zeros((2,3))
# all one: four 2*2 matrix
np.ones((4,2,2),dtype='int32')
# other numbers
np.full((2,2),100)
# full_like, make an alike matrix
np.full_like(a,4)

# random decimal numbers
np.random.rand(4,2)
np.random.sample(a.shape)

# random int values from 3 to 7(8 is exluded)
np.random.randint(3,8,size=(3,3))

# identity matrix,diagonal 1
np.identity(5)

# repeat
arr=np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

# construct matrix
output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:4,1:4]=z
print(output)

# copy arrays
# change the original value as well
a=np.array([1,2,3])
b=a
b[0]=100
print(a)
print(b)
# instead use the copy
b=a.copy()


# cal
a=np.array([1,2,3,4])
print(a)

# all add 2
a+2

# cal between array
b=np.array([1,0,1,0])
a+b

# expenotiate
a**2

# sin/cos/tan
np.cos(a)

# linear algebra
a=np.ones((2,3))
b=np.full((3,2),2)

np.matmul(a,b)


# determinant
c=np.identity(3)
np.linalg.det(c)


# statistics analysis
stats=np.array([[1,2,3],[4,5,6]])
np.max(stats,axis=1)

# sum of col
np.sum(stats,axis=0)
# sum of row
np.sum(stats,axis=1)

# reorganizing
before=np.array([[1,2,3],[4,5,6]])
after=before.reshape((3,2))
print(after)

# stacking
v1=np.array([1,2,3])
v2=np.array([4,5,3])

np.vstack([v1,v2,v2])

# horizontal stacking
np.hstack([v1,v2])


# load the data
filedata=np.genfromtxt('data.txt',delimiter=',')
filedata.astype('int32')
filedata

filedata[[1,2,7]]
# filter-index with a list
filedata[filedata>50]

np.any(filedata>50, axis=0)

np.all(filedata>50, axis=0)

# check if meet certain critiria
((filedata>50)&(filedata<100))







