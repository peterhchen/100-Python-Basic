skip = 5
x = int (input ('How many candies do you want? '))
i = 1
while (i <= x):

    if (i == skip or i % skip == 0):
        print ('Skip ', i)
        i += 1
        continue
    else:
        print ('Candy')
        i += 1