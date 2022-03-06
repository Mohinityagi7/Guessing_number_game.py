# problem ask user to input a number containing more than one digit
# example - 1256 # length = 4
# calculate 1+2+5+6 and print
num = input("enter the number : ")
sum = 0
for i in range(0,len(num)):
    sum += int(num[i])
print(sum)