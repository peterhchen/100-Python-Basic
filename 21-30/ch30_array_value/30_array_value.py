from array import *
arr = array('i', [])    # integer type 'i'
n = int (input ("Enter the length of the array: "))

for i in range(n):
    x = int (input ("Input the next value: "))
    arr.append(x)

print (arr)

val = int (input("Enter the value for search: "))
k = 0
for e in arr:
    if (e == val):
        print (k)
        break
    k+=1