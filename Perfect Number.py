# Perfect Number Check Using Python.

data = int(input('Enter Number to be Check : '))
res = 0
for i in range(1, data):
    if data % i == 0:
        res += i
else:
    if res == data:
        print(data, 'is a Perfect Number')