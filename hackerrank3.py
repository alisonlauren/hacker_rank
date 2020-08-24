#Task 
#The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .



n = input()
n = int(n)
for i in range(0,100):
    if i < n:
        print(i**2)
