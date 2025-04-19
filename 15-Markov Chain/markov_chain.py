#!/usr/bin/env python3
"""
Markov Chain Text Generator
A simple implementation of a Markov chain for text generation.
"""

import random
import argparse
import os 
import json
import sys


class MarkovChain:
    """A Markov chain text generator."""

    def __init__(self, chain_length=2):
        """Initialize the Markov chain with a specified chain length."""
        self.chain_length = chain_length
        self.model = {}
        self.start_words = []

    def train(self, text):
        """Train the Markov chain on the provided text."""
        words = text.split()
        if len(words) <= self.chain_length:
            raise ValueError("Text is too short to train the model")

        # Add starting words to the list of possible starting points
        for i in range(len(words) - self.chain_length):
            key = tuple(words[i:i + self.chain_length])
            self.start_words.append(key)

            # Build the model
            if key not in self.model:
                self.model[key] = []
            
            if i + self.chain_length < len(words):
                self.model[key].append(words[i + self.chain_length])

    def train_from_file(self, filename):
        """Train the Markov chain from a text file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                self.train(text)
                print(f"Successfully trained on {filename}")
        except Exception as e:
            print(f"Error training from file {filename}: {e}")
            sys.exit(1)

    def generate_text(self, max_words=100):
        """Generate text using the trained Markov chain."""
        if not self.model:
            raise ValueError("Model is not trained yet")

        if not self.start_words:
            raise ValueError("No starting words available")

        # Start with a random key from the start_words
        current_key = random.choice(self.start_words)
        result = list(current_key)

        # Generate text
        for _ in range(max_words - self.chain_length):
            if current_key not in self.model or not self.model[current_key]:
                # If we reach a dead end, pick a new random starting point
                current_key = random.choice(self.start_words)
                result.append("...")
                continue

            # Choose the next word based on the current key
            next_word = random.choice(self.model[current_key])
            result.append(next_word)

            # Update the current key
            current_key = tuple(result[-self.chain_length:])

        return " ".join(result)

    def save_model(self, filename):
        """Save the trained model to a JSON file."""
        # Convert tuple keys to strings for JSON serialization
        serializable_model = {
            "chain_length": self.chain_length,
            "model": {" ".join(key): value for key, value in self.model.items()},
            "start_words": [" ".join(key) for key in self.start_words]
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(serializable_model, file, indent=2)
                print(f"Model saved to {filename}")
        except Exception as e:
            print(f"Error saving model to {filename}: {e}")

    def load_model(self, filename):
        """Load a trained model from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                self.chain_length = data["chain_length"]
                # Convert string keys back to tuples
                self.model = {tuple(key.split()): value for key, value in data["model"].items()}
                self.start_words = [tuple(key.split()) for key in data["start_words"]]
                
                print(f"Model loaded from {filename}")
        except Exception as e:
            print(f"Error loading model from {filename}: {e}")
            sys.exit(1)


def main():
    """Main function to run the Markov chain text generator."""
    parser = argparse.ArgumentParser(description="Markov Chain Text Generator")
    parser.add_argument("--train", help="Train on a text file")
    parser.add_argument("--generate", action="store_true", help="Generate text")
    parser.add_argument("--words", type=int, default=100, help="Number of words to generate")
    parser.add_argument("--chain-length", type=int, default=2, help="Length of the Markov chain")
    parser.add_argument("--save-model", help="Save the trained model to a file")
    parser.add_argument("--load-model", help="Load a trained model from a file")
    parser.add_argument("--output", help="Output file for generated text")
    
    args = parser.parse_args()
    
    # Create a Markov chain
    markov = MarkovChain(chain_length=args.chain_length)
    
    # Load model if specified
    if args.load_model:
        markov.load_model(args.load_model)
    
    # Train on text file if specified
    if args.train:
        markov.train_from_file(args.train)
    
    # Save model if specified
    if args.save_model:
        markov.save_model(args.save_model)
    
    # Generate text if requested
    if args.generate:
        try:
            generated_text = markov.generate_text(max_words=args.words)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as file:
                    file.write(generated_text)
                    print(f"Generated text saved to {args.output}")
            else:
                print("\nGenerated Text:")
                print("--------------")
                print(generated_text)
                print("--------------")
        except ValueError as e:
            print(f"Error generating text: {e}")
            sys.exit(1)
    
    # If no action was specified, show help
    if not (args.train or args.generate or args.load_model or args.save_model):
        parser.print_help()


if __name__ == "__main__":
    main()

