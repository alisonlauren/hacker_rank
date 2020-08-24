#Task 
#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird



import sys
n=input()
n=int(n)
if n>=1 and n<=100:
    if n%2==1:
        print("Weird")
    elif n%2:
        print("Not Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n>20:
        print("Not Weird")
