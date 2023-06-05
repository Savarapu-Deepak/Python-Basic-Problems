# Python Program to print Fibonacci Series.

data = int(input('Enter Fibonacci Range : '))
n1, n2 = 0, 1
while data > 0:
    print(n1, end=' ')
    next_element = n1 + n2
    n1 = n2
    n2 = next_element
    data -= 1