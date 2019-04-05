#import array as arr
# from module import all funciton *
from array import *

# https://docs.python.org/2/library/array.html
# for integer
vals = array('i', [5, 8, 8, -4, 2])   # array of integer
print ('vals: ', vals)
vals.reverse()
print ('reverse int array: ', vals)
for i in range(5):
    print (vals[i])

# for character, use unicode
cArr = array('u', ['a', 'e', 'i', 'o', 'u'])   # array of character
print ('character array:')
for c in cArr:
    print (c)

iArr = array('i', [5, 8, 8, -4, 2]) 
newArr = array (iArr.typecode, (a*a for a in iArr))
i = 0
for i in range(len (newArr)):
        print (newArr[i])