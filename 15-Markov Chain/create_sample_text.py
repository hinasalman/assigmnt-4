#!/usr/bin/env python3
"""
Create a sample text file with a short excerpt from Alice in Wonderland.
"""

import argparse

def create_sample_text(filename="sample_text.txt"):
    """Create a sample text file with a short excerpt."""
    sample_text = """Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do: once or twice she had peeped into the book her sister was reading, 
but it had no pictures or conversations in it, "and what is the use of a book," thought Alice 
"without pictures or conversations?"

So she was considering in her own mind (as well as she could, for the hot day made her feel very 
sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of 
getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sample_text)
        print(f"Sample text file created: {filename}")
    except IOError as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a sample Alice in Wonderland text file.")
    parser.add_argument("--output", default="sample_text.txt", help="Output file name")
    args = parser.parse_args()
    create_sample_text(filename=args.output)
# create_sample_text.py

def create_sample_text():
    """Create a sample text file with conversational and fun chatbot-like text."""
    sample_text = """Alice was beginning to get very tired of sitting by her sister on the bank,
    and of having nothing to do: once or twice she had peeped into the book her sister was reading,
    but it had no pictures or conversations in it, "and what is the use of a book," thought Alice
    "without pictures or conversations?"

    User: Hello, how are you?
    Bot: I am good! How can I help you today?

    User: Tell me a joke.
    Bot: Why did the scarecrow win an award? Because he was outstanding in his field!

    User: Motivate me.
    Bot: You are capable of amazing things! Just believe in yourself and keep going.

    User: Kya haal hai?
    Bot: Main bilkul theek hoon! Tumhare liye kya kar sakta hoon?

    User: Shayari sunaao.
    Bot: Zindagi ek kitaab hai, har pal ek nayi kahani hai,
    samjho toh mooti hai, na samjho toh paani hai.
    """

    with open("sample_text.txt", "w", encoding="utf-8") as file:
        file.write(sample_text)

    print("Sample text file created: sample_text.txt")


if __name__ == "__main__":
    create_sample_text()
