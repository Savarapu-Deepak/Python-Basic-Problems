# Armstrong Number Check Using Python.

data = int(input('Enter Any Number : '))
check, total, length = data, 0, len(str(data))
while data > 0:
    rem = data % 10
    total = total + (rem ** length)
    data //= 10
else:
    if total == check:
        print(check, 'is an Armstrong Number')
    else:
        print(check, 'is not an Armstrong Number')