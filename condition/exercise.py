#Exercise, Number guessing game
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correcttly then print "YOU WIN !!!!"
# if user didn't guessed correctly then:
#     if user guessed lower than actual numberthen print "too low"
#     if user guessed higher then actual number then print "too high"

# google " how to generate random number in python " to generate random 
# winning number

# import random 
# n = random. random() 
# print(n)

winning_number = 27
user_input = input("guess a number b/w 1 and 100 : ")
user_input = int(user_input)
if user_input == winning_number:
    print("You win !!!")
else: #nested if_else
    if user_input<winning_number:
        print("too low")
    else:
        print("too high")