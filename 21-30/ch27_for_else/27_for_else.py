# http://book.pythontips.com/en/latest/for_-_else.html
nums = [12, 15, 10, 21, 33]
for num in nums:
    print ('num = ', num)
    if (num % 5 == 0):
        # found it
        print ('num % 5 == 0: ', num)
        break
else:
    # Did not finf anything
    print("not found")