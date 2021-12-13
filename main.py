#####-Imports-#####
# Import turtle library for drawing and display functions
import turtle as trtl

# Import random library to utilize random number generation functions
import random as rand

# Import welcome module storing insturctions and welcome functions
import welcome as welcome

# Call the function to welcome the user to the game
welcome.welcome_user()

# Define a variable to determine if the user wants to receive debug message in the terminal
developer_mode = 0

# Ask the user if they want instructions until they enter a valid input
while True:
    # Store the user input for instructions request
    instructions_request = str(input("Please write y for yes, n for no, and d if you would like to enter developer mode: "))

    # Check if the user selected yes and adjust variables appropriately
    if instructions_request == "y":
        instructions_request = 1
        break

    # Check if the user selected no and adjust variables appropriately
    elif instructions_request == "n":
        instructions_request = 0
        break

    # Check if the user wants to enter developer mode
    elif instructions_request == "d":
        # Turn on developer mode
        developer_mode = 1
        print("You are now in developer mode.")

    # Output an error message if the user enters an invalid input
    else:
        print("Sorry! That was not a valid input.\nPlease try again.")

# Print the instructions if the user wants them
if instructions_request == 1:
    welcome.print_instructions()

# Don't print the instructions if the user doesn't want them
elif instructions_request == 0:
    print("\nWelcome back!")

# Output message for debugging if the user is in developer mode
if developer_mode == 1:
    print("You are running this program as a developer")

# Inform the user the game is starting
print("\nLets begin!")