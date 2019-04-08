def person (name, age):
    print (name)
    print (age)

# variable arguments: *args
def sum (*b):
    #c = a + b
    #print (c)
    c = 0
    for i in b:
        c = c + i
    print (c)
person ('peter', 62)
sum (1, 2, 3, 4, 5)