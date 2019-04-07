from numpy import *
arr1 = array ([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])
print (arr1)
print ('size of array: ', arr1.size)
# 2 di array into 1 d array
arr2 = arr1.flatten();
print ('2-d array into 1-d array:\n', arr2)
# reshape
arr3 = arr2.reshape (2, 2, 3)
print ('1-d array into 3-d array: \n', arr3)
print ('max of array: \n', arr3.max())
m1 = matrix ('1 2 3; 4 5 6; 7 8 9')
m2 = matrix ('1 2 3; 4 5 6; 6 7 9')
# the following is something different, not one-by-obe
m3 = m1 * m2
print ('m3: ', m3)