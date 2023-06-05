# Python Program to print Factorial of a NUmber.

data = int(input('Enter Any Number : '))
factorial = 1
for num in range(1, data + 1):
    factorial *= num
else:
    print(f'Factorial of the given number {data} is : ', factorial)
