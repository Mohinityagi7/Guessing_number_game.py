#Exercise of three
# Sum of n natural numbers 
#ask a user for natural number(n)
#print total from 1 to n
n = int(input("enter a number : "))
Sum = 0 
i = 1
while i<=n:
    Sum = Sum + i
    i = i + 1
print(Sum)
