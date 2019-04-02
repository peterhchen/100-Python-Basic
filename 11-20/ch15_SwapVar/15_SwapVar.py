# swap with two variables, not three variables
# numeric way
a = 5
b = 6
print ('before swap a = ', a, ' b = ', b )
a = a + b
b = a - b
a = a - b
#b = b - a
# Python way
print ('after a =', a, ' b = ', b)
a = 5
b = 6
print ('before swap a = ', a, ' b = ', b )
a,b = b,a
print ('after swap a = ', a, ' b = ', b )
