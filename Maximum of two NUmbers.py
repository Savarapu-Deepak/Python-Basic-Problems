# Python Program to print maximum of two numbers.

a = int(input('Enter Any Number : '))
b = int(input('Enter Any Number : '))
if a > b:
    print(a, 'is greater than ', b)
else:
    print(b, 'is greater than', a)

# Using Functions Concept.

def max_Of_Two(a, b):
    if a > b:
        print(a, 'is greater than ', b)
    else:
        print(b, 'is greater than ', b)
max_Of_Two(100, 125)