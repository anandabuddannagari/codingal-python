import random#import module
playing = True # initalise
number = str(random.randint (0,9)) #random in-builr function

print(" I will generate a number for 0 to 9 and you have to try to guess the 1 number digit")

print("The game ends when u get 1 hero")

while playing:
    guess = input("Give me your best guess \n")
    if number == guess:
        print("you win the game")
        print("The number was" , number)
        break

    else:
        print("Your guess isnt right try again")