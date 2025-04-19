# Steps for Creating the Game:
# Import the random module: This will help generate random numbers.
# Generate a random number: The computer will randomly pick a number between a given range.
# Get the user's guess: The user will be prompted to enter their guess.
# Check if the guess is correct: Use a while loop to keep asking the user until they guess the correct number.
# Give feedback: Provide hints (like "too high" or "too low") to guide the user.
# End the game when the user guesses correctly.


import random

# Function to start the game
def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize number of guesses
    attempts = 0

    print("Welcome to 'Guess the Number' Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # While loop to keep asking the user for guesses
    while True:
        # Get the user's guess
        user_guess = int(input("Enter your guess: "))
        
        # Increment the attempt counter
        attempts += 1

        # Check if the user's guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # User guessed correctly
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
guess_the_number()

# Key Concepts Covered:



# Random Module: We used the random.randint() function to generate a random number.
# Functions: We defined a function guess_the_number() to encapsulate the game logic.
# While Loop: We used a while True loop to keep the game going until the correct guess is made.
# Conditionals: We used if, elif, and else to check if the guess is correct or not.
# User Input: We used input() to get guesses from the user and converted them to integers.