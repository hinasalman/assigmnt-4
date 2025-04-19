# Steps for Creating the Game:
# User Input: The player will enter their choice (rock, paper, or scissors).
# Computer's Choice: The computer will randomly pick one of the three options using random.choice().
# Determine the Winner: The program will compare the player's choice with the computer's choice and determine who wins based on the rules:
# Rock beats Scissors.
# Scissors beats Paper.
# Paper beats Rock.
# Repeat: The game can be played multiple times, and the winner is displayed after each round.

import random

# Function to play one round of Rock, Paper, Scissors
def play_round():
    # List of valid choices
    choices = ['rock', 'paper', 'scissors']

    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Ensure the user's input is valid
    if user_choice not in choices:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        return

    # Computer makes its choice
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Function to play multiple rounds of the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        play_round()

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()




# Explanation of the Code:
# Importing random module:

# The random.choice() function is used to randomly select an option from the list of choices: rock, paper, or scissors.
# play_round() function:

# User Input: The program asks the player to input their choice using input(). The .lower() method is used to ensure case-insensitivity.
# Input Validation: If the user enters something other than rock, paper, or scissors, the game will inform them that the input is invalid and exit the function.
# Computer’s Choice: The computer picks a random choice from the list.
# Determine the Winner: Using if-elif-else statements, the program compares the user’s choice with the computer’s choice and prints the result:
# If both choices are the same, it’s a tie.
# Otherwise, the rules of the game are applied to decide the winner.
# play_game() function:

# This function controls the flow of the game, allowing the user to play multiple rounds. After each round, the user is asked if they want to play again. If they type "yes", the game continues; otherwise, it ends.
