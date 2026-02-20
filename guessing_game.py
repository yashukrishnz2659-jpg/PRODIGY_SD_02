import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

attempts = 0
print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        print("It took you", attempts, "attempt(s) to win the game.")
        break
