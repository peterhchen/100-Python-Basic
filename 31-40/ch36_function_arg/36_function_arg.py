# call by value and call by reference

def update (x):
    x = 9;
    print ('x = ', x)

a = 10
update (a)
print ('a = ', a)

# prinbt id
def update1 (x):
    x = 9;
    print ('x = ', x)

b = 10
print ('id(b)= ', id (b))
update1 (b)
print ('b = ', b)

# Use list
def update_list (lst):
    lst[1] = 25;
    print ('lst = ', lst)

lst = [10, 20, 30]
print ('id(lst)= ', id (lst))
update_list (lst)
print ('lst = ', lst)