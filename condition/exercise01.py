# Exercise - Watch coco
# Ask user's name and age
# if user's name start with ('a' or 'A') and age is avove 10 then
# print 'you can watch coco movie'
# Else print 'sorry, you cannot watch coco'
name = input("Enter your name :")
age = int(input("Enter your age :"))
if (age >= 10 and name[0]=='a' or name[0]==''):
    print("You can watch coco movie")
else:
    print("sorry, you can't watch coco")