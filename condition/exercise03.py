# problem ask user to input a number containing more than one digit
# example - 1256 
# calculate 1+2+5+6 and print
Number = input('enter the number: ')
# "1256" #length = 4,last index = 3
total = 0
i = 0
while i<len(Number):
    total += int(Number[i])
    i += 1
print(total)
# print0(f"sum of numbers{Example[]+Example[]+Example[]+Example[]}")