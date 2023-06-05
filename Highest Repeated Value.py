# Python Program to print highest repeated value.

data = eval(input('Enter List Value : '))
result = max(set(data), key=data.count)
# list = [1, 2, 3, 4, 1, 54, 1, 98, 1]
# max([1, 2, 3, 4, 54, 98], [4, 1, 1, 1, 1, 1]
print(result)