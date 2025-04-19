# Markov Chain Text Generator

A simple Python implementation of a Markov chain for generating text based on patterns in existing text.

## What is a Markov Chain?

A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules. In text generation, a Markov chain analyzes existing text to determine the probability of one word following another, then uses these probabilities to generate new text that mimics the style of the original.

## Requirements

- Python 3.6 or higher

## Setup

1. Clone or download this repository
2. No additional packages are required - the project uses only Python standard libraries

## Quick Start

### Create a sample text file

<!-- # Create a sample text file -->

python create_sample_text.py

<!-- # Train on the sample text and generate 100 words -->

python markov_chain.py --train sample_text.txt --generate --words 100

<!-- # Save the trained model -->

python markov_chain.py --train sample_text.txt --save-model my_model.json

<!-- # Load the model and generate text -->

python markov_chain.py --load-model my_model.json --generate
