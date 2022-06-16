#! /usr/bin/env python3

num = int(input("Enter the number to find factorial: "))

facto = 1
n = num

if (num < 0):
    print("Invalid input\nExiting...")
    exit()

elif(num == 0 or num == 1):
    print(f"The factorial of {num} is: 1")
    exit()
    
else:
    # while loop for finding the factorial
    while(n > 0):
        facto *= n
        n -= 1

print(f"The factorial of {num} is : {facto}")