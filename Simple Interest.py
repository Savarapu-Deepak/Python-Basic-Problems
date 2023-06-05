# EXAMPLE1:
# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500.0
# We need to find simple interest on
# Rs. 10,000 at the rate of 5% for 5
# units of time

# Python Program to print Simple Interest.

p = int(input('Enter Principal Amount : '))
t = int(input('Enter Time : '))
r = eval(input('Enter Rate of Interest : '))

res = (p * t * r) / 100
print('Simple Interest is : Rs.',res)