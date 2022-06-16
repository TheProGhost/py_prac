#! /usr/bin/env python3

num = input("Enter here for checking palindrome: ")

# checking with reverase string
if (num == num[::-1]):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")