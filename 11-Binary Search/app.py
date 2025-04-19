import random
import time
from bisect import bisect_left

# Binary Search Python Project
# This project demonstrates naive search, recursive binary search, and built-in bisect search.
# These searching methods are commonly discussed in interviews.
# The program also includes user input validation and performance testing.

def naive_search(lst, target):
    """Naive search scans the entire list for the target."""
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

def binary_search(lst, target, low=0, high=None):
    """Recursive binary search on a sorted list."""
    if high is None:
        high = len(lst) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    else:
        return binary_search(lst, target, midpoint + 1, high)

def builtin_bisect_search(lst, target):
    """Uses Python's bisect module for binary search."""
    index = bisect_left(lst, target)
    if index != len(lst) and lst[index] == target:
        return index
    return -1

def performance_test():
    length = 10000
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

    # Naive search performance
    start = time.perf_counter()
    for target in sorted_list:
        naive_search(sorted_list, target)
    print(f"Naive search time: {time.perf_counter() - start:.4f} seconds")

    # Binary search performance
    start = time.perf_counter()
    for target in sorted_list:
        binary_search(sorted_list, target)
    print(f"Recursive binary search time: {time.perf_counter() - start:.4f} seconds")

    # Built-in bisect search performance
    start = time.perf_counter()
    for target in sorted_list:
        builtin_bisect_search(sorted_list, target)
    print(f"Built-in bisect search time: {time.perf_counter() - start:.4f} seconds")

def user_search():
    """Allow user to enter a target number and choose search method with improved error handling and clear prompts."""
    lst = sorted(random.sample(range(-1000, 1000), 100))
    print("\nGenerated sorted list:")
    print(lst)

    while True:
        user_input = input("\nEnter a number to search: ")
        try:
            target = int(user_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print("Choose a search method:")
    print("1. naive")
    print("2. binary")
    print("3. bisect")

    method_map = {"1": "naive", "2": "binary", "3": "bisect", "naive": "naive", "binary": "binary", "bisect": "bisect"}

    while True:
        method_input = input("Enter method name or number: ").strip().lower()
        method = method_map.get(method_input)
        if method:
            break
        else:
            print("Invalid method! Please enter '1', '2', '3' or method names (naive, binary, bisect).")

    if method == 'naive':
        result = naive_search(lst, target)
    elif method == 'binary':
        result = binary_search(lst, target)
    else:
        result = builtin_bisect_search(lst, target)

    if result != -1:
        print(f"Target found at index {result}.")
    else:
        print("Target not found.")

if __name__ == "__main__":
    print("\n---- Performance Test ----")
    performance_test()

    print("\n---- User Search ----")
    user_search()
