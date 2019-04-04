max = 5
x = int (input ('How many candies do you want? '))
i = 1
while (i <= x):
    print ('Candy')
    if (i >= max):
        print ('Out of stock')
        break
    i += 1