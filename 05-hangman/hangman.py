import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses a word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_current_state(lives, used_letters, word, lives_visual_dict):
    print(f"\nYou have {lives} lives left. Used letters: ", ' '.join(sorted(used_letters)))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_visual_dict[lives])
    print('Current word: ', ' '.join(word_list))

def get_user_guess(alphabet, used_letters):
    while True:
        user_letter = input('Guess a letter: ').upper()
        if len(user_letter) != 1 or not user_letter.isalpha():
            print("Please enter a single valid letter.")
        elif user_letter in used_letters:
            print("You have already guessed that letter. Try another one.")
        else:
            return user_letter

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        display_current_state(lives, used_letters, word, lives_visual_dict)
        user_letter = get_user_guess(alphabet, used_letters)

        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('Correct guess!')
        else:
            lives -= 1
            print(f"Incorrect guess. The letter {user_letter} is not in the word.")

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'Sorry, you lost! The word was: {word}')
    else:
        print(f'Congratulations! You correctly guessed the word: {word}')

def main():
    while True:
        hangman()
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
