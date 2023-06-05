# Prime Number Check Using Python.

data = int(input('Enter Number to be Check :'))
if data > 1:
    for i in range(2, data):
        if data % i == 0:
            print(data, 'is not a Prime Number')
            break
    else:
        print(data, 'is a Prime Number')