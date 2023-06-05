# Python Program to check given number is fibonacci or not.

data = int(input('Enter Any Number : '))
c, a, b = 0, 1, 1
if data == 0 or data == 1:
    print(data, 'is a Fibonacci Number')
else:
    while c < data:
        c = a + b
        a = b
        b = c
        if c == data:
            print(data, 'is a Fibonacci Number')
            break
        else:
            pass
    else:
        print(data, 'is not a Fibonacci Number')


