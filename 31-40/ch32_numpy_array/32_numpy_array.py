from numpy import *
# set the array into float
arr = array ([1, 2, 3, 4, 5], float)
print (arr.dtype)
print (arr)
arr1 = linspace (0, 16, 10) # start, stop, number of elements
print (arr1)
arr2 = arange (1, 15, 2) # start, stop, increment
print (arr2)
# start: 1E+01, stop: 1.E+40, number of elements
arr3 = logspace (1, 40, 5) 
print (arr3)
arr4 = zeros (5)
print (arr4)
arr5 = ones (5, int)
print (arr5)