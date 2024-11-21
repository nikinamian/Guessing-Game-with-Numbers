#Guessing Game

import random
print ("Welcome to the guessing game!")
print()
print ("Try and guess the right number!")
playagain = "z"
while playagain.upper() != "X":
    guess = int(input("Guess a number 1-10: "))
    num = random.randint(1,10)
    if guess==num:
        print("You guessed right!")
        break
    elif guess<num:
        print("Too low!")
        print("The number was",num)
    elif guess>num:
        print("Too high!")
        print("The number was",num)
    playagain = input("Enter X to quit or any key to play a new game: ").strip()
    print()
    
    
