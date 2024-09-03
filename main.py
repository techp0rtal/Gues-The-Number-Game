import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.choice(range(1, 101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_lives = 10
else:
    number_of_lives = 5
print(f"You have {number_of_lives} attempts remaining to guess the number.")

def check_num(input):

    if input > answer and number_of_lives == 1: # this and line 19 fix the bug where it says "guess again" after you've used your last guess
        print(f"Too high.")
    elif input < answer and number_of_lives == 1:
        print(f"Too low.")
    elif input > answer:
        print(f"Too high.\nGuess again.")
    elif input < answer:
        print(f"Too low.\nGuess again.")

def subtract_lives():
    global number_of_lives
    number_of_lives -= 1
    if number_of_lives == 0:
        print("You've run out of guesses, you lose.")
        return
    else:
        print(f"You have {number_of_lives} attempts remaining to guess the number")


#main
while number_of_lives > 0:
    #print(f"You have {number_of_lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    check_num(guess)
    if answer == guess:
        print(f"You got it! The answer was {answer}.")
        break
    else:
        subtract_lives()
