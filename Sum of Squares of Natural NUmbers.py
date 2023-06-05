# Python Program to print sum of squares of first n natural numbers.

lower_Value = int(input('Enter Lower Value : '))
upper_Value = int(input('Enter Upper Value : '))
sum_ = 0
for num in range(lower_Value, upper_Value + 1):
    sum_ += (num * num)
else:
    print(sum_)
