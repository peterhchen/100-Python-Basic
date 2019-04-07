from numpy import *
arr = array([1,2,3,4,5])
arr = arr + 5
print (arr)

arr1 = array([1.0,1.0,3], float)
arr2 = array([0.5707,2.14159,8], float)
arr3 = arr1 + arr2
print (arr3)
print (sin(arr3))
print (sqrt(arr3))
print (max(arr3))
print (sort(arr3))
print (concatenate([arr1, arr2]))