# Compound Interest .

# Formula ---> P(1 + (r / 100))**t

p = float(input('Enter Principal Amount : '))
t = int(input('Enter Time Peroid : '))
r = float(input('Enter Rate of Interest : '))

a = p * (1 + (r / 100))**t
print('Compound Interest : ', round((a - p), 2))