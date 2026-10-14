import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number 0-9 and you have to guess the number one digit at a time")
print("The game end when you get 1 hero")
while playing:
    guess = input("Guess a number: ")
    if number == guess:
        print("You win")
    else: 
        print("Try again")