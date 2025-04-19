# README: Binary Search Python Project

This project demonstrates three search algorithms in Python: **naive search**, **recursive binary search**, and **built-in bisect search**. It also includes a performance test and allows user interaction to choose a search method.

## What’s Included in the Project

### 1. Importing Libraries

- **random**: For generating random numbers.
- **time**: For measuring execution time.
- **bisect**: For using Python’s built-in binary search functionality.

### 2. Search Methods Explained

- **Naive Search**:
  - Goes through each item in the list to find the target.
  - Very simple but slow (O(n) time complexity).

- **Recursive Binary Search**:
  - Works on sorted lists only.
  - Repeatedly splits the list and checks the midpoint.
  - Much faster (O(log n) time complexity).

- **Built-in Bisect Search**:
  - Uses Python’s `bisect_left` for binary searching.
  - Highly optimized and efficient.

### 3. Performance Testing

- The program generates a large sorted list.
- It runs each search method and measures how long each one takes.
- This helps compare which method is the fastest.

### 4. User Search Interaction

- The user is shown a generated sorted list.
- They can input a number to search for.
- The user chooses the method: naive, binary, or bisect.
- The program then shows whether the number was found and at which index.

## Why This Project Matters

- This code is great for learning and understanding search algorithms.
- It helps you see the speed difference between simple and advanced methods.
- The user-friendly part helps you try it yourself and visualize how each method works.

## How to Run

- Run the Python file.
- First, a performance test will show up.
- Then, the program will ask for your input to try a search yourself.

## Conclusion

- Naive search = Simple but slow.
- Binary search = Much faster with sorted data.
- Bisect = Python’s fast built-in solution.

> Learn by running and experimenting with each search method!
