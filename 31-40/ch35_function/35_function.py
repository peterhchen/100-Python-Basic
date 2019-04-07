# step 1: define funciotn
# step 2: call a funciton

#define funciton
def greet():
    print ("Hello")
    print ("How are you?")

def add (x, y):
    c = x + y
    print ('x + y = ', c)
    return c

def add_sub (x, y):
    c = x + y
    d = x - y
    return c, d

# call function
greet()

result1 = add (5, 4)
print ('resut1 = ', result1)
result2 = add (7, 8)
print ('result2 = ', result2)

result3, result4 = add_sub (4, 5)
print ('result3 = ', result3, '\nresult4 = ', result4)