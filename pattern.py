#! /usr/bin/env python3

""" pattern
        1
    1   2   1
1   2   3   2   1
"""
n = int(input("Enter the depth of pattern : "))

num = 1

for i in range(0, n):
    print("  "*(n-i-1),end="")

    for j in range(0, 2*i+1):
        if ( i == 0 and j == 0 ):
            print("1",end="")
        else:
            if ( j < i ):
                print(num,end=" ")
                num += 1
            elif( j == i ):
                print(num, end=" ")
            else:
                num -= 1
                print(num, end=" ")
    
    print("")
