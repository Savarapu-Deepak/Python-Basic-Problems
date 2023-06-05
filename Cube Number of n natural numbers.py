# Python Program to print sum of cubes of first n natural numbers.

low = int(input('Enter Lower Value : '))
high = int(input('Enter Higher Value : '))
res = 0
for num in range(low, high + 1):
    res += (num ** 3)
else:
    print(res)