# Steps to Build a Countdown Timer:
# Get the Countdown Time: Ask the user to enter the number of seconds for the countdown.
# Countdown Logic: Use a while loop to keep counting down until it reaches zero.
# Display the Time: Print the remaining time at each second.
# End the Countdown: When the timer reaches zero, print a message to indicate that the countdown is over.import time

# Function to start the countdown timer
import time


def countdown_timer():
    # Ask user for the countdown time in seconds
    countdown_time = int(input("Enter the countdown time in seconds: "))
    
    # Countdown loop
    while countdown_time > 0:
        # Display the remaining time
        print(f"Time left: {countdown_time} seconds")
        time.sleep(1)  # Wait for 1 second
        countdown_time -= 1  # Decrease the time by 1 second

    # When countdown reaches zero
    print("Time's up!")

# Run the countdown timer
countdown_timer()


# Explanation of the Code:
# Importing the time Module:

# The time module is used to handle time-related tasks, such as delaying the execution of the program. Here, time.sleep(1) is used to pause the program for one second between each countdown.
# Getting User Input:

# The program prompts the user to enter a countdown time in seconds using input(). This input is converted to an integer using int().
# Countdown Logic:

# A while loop is used to repeatedly print the remaining time until it reaches zero. The loop condition is countdown_time > 0, meaning it continues as long as the countdown time is greater than zero.
# Each time the loop runs, time.sleep(1) pauses the program for one second, and countdown_time -= 1 reduces the countdown by one second.
# Ending the Countdown:

# When the countdown reaches zero, the loop stops, and the program prints "Time's up!" to notify the user that the countdown has finished.
