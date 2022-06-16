#! /usr/bin/env python3

num = input("Enter the number to check: ")
new_num = 0

# checking if input is digit or not
if(num.isdigit()):
    length = len(num)
    for i in range (0, length):
        new_num += (int(num[i]))**length

# exiting if input is not digit
else: 
    print("Please Enter the Digits ONLY.\nExiting...")
    exit()

# printing if it is palindrome or not.
if(new_num == int(num)):
    print(f"{num} is armstrong.")
else:
    print(f"{num} is not armstrong.")