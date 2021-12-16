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
    print("\n-Game Info-")
    print("After choosing a cool username and placing your ships on the desired coordinates,")
    print("You will be tasked with taking down your opponent's ships.")
    print("To do this, you must guess the coordinates of their ships.")
    print("For example, if you believe that one of their ships is on b4, you will simply type 'b4'.")
    print("If you have guessed correctly, the chosen square will turn red.")
    print("However, if you have guessed incorrectly, an image of the ocean will appear.")
    
