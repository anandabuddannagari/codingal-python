import random #importanting random modules

while True: #iterate loop
    user_action = input("Enter a choice (rock, paper, scissors): ")#take imput 
    possible_actions = ["rock","paper","scissors"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\nyou chose{user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors! you win!")
        else:
            print("paper covers rock! you lose.")

    elif user_action =="paper":
        if computer_action =="rock":
            print("paper cover rock you win")
        else:
            print("scissors cuts paper! you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! you win!")

        else:
            print("scissors cuts paper! you lose.")
    elif user_action == "Scissors":
        if computer_action == "paper":
            print("scissors cuts paper! you win!")
        else: 
            print("rock smashes scissors! you lose!")

    play_again = input("play again?(y/n):")
    if play_again != "y":
        break