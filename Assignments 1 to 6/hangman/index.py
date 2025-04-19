
# The Hangman game is another fun Python project that involves using concepts like dictionaries, lists, strings, and random modules. In this project, you will create a game where the user has to guess a hidden word by suggesting letters, and they have a limited number of guesses before they lose the game.

# Steps for Creating the Hangman Game:
# Choose a Word: The program will select a word from a list of possible words.
# Display the Word: The word will be displayed as underscores (_), with the number of underscores matching the number of letters in the word.
# Get User Guesses: The user will guess letters one at a time.
# Track Incorrect Guesses: If the guess is incorrect, the program will count the number of wrong guesses, and the user will lose the game after a set number of incorrect guesses.
# Check for Win or Loss: The game continues until the user guesses the word or runs out of guesses.import random

# List of possible words to guess
import random


word_list = ["python", "java", "javascript", "hangman", "developer", "coding"]

# Function to start the game
def hangman():
    # Randomly select a word
    word = random.choice(word_list)
    word_length = len(word)
    guessed_word = ["_"] * word_length  # Display the word as underscores initially
    guessed_letters = []  # Track the letters that have been guessed
    incorrect_guesses = 0  # Track incorrect guesses
    max_incorrect_guesses = 6  # Max number of incorrect guesses before losing
    
    print("Welcome to Hangman!")
    print("Try to guess the word!")
    print(" ".join(guessed_word))  # Display the initial word with underscores
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Enter a letter: ").lower()
        
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # If the letter has been guessed already, prompt the user to try again
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        # Add the guessed letter to the guessed letters list
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # Update the guessed word with the correct letter
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} tries left.")
        
        # Display the current state of the word and guessed letters
        print(" ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check if the word is fully guessed
        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break
    
    # If the user runs out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game Over! The word was '{word}'.")
    
# Start the game
hangman()


# Explanation of the Code:
# Word List:

# word_list contains a list of words that the program will randomly choose from for the user to guess.
# You can modify the list to include your own words or add more.
# Selecting a Word:

# The word is randomly chosen using random.choice(word_list).
# Displaying the Word:

# The word is displayed as a series of underscores (_) initially, each representing a letter in the word. For example, if the word is "python", it will be displayed as ['_', '_', '_', '_', '_', '_'].
# User Guess:

# The user is asked to guess a letter one at a time using input().
# The program checks if the guess is a valid single letter, and if the user has already guessed it.
# Incorrect Guesses:

# If the user's guess is incorrect, the program increases the count of incorrect_guesses and tells the user how many guesses they have left (the max allowed is 6).
# Update the Display:

# When the user guesses correctly, the program updates the guessed word by replacing the appropriate underscores with the guessed letter.
# End of Game:

# The game ends when the user either guesses the word correctly or runs out of incorrect guesses.
# If the user guesses the word, they win. If they run out of guesses, the game ends with a "Game Over" message and reveals the word.
