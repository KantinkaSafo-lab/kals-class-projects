import random

print("🎯 Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Number of guesses allowed
attempts = 3

while attempts > 0:
    guess = int(input(f"Guess a number between 1 and 10 ({attempts} attempts left): "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! 📉 Try again.")
    else:
        print("Too high! 📈 Try again.")

    attempts -= 1

if attempts == 0:
    print(f"😢 Sorry, you're out of attempts. The number was {secret_number}.")
