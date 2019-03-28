list = [10, 20, 30, 40, 50]
print ('type(list) = ', type(list))
s = { 10, 20, 30, 40, 50}
print ('type(s) = ', type(s))
t = (10, 20, 30, 40, 50)
print ('type(t) = ', type(t))
str = 'Peter'
print ('type(str) = ', type (str))
# In Pygton, we do not have character
# we can use single string as a character
c = 'a'
print ('c = ', c, ', type(c) = ', type (c))
# range is a special in Pyhton
x = range(5)
for n in x: 
    print ('n = ', n)
print ('type (x) = ', type (x))
print ('x[0] = ', x[0], 'x[1] = ', x[1])

y = range (2, 5, 2)
for n in y: 
    print ('n = ', n)
print ('type (y) = ', type (y))
print ('y[0] = ', y[0], 'y[1] = ', y[1])