import random
winning_number = 43 #user guess 43 then win
guess = 1 # counting number user guessing number
number = int(input("guess a number between 1 and 100: ")) # user number input
game_over = False # user win then game stop

while not game_over: # i dont know how many times are loop went then i am appling {while loop condition} :
    if number == winning_number:   # win
        print(f"you win, and you guessed this number in {guess} times") # string formating
        game_over = True
      
    else:          # guess wrong
        if number < winning_number :
            print("too low")  
            guess +=1
            number = int(input("guess  again : "))
            # low guess
        else :
            print("too high")
            guess += 1
            number = int(input("guess again :"))
            #high guess