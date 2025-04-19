

# What Are F-strings?


# Introduced in Python 3.6, f-strings (formatted string literals) let you embed expressions inside string literals.
# Prefix the string with f or F, and include variables or expressions inside {}.

# Input Section
name = input("What is your name? ")
age = int(input("How old are you? "))
hobby = input("What is your favorite hobby? ")
year = 2024  # Current year

# Calculating Year of Birth
birth_year = year - age

# Displaying Results with F-strings
print(f"\nHello, {name}! Nice to meet you.")
print(f"You are {age} years old, so you were probably born in {birth_year}.")
print(f"It's great that you enjoy {hobby}!")
print(f"Did you know that in 5 years, you'll be {age + 5}? Time flies!")


#  Before f-strings were introduced in Python 3.6, there were two other popular ways to format strings in Python:

# % Formatting (Old Style)
# .format() Method (Introduced in Python 2.7 and 3.0)

# 1. % String Formatting (Old Style)

#This method uses the % operator to format strings. It’s very similar to the way C language handles string formatting.
name = "Hina"
age = 27
hobby = "shopping"
year = 2024

birth_year = year - age

# Using % Formatting
print("Hello, %s! You are %d years old, so you were probably born in %d." % (name, age, birth_year))
print("It's great that you enjoy %s!" % hobby)
print("Did you know that in 5 years, you'll be %d?" % (age + 5))

# Explanation:
# %s is used to insert a string (for name and hobby).
# %d is used to insert integers (for age and birth_year).
# Values are passed after the string using the % operator.


# .format() Method
# The .format() method allows you to insert variables into a string at specified positions. You use curly braces {} as placeholders, and the values are provided using .format().

name = "Hina"
age = 27
hobby = "shopping"
year = 2024

birth_year = year - age

# Using .format() Method
print("Hello, {}! You are {} years old, so you were probably born in {}.".format(name, age, birth_year))
print("It's great that you enjoy {}!".format(hobby))
print("Did you know that in 5 years, you'll be {}?".format(age + 5))

# Explanation:
# The {} are placeholders.
# The .format() method replaces each placeholder with the provided values in order.
