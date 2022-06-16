#! /usr/bin/env python3

num = int(input("Enter number to check: "))

# initializing flag
flag = 0

# 1 is not prime neither composite
if (num == 1 or num == 0):
    print(f"{num} is none.")
    exit()

for i in range (0 , (num // 2)+1):
    # if num is 2, it is prime
    if(num == 2):
        flag = 0
        break
    # if it not prime
    elif ( i % num == 0):
        flag = 1
        break
    # it is prime
    else:
        flag = 0

if (flag == 0):
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")
