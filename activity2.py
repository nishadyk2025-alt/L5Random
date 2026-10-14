import random
while True:
    user_action = input("Enter rock, scissor or paper: ")
    possible_action = ["rock", "paper", "scissors"]
    possible_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {possible_action}.\n")
    if user_action == possible_action:
        print("Draw")
    elif (user_action == "rock" and possible_action == "paper") or (user_action == "scissors" and possible_action == "rock") or (user_action == "paper" and possible_action == "scissors"):
        print("You lose")
    else: 
        print("Win")