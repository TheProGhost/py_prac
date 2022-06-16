#! /usr/bin/env python3

upper_limit = int(input("Enter number of elements you wanted to print: "))

# initializing the series list
fibo = [0, 1]
# input conditions
if( upper_limit <= 0 ):
    print("Next time enter atleast 1. PLEASE..\nExiting...")
    exit()
elif(upper_limit == 1):
    print(f"The series with given number of elements is: {fibo[0]}")
    exit()

else:
    # adding elements to series list
    for i in range(0, upper_limit - 2):
        fibo.append(fibo[i] + fibo[i+1])

    print(f"The series with given number of elements is: {fibo}")