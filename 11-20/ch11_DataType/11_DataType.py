num = 5
print (type (num))
num = 2.5
print (type (num))
# if I have complex number a + b j
num = 6 + 9j
print (type(num))
# Conver the float into int
a = 5.6
b = int (a)
print ('a = ', a, ', b = ', b, ', type(a) = ', type (a), ', type(b) = ', type (b))
# Convert the int into float
k = float (b)
print ('k = ', k, ', type (k) = ', type(k))
# Covert into complex
c = complex (a, b)
print ('c = ', c, ', type (c) = ', type(c))
# boolean: true or false
print ('a > b = ', a > b)
bool = a > b
print ('bool = ', bool, ', type (bool) = ', type (bool))
# In Pyhton, if you convert boolean into integer, True is 1, False is 0
print ('int (True) = ', int (True), ', int (False) = ', int (False))