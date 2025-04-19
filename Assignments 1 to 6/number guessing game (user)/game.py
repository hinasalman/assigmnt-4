# teps for Creating the Game:
# Set a range: The user will define a number range (e.g., between 1 and 100).
# Computer guesses: The computer will try to guess a number within this range.
# User feedback: The user will provide feedback whether the computer's guess is too high, too low, or correct.
# Loop: The computer will continue guessing and adjusting based on user feedback until it guesses the correct number.
import random

# Function to start the game
def computer_guess():
    # The user will set the range for the guess
    print("Welcome to the 'Guess the Number' game!")
    print("Pick a number between 1 and 100, and I will try to guess it.")

    # User specifies the range
    low = 1
    high = 100
    feedback = ''

    # While loop continues until the computer guesses the number correctly
    while feedback != 'c':
        # The computer guesses the middle value between low and high
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        
        # Ask the user for feedback on the guess
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").lower()

        # Adjust the range based on the feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Hooray! I guessed the correct number: {guess}")
        else:
            print("Please enter a valid response (H, L, or C).")

# Start the game
computer_guess()



# Explanation of the Code:
# Importing the random module:

# We use import random to access the randint() function, which will allow the computer to randomly select guesses from the given range.
# Game Function (computer_guess):

# The function computer_guess() handles the main game logic. It begins by setting a range (low and high), which is initially set between 1 and 100.
# Guessing the Number:

# The computer guesses the middle value of the current range using random.randint(low, high).
# User Feedback:

# After each guess, the user is prompted to provide feedback:
# 'H' for "too high"
# 'L' for "too low"
# 'C' for "correct"
# Depending on the feedback:
# If too high, the upper limit of the range (high) is reduced.
# If too low, the lower limit of the range (low) is increased.
# If the guess is correct, the game ends.
# Looping:

# The game uses a while loop to continue making guesses until the user confirms the guess is correct by entering 'c'.
# Input Handling:

# The feedback is case-insensitive, and the program prompts for a valid response if the input is incorrect.