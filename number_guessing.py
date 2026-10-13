# This is just a simple number guessing game.
import random

number = random.randint(1, 100)
attempts = 0
success = False

while not success:
    guess = input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess == number:
        success = True
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
    elif guess < number:
        attempts += 1
        print("Too low! Try again.")
    else:
        attempts += 1
        print("Too high! Try again.")