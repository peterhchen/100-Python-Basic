
nums = [25, 12, 36, 95, 14]
print (nums)
# index 0
print (nums[0])
# print from index 2 to end
print (nums[2:])
# print from index -1 is before 0 which is the end
print (nums[-1])
print (nums[-2])

# String array
names = ['Peter', 'Irene', 'Jessica', 'Jason', 'Jasmine', 'Jonathan']
print (names)
# Mix two arrays: numbers and string array
mil = [nums, names]
print (mil)
# append number at the end
nums.append(45)
print (nums)
# insert the number by index and value
nums.insert (1, 77)
print (nums)
# remove by values
nums.remove (77)
print (nums)
# remove by index 1
nums.pop (1)
print (nums)
# pop the array at the end
print (nums.pop())
print (nums)
# delete the elements from index 2 to end
del nums[2:]
print (nums)
# add multiple values
nums.extend ([29, 12, 14, 36])
print (nums)
print (min(nums), max(nums), sum(nums))
nums.sort()
print (nums)