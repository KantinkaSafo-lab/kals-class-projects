import random

print("🎯 Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 20.")

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Number of guesses allowed
attempts = 5

while attempts > 0:
    guess = int(input(f"Your guess ({attempts} attempts left): "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    else:
        # Give hint based on closeness
        difference = abs(secret_number - guess)

        if difference <= 2:
            print("🔥 Very hot! You’re super close.")
        elif difference <= 5:
            print("🌡 Hot! You’re getting close.")
        elif difference <= 10:
            print("❄ Cold! You’re far away.")
        else:
            print("🥶 Very cold! Way off.")

    attempts -= 1

if attempts == 0:
    print(f"😢 Out of attempts! The number was {secret_number}.")
