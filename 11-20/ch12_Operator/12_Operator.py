num = 5
print (id (num))  # print the address of num
name = 'Peter'
print (id(name))  # print the address of name
# address is not based on variable. It is based on data.
b  = 10
a = b
print ('id(a): ', id (a), ' id(b): ', id (b)) # multiple variables (with same address) point to the same data.
# declare another variable k = 10
k = 10
print ('id(k): ' , id(k))
a = 9
print ('id(a): ', id (a), ' id(b): ', id (b), 'id(k): ' , id(k))
b = 8
print ('id(a): ', id (a), ' id(b): ', id (b), 'id(k): ' , id(k))