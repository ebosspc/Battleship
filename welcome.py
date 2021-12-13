#Define a function that will welcome a user to the game
def welcome_user():
    global usr_name # Set as a global variable so it can be accessed in other functions

    # Get the user's name as an input, store it in a variable and then print out a welcome message using that name
    print("-----Welcome to the game!-----\n")
    usr_name = str(input("Please enter your name here: "))
    print("Welcome to battleship", usr_name +"!\n")
    print(usr_name + ",", "would you like to read the instructions for the game?")


# Define a function to print the instructions for the game if the user requests them
def print_instructions():
    # Explain to users some basic info about the game
    print("\n-Game Info-")

    #Explain the rules of the game, like how each piece moves
    print("\n-Rules-")
    
    #Describe the objective of the game
    print("\n-Objective-")
    