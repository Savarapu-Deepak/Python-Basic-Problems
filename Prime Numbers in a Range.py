# Prime Numbers with in a Range.

low = int(input('Enter Lower Value : '))
high = int(input('Enter Upper Value : '))

for i in range(low, high + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
    else:
        print('Starting Number Should be greater than 1')