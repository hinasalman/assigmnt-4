# Steps to Build a Password Generator:
# User Input: Ask the user how many passwords they want and the length of each password.
# Random Character Selection: Use the random module to select random characters for the passwords.
# Password Generation: Use a for loop to generate multiple passwords based on the user’s input.
# Display the Passwords: Output the generated passwords to the user.
import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters and join them to form a password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Function to generate multiple passwords based on user input
def generate_multiple_passwords():
    # Ask the user for the number of passwords and length of each password
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter the length of each password: "))

    # Generate and display the passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

# Run the password generator
generate_multiple_passwords()


# Explanation of the Code:
# Importing the random and string Modules:

# The random module is used to randomly select characters.
# The string module provides pre-defined sets of characters like letters (string.ascii_letters), digits (string.digits), and punctuation (string.punctuation).
# generate_password Function:

# This function takes a password length as input and generates a random password of that length.
# string.ascii_letters, string.digits, and string.punctuation are combined into a single string of possible characters that can be used in the password.
# The random.choice() function randomly selects characters from this pool, and ''.join() is used to combine them into a single password string.
# generate_multiple_passwords Function:

# This function prompts the user to enter how many passwords they want to generate and the length of each password.
# It then uses a for loop to call the generate_password function the specified number of times, generating and printing each password.
# User Input:

# The user is asked for the number of passwords and their length using input(). These inputs are converted into integers using int().
# Output:

# The program prints the generated passwords one by one to the console.
