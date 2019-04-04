pas = 5
x = int (input ('How many candies do you want? '))
i = 1
while (i <= x):
    if (i == pas or i % pas == 0):
        # cannot have no code here
        # Need to hace some code here. Use 'pass' to avoid error.
        print ('pass ', i)
        pass
    else:
        print ('Candy')
    i += 1