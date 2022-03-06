# Ask a user for name
# Example - Harshit Vashisth
# Print count of each words
# Output:
# H : 1
# a : 2
# r : 1
# s : 3
# h : 3
# i : 2 
# t : 3
#   : 1
# v : 1
# name = "HaRsHiT vASHISThA"
# # count() method
# print(name.count(""))
name = input("please enter your name")
i= 0
while i < len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i +=1