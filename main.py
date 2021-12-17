#####-Imports-#####
# Import turtle library for drawing and display functions
import turtle as trtl

# Import random library to utilize random number generation functions
import random as rand

# Import welcome module storing insturctions and welcome functions
import welcome as welcome

#####-Instructions and Welcome Handling-#####
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


#####-Game Config-#####
def create_coordinates_list():
    # Define a global list of coordinates to easily grab values from
    global coordinates_list
    coordinates_list = ["a1","a2","a3","a4","a5","a6","a7","a8"
                        "b1","b2","b3","b4","b5","b6","b7","b8",
                        "c1","c2","c3","c4","c5","c6","c7","c8",
                        "d1","d2","d3","d4","d5","d6","d7","d8",
                        "e1","e2","e3","e4","e5","e6","e7","e8",
                        "f1","f2","f3","f4","f5","f6","f7","f8",
                        "g1","g2","g3","g4","g5","g6","g7","g8",
                        "h1","h2","h3","h4","h5","h6","h7","h8",]

# Define a function that will create the grid that the user will set as their own ships
def create_user_grid():
    # https://trinket.io/python/051179b6d3
    squares_per_side = 8

    #Define an empty list that will contain the locations of the user's ships
    # A 0 corresponds to no ship at that location
    # A 1 corresponds to a ship at that location
    # An X stands for a hit ship at that location
    # The notation will not change for a miss
    global player_grid
    player_grid = []

    global column_a,column_b,column_c,column_d,column_e,column_f,column_g,column_h
    column_a = 0
    column_b = 1
    column_c = 2
    column_d = 3
    column_e = 4
    column_f = 5
    column_g = 6
    column_h = 7

    global row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8
    row_1 = 7
    row_2 = 6
    row_3 = 5
    row_4 = 4
    row_5 = 3
    row_6 = 2
    row_7 = 1
    row_8 = 0

    # For loop to generate all values in the grid
    for i in range(squares_per_side):
        player_grid.append(["O"] * squares_per_side)


# Define a function to create tracker variables for the users' ships
def set_user_ship_properties():
    # Globalize and define ship tracker variables for the a squares so they can be used in other functions
    global ship_on_a1,ship_on_a2,ship_on_a3,ship_on_a4,ship_on_a5,ship_on_a6,ship_on_a7,ship_on_a8
    ship_on_a1 = 0
    ship_on_a2 = 0
    ship_on_a3 = 0
    ship_on_a4 = 0
    ship_on_a5 = 0
    ship_on_a6 = 0
    ship_on_a7 = 0
    ship_on_a8 = 0

    # Globalize and define ship tracker variables for the b squares so they can be used in other functions
    global ship_on_b1,ship_on_b2,ship_on_b3,ship_on_b4,ship_on_b5,ship_on_b6,ship_on_b7,ship_on_b8
    ship_on_b1 = 0
    ship_on_b2 = 0
    ship_on_b3 = 0
    ship_on_b4 = 0
    ship_on_b5 = 0
    ship_on_b6 = 0
    ship_on_b7 = 0
    ship_on_b8 = 0

    # Globalize and define ship tracker variables for the c squares so they can be used in other functions
    global ship_on_c1,ship_on_c2,ship_on_c3,ship_on_c4,ship_on_c5,ship_on_c6,ship_on_c7,ship_on_c8
    ship_on_c1 = 0
    ship_on_c2 = 0
    ship_on_c3 = 0
    ship_on_c4 = 0
    ship_on_c5 = 0
    ship_on_c6 = 0
    ship_on_c7 = 0
    ship_on_c8 = 0

    # Globalize and define ship tracker variables for the d squares so they can be used in other functions
    global ship_on_d1,ship_on_d2,ship_on_d3,ship_on_d4,ship_on_d5,ship_on_d6,ship_on_d7,ship_on_d8
    ship_on_d1 = 0
    ship_on_d2 = 0
    ship_on_d3 = 0
    ship_on_d4 = 0
    ship_on_d5 = 0
    ship_on_d6 = 0
    ship_on_d7 = 0
    ship_on_d8 = 0

    # Globalize and define ship tracker variables for the e squares so they can be used in other functions
    global ship_on_e1,ship_on_e2,ship_on_e3,ship_on_e4,ship_on_e5,ship_on_e6,ship_on_e7,ship_on_e8
    ship_on_e1 = 0
    ship_on_e2 = 0
    ship_on_e3 = 0
    ship_on_e4 = 0
    ship_on_e5 = 0
    ship_on_e6 = 0
    ship_on_e7 = 0
    ship_on_e8 = 0

    # Globalize and define ship tracker variables for the f squares so they can be used in other functions
    global ship_on_f1,ship_on_f2,ship_on_f3,ship_on_f4,ship_on_f5,ship_on_f6,ship_on_f7,ship_on_f8
    ship_on_f1 = 0
    ship_on_f2 = 0
    ship_on_f3 = 0
    ship_on_f4 = 0
    ship_on_f5 = 0
    ship_on_f6 = 0
    ship_on_f7 = 0
    ship_on_f8 = 0

    # Globalize and define ship tracker variables for the g squares so they can be used in other functions
    global ship_on_g1,ship_on_g2,ship_on_g3,ship_on_g4,ship_on_g5,ship_on_g6,ship_on_g7,ship_on_g8
    ship_on_g1 = 0
    ship_on_g2 = 0
    ship_on_g3 = 0
    ship_on_g4 = 0
    ship_on_g5 = 0
    ship_on_g6 = 0
    ship_on_g7 = 0
    ship_on_g8 = 0

    # Globalize and define ship tracker variables for the h squares so they can be used in other functions
    global ship_on_h1,ship_on_h2,ship_on_h3,ship_on_h4,ship_on_h5,ship_on_h6,ship_on_h7,ship_on_h8
    ship_on_h1 = 0
    ship_on_h2 = 0
    ship_on_h3 = 0
    ship_on_h4 = 0
    ship_on_h5 = 0
    ship_on_h6 = 0
    ship_on_h7 = 0
    ship_on_h8 = 0


# Define a function to choose where the user wants to place their ships
def get_user_ship_properties():
    print("-Ship Selection-")
    print("\nBefore we begin the game, you need to choose where you want to place your ships.")
    print("please note that your coordinate should follow the naming convention LetterNumber ex: a1, e4, c3.")
    print("You may only select letters between a-h and numbers between 1-8.")
    print("When you are done entering coordinates, type done or d")

    continue_with_loop = 1
    global player_grid
    while continue_with_loop == 1:
        usr_ship_selection_input = str(input("Please type the coordinate of where you want to place your ship: "))

        global ship_on_a1,ship_on_a2,ship_on_a3,ship_on_a4,ship_on_a5,ship_on_a6,ship_on_a7,ship_on_a8
        if usr_ship_selection_input == "a1":
            ship_on_a1 = 1
            player_grid[row_1][column_a] = "1"
        if usr_ship_selection_input == "a2":
            ship_on_a2 = 1
            player_grid[row_2][column_a] = "1"
        if usr_ship_selection_input == "a3":
            ship_on_a3 = 1
            player_grid[row_3][column_a] = "1"
        if usr_ship_selection_input == "a4":
            ship_on_a4 = 1
            player_grid[row_4][column_a] = "1"
        if usr_ship_selection_input == "a5":
            ship_on_a5 = 1
            player_grid[row_5][column_a] = "1"
        if usr_ship_selection_input == "a6":
            ship_on_a6 = 1
            player_grid[row_6][column_a] = "1"
        if usr_ship_selection_input == "a7":
            ship_on_a7 = 1
            player_grid[row_7][column_a] = "1"
        if usr_ship_selection_input == "a8":
            ship_on_a8 = 1
            player_grid[row_8][column_a] = "1"
        
        global ship_on_b1,ship_on_b2,ship_on_b3,ship_on_b4,ship_on_b5,ship_on_b6,ship_on_b7,ship_on_b8
        if usr_ship_selection_input == "b1":
            ship_on_b1 = 1
            player_grid[row_1][column_b] = "1"
        if usr_ship_selection_input == "b2":
            ship_on_b2 = 1
            player_grid[row_2][column_b] = "1"
        if usr_ship_selection_input == "b3":
            ship_on_b3 = 1
            player_grid[row_3][column_b] = "1"
        if usr_ship_selection_input == "b4":
            ship_on_b4 = 1
            player_grid[row_4][column_b] = "1"
        if usr_ship_selection_input == "b5":
            ship_on_b5 = 1
            player_grid[row_5][column_b] = "1"
        if usr_ship_selection_input == "b6":
            ship_on_b6 = 1
            player_grid[row_6][column_b] = "1"
        if usr_ship_selection_input == "b7":
            ship_on_b7 = 1
            player_grid[row_7][column_b] = "1"
        if usr_ship_selection_input == "b8":
            ship_on_b8 = 1
            player_grid[row_8][column_b] = "1"
        
        global ship_on_c1,ship_on_c2,ship_on_c3,ship_on_c4,ship_on_c5,ship_on_c6,ship_on_c7,ship_on_c8
        if usr_ship_selection_input == "c1":
            ship_on_c1 = 1
            player_grid[row_1][column_c] = "1"
        if usr_ship_selection_input == "c2":
            ship_on_c2 = 1
            player_grid[row_2][column_c] = "1"
        if usr_ship_selection_input == "c3":
            ship_on_c3 = 1
            player_grid[row_3][column_c] = "1"
        if usr_ship_selection_input == "c4":
            ship_on_c4 = 1
            player_grid[row_4][column_c] = "1"
        if usr_ship_selection_input == "c5":
            ship_on_c5 = 1
            player_grid[row_5][column_c] = "1"
        if usr_ship_selection_input == "c6":
            ship_on_c6 = 1
            player_grid[row_6][column_c] = "1"
        if usr_ship_selection_input == "c7":
            ship_on_c7 = 1
            player_grid[row_7][column_c] = "1"
        if usr_ship_selection_input == "c8":
            ship_on_c8 = 1
            player_grid[row_8][column_c] = "1"
        
        global ship_on_d1,ship_on_d2,ship_on_d3,ship_on_d4,ship_on_d5,ship_on_d6,ship_on_d7,ship_on_d8
        if usr_ship_selection_input == "d1":
            ship_on_d1 = 1
            player_grid[row_1][column_d] = "1"
        if usr_ship_selection_input == "d2":
            ship_on_d2 = 1
            player_grid[row_2][column_d] = "1"
        if usr_ship_selection_input == "d3":
            ship_on_d3 = 1
            player_grid[row_3][column_d] = "1"
        if usr_ship_selection_input == "d4":
            ship_on_d4 = 1
            player_grid[row_4][column_d] = "1"
        if usr_ship_selection_input == "d5":
            ship_on_d5 = 1
            player_grid[row_5][column_d] = "1"
        if usr_ship_selection_input == "d6":
            ship_on_d6 = 1
            player_grid[row_6][column_d] = "1"
        if usr_ship_selection_input == "d7":
            ship_on_d7 = 1
            player_grid[row_7][column_d] = "1"
        if usr_ship_selection_input == "d8":
            ship_on_d8 = 1
            player_grid[row_8][column_d] = "1"
        
        global ship_on_e1,ship_on_e2,ship_on_e3,ship_on_e4,ship_on_e5,ship_on_e6,ship_on_e7,ship_on_e8
        if usr_ship_selection_input == "e1":
            ship_on_e1 = 1
            player_grid[row_1][column_e] = "1"
        if usr_ship_selection_input == "e2":
            ship_on_e2 = 1
            player_grid[row_2][column_e] = "1"
        if usr_ship_selection_input == "e3":
            ship_on_e3 = 1
            player_grid[row_3][column_e] = "1"
        if usr_ship_selection_input == "e4":
            ship_on_e4 = 1
            player_grid[row_4][column_e] = "1"
        if usr_ship_selection_input == "e5":
            ship_on_e5 = 1
            player_grid[row_5][column_e] = "1"
        if usr_ship_selection_input == "e6":
            ship_on_e6 = 1
            player_grid[row_6][column_e] = "1"
        if usr_ship_selection_input == "e7":
            ship_on_e7 = 1
            player_grid[row_7][column_e] = "1"
        if usr_ship_selection_input == "e8":
            ship_on_e8 = 1
            player_grid[row_8][column_e] = "1"
        
        global ship_on_f1,ship_on_f2,ship_on_f3,ship_on_f4,ship_on_f5,ship_on_f6,ship_on_f7,ship_on_f8
        if usr_ship_selection_input == "f1":
            ship_on_f1 = 1
            player_grid[row_1][column_f] = "1"
        if usr_ship_selection_input == "f2":
            ship_on_f2 = 1
            player_grid[row_2][column_f] = "1"
        if usr_ship_selection_input == "f3":
            ship_on_f3 = 1
            player_grid[row_3][column_f] = "1"
        if usr_ship_selection_input == "f4":
            ship_on_f4 = 1
            player_grid[row_4][column_f] = "1"
        if usr_ship_selection_input == "f5":
            ship_on_f5 = 1
            player_grid[row_5][column_f] = "1"
        if usr_ship_selection_input == "f6":
            ship_on_f6 = 1
            player_grid[row_6][column_f] = "1"
        if usr_ship_selection_input == "f7":
            ship_on_f7 = 1
            player_grid[row_7][column_f] = "1"
        if usr_ship_selection_input == "f8":
            ship_on_f8 = 1
            player_grid[row_8][column_f] = "1"
        
        global ship_on_g1,ship_on_g2,ship_on_g3,ship_on_g4,ship_on_g5,ship_on_g6,ship_on_g7,ship_on_g8
        if usr_ship_selection_input == "g1":
            ship_on_g1 = 1
            player_grid[row_1][column_g] = "1"
        if usr_ship_selection_input == "g2":
            ship_on_g2 = 1
            player_grid[row_2][column_g] = "1"
        if usr_ship_selection_input == "g3":
            ship_on_g3 = 1
            player_grid[row_3][column_g] = "1"
        if usr_ship_selection_input == "g4":
            ship_on_g4 = 1
            player_grid[row_4][column_g] = "1"
        if usr_ship_selection_input == "g5":
            ship_on_g5 = 1
            player_grid[row_5][column_g] = "1"
        if usr_ship_selection_input == "g6":
            ship_on_g6 = 1
            player_grid[row_6][column_g] = "1"
        if usr_ship_selection_input == "g7":
            ship_on_g7 = 1
            player_grid[row_7][column_g] = "1"
        if usr_ship_selection_input == "g8":
            ship_on_g8 = 1
            player_grid[row_8][column_g] = "1"
        
        global ship_on_h1,ship_on_h2,ship_on_h3,ship_on_h4,ship_on_h5,ship_on_h6,ship_on_h7,ship_on_h8
        if usr_ship_selection_input == "h1":
            ship_on_h1 = 1
            player_grid[row_1][column_h] = "1"
        if usr_ship_selection_input == "h2":
            ship_on_h2 = 1
            player_grid[row_2][column_h] = "1"
        if usr_ship_selection_input == "h3":
            ship_on_h3 = 1
            player_grid[row_3][column_h] = "1"
        if usr_ship_selection_input == "h4":
            ship_on_h4 = 1
            player_grid[row_4][column_h] = "1"
        if usr_ship_selection_input == "h5":
            ship_on_h5 = 1
            player_grid[row_5][column_h] = "1"
        if usr_ship_selection_input == "h6":
            ship_on_h6 = 1
            player_grid[row_6][column_h] = "1"
        if usr_ship_selection_input == "h7":
            ship_on_h7 = 1
            player_grid[row_7][column_h] = "1"
        if usr_ship_selection_input == "h8":
            ship_on_h8 = 1
            player_grid[row_8][column_h] = "1"

        if usr_ship_selection_input == "d":
            continue_with_loop = 0
        if usr_ship_selection_input == "D":
            continue_with_loop = 0
        if usr_ship_selection_input == "done":
            continue_with_loop = 0
        if usr_ship_selection_input =="Done":
            continue_with_loop = 0


# Define a function to create tracker varliables for the computers' ships
def set_enemy_ship_properties():
    # Globalize and define ship tracker variables for the a squares so they can be used in other functions
    global enemy_ship_on_a1,enemy_ship_on_a2,enemy_ship_on_a3,enemy_ship_on_a4,enemy_ship_on_a5,enemy_ship_on_a6,enemy_ship_on_a7,enemy_ship_on_a8
    enemy_ship_on_a1 = 0
    enemy_ship_on_a2 = 0
    enemy_ship_on_a3 = 0
    enemy_ship_on_a4 = 0
    enemy_ship_on_a5 = 0
    enemy_ship_on_a6 = 0
    enemy_ship_on_a7 = 0
    enemy_ship_on_a8 = 0

    # Globalize and define ship tracker variables for the b squares so they can be used in other functions
    global enemy_ship_on_b1,enemy_ship_on_b2,enemy_ship_on_b3,enemy_ship_on_b4,enemy_ship_on_b5,enemy_ship_on_b6,enemy_ship_on_b7,enemy_ship_on_b8
    enemy_ship_on_b1 = 0
    enemy_ship_on_b2 = 0
    enemy_ship_on_b3 = 0
    enemy_ship_on_b4 = 0
    enemy_ship_on_b5 = 0
    enemy_ship_on_b6 = 0
    enemy_ship_on_b7 = 0
    enemy_ship_on_b8 = 0

    # Globalize and define ship tracker variables for the c squares so they can be used in other functions
    global enemy_ship_on_c1,enemy_ship_on_c2,enemy_ship_on_c3,enemy_ship_on_c4,enemy_ship_on_c5,enemy_ship_on_c6,enemy_ship_on_c7,enemy_ship_on_c8
    enemy_ship_on_c1 = 0
    enemy_ship_on_c2 = 0
    enemy_ship_on_c3 = 0
    enemy_ship_on_c4 = 0
    enemy_ship_on_c5 = 0
    enemy_ship_on_c6 = 0
    enemy_ship_on_c7 = 0
    enemy_ship_on_c8 = 0

    # Globalize and define ship tracker variables for the d squares so they can be used in other functions
    global enemy_ship_on_d1,enemy_ship_on_d2,enemy_ship_on_d3,enemy_ship_on_d4,enemy_ship_on_d5,enemy_ship_on_d6,enemy_ship_on_d7,enemy_ship_on_d8
    enemy_ship_on_d1 = 0
    enemy_ship_on_d2 = 0
    enemy_ship_on_d3 = 0
    enemy_ship_on_d4 = 0
    enemy_ship_on_d5 = 0
    enemy_ship_on_d6 = 0
    enemy_ship_on_d7 = 0
    enemy_ship_on_d8 = 0

    # Globalize and define ship tracker variables for the e squares so they can be used in other functions
    global enemy_ship_on_e1,enemy_ship_on_e2,enemy_ship_on_e3,enemy_ship_on_e4,enemy_ship_on_e5,enemy_ship_on_e6,enemy_ship_on_e7,enemy_ship_on_e8
    enemy_ship_on_e1 = 0
    enemy_ship_on_e2 = 0
    enemy_ship_on_e3 = 0
    enemy_ship_on_e4 = 0
    enemy_ship_on_e5 = 0
    enemy_ship_on_e6 = 0
    enemy_ship_on_e7 = 0
    enemy_ship_on_e8 = 0

    # Globalize and define ship tracker variables for the f squares so they can be used in other functions
    global enemy_ship_on_f1,enemy_ship_on_f2,enemy_ship_on_f3,enemy_ship_on_f4,enemy_ship_on_f5,enemy_ship_on_f6,enemy_ship_on_f7,enemy_ship_on_f8
    enemy_ship_on_f1 = 0
    enemy_ship_on_f2 = 0
    enemy_ship_on_f3 = 0
    enemy_ship_on_f4 = 0
    enemy_ship_on_f5 = 0
    enemy_ship_on_f6 = 0
    enemy_ship_on_f7 = 0
    enemy_ship_on_f8 = 0

    # Globalize and define ship tracker variables for the g squares so they can be used in other functions
    global enemy_ship_on_g1,enemy_ship_on_g2,enemy_ship_on_g3,enemy_ship_on_g4,enemy_ship_on_g5,enemy_ship_on_g6,enemy_ship_on_g7,enemy_ship_on_g8
    enemy_ship_on_g1 = 0
    enemy_ship_on_g2 = 0
    enemy_ship_on_g3 = 0
    enemy_ship_on_g4 = 0
    enemy_ship_on_g5 = 0
    enemy_ship_on_g6 = 0
    enemy_ship_on_g7 = 0
    enemy_ship_on_g8 = 0

    # Globalize and define ship tracker variables for the h squares so they can be used in other functions
    global enemy_ship_on_h1,enemy_ship_on_h2,enemy_ship_on_h3,enemy_ship_on_h4,enemy_ship_on_h5,enemy_ship_on_h6,enemy_ship_on_h7,enemy_ship_on_h8
    enemy_ship_on_h1 = 0
    enemy_ship_on_h2 = 0
    enemy_ship_on_h3 = 0
    enemy_ship_on_h4 = 0
    enemy_ship_on_h5 = 0
    enemy_ship_on_h6 = 0
    enemy_ship_on_h7 = 0
    enemy_ship_on_h8 = 0


# Define a function to choose where the computer is going to place their ships
def get_enemy_ship_properties():
    global enemy_ship_cors
    enemy_ship_cors = []

    # Generate 10 random values for the coordinates of enemy ships and add them to the enemy coordinates list
    for i in range(10):
        rand_cor = rand.choice(coordinates_list)
        coordinates_list.remove(rand_cor)
        enemy_ship_cors.append(rand_cor)
    
    # Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print(enemy_ship_cors)
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_a1,enemy_ship_on_a2,enemy_ship_on_a3,enemy_ship_on_a4,enemy_ship_on_a4,enemy_ship_on_a5,enemy_ship_on_a6,enemy_ship_on_a7,enemy_ship_on_a8
    if "a1" in enemy_ship_cors:
        enemy_ship_on_a1 = 1
    if "a2" in enemy_ship_cors:
        enemy_ship_on_a2 = 1
    if "a3" in enemy_ship_cors:
        enemy_ship_on_a3 = 1
    if "a4" in enemy_ship_cors:
        enemy_ship_on_a4 = 1
    if "a5" in enemy_ship_cors:
        enemy_ship_on_a5 = 1
    if "a6" in enemy_ship_cors:
        enemy_ship_on_a6 = 1
    if "a7" in enemy_ship_cors:
        enemy_ship_on_a7 = 1
    if "a8" in enemy_ship_cors:
        enemy_ship_on_a8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_b1,enemy_ship_on_b2,enemy_ship_on_b3,enemy_ship_on_b4,enemy_ship_on_b4,enemy_ship_on_b5,enemy_ship_on_b6,enemy_ship_on_b7,enemy_ship_on_b8
    if "b1" in enemy_ship_cors:
        enemy_ship_on_b1 = 1
    if "b2" in enemy_ship_cors:
        enemy_ship_on_b2 = 1
    if "b3" in enemy_ship_cors:
        enemy_ship_on_b3 = 1
    if "b4" in enemy_ship_cors:
        enemy_ship_on_b4 = 1
    if "b5" in enemy_ship_cors:
        enemy_ship_on_b5 = 1
    if "b6" in enemy_ship_cors:
        enemy_ship_on_b6 = 1
    if "b7" in enemy_ship_cors:
        enemy_ship_on_b7 = 1
    if "b8" in enemy_ship_cors:
        enemy_ship_on_b8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_c1,enemy_ship_on_c2,enemy_ship_on_c3,enemy_ship_on_c4,enemy_ship_on_c4,enemy_ship_on_c5,enemy_ship_on_c6,enemy_ship_on_c7,enemy_ship_on_c8
    if "c1" in enemy_ship_cors:
        enemy_ship_on_c1 = 1
    if "c2" in enemy_ship_cors:
        enemy_ship_on_c2 = 1
    if "c3" in enemy_ship_cors:
        enemy_ship_on_c3 = 1
    if "c4" in enemy_ship_cors:
        enemy_ship_on_c4 = 1
    if "c5" in enemy_ship_cors:
        enemy_ship_on_c5 = 1
    if "c6" in enemy_ship_cors:
        enemy_ship_on_c6 = 1
    if "c7" in enemy_ship_cors:
        enemy_ship_on_c7 = 1
    if "c8" in enemy_ship_cors:
        enemy_ship_on_c8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_d1,enemy_ship_on_d2,enemy_ship_on_d3,enemy_ship_on_d4,enemy_ship_on_d4,enemy_ship_on_d5,enemy_ship_on_d6,enemy_ship_on_d7,enemy_ship_on_d8
    if "d1" in enemy_ship_cors:
        enemy_ship_on_d1 = 1
    if "d2" in enemy_ship_cors:
        enemy_ship_on_d2 = 1
    if "d3" in enemy_ship_cors:
        enemy_ship_on_d3 = 1
    if "d4" in enemy_ship_cors:
        enemy_ship_on_d4 = 1
    if "d5" in enemy_ship_cors:
        enemy_ship_on_d5 = 1
    if "d6" in enemy_ship_cors:
        enemy_ship_on_d6 = 1
    if "d7" in enemy_ship_cors:
        enemy_ship_on_d7 = 1
    if "d8" in enemy_ship_cors:
        enemy_ship_on_d8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_e1,enemy_ship_on_e2,enemy_ship_on_e3,enemy_ship_on_e4,enemy_ship_on_e4,enemy_ship_on_e5,enemy_ship_on_e6,enemy_ship_on_e7,enemy_ship_on_e8
    if "e1" in enemy_ship_cors:
        enemy_ship_on_e1 = 1
    if "e2" in enemy_ship_cors:
        enemy_ship_on_e2 = 1
    if "e3" in enemy_ship_cors:
        enemy_ship_on_e3 = 1
    if "e4" in enemy_ship_cors:
        enemy_ship_on_e4 = 1
    if "e5" in enemy_ship_cors:
        enemy_ship_on_e5 = 1
    if "e6" in enemy_ship_cors:
        enemy_ship_on_e6 = 1
    if "e7" in enemy_ship_cors:
        enemy_ship_on_e7 = 1
    if "e8" in enemy_ship_cors:
        enemy_ship_on_e8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_f1,enemy_ship_on_f2,enemy_ship_on_f3,enemy_ship_on_f4,enemy_ship_on_f4,enemy_ship_on_f5,enemy_ship_on_f6,enemy_ship_on_f7,enemy_ship_on_f8
    if "f1" in enemy_ship_cors:
        enemy_ship_on_f1 = 1
    if "f2" in enemy_ship_cors:
        enemy_ship_on_f2 = 1
    if "f3" in enemy_ship_cors:
        enemy_ship_on_f3 = 1
    if "f4" in enemy_ship_cors:
        enemy_ship_on_f4 = 1
    if "f5" in enemy_ship_cors:
        enemy_ship_on_f5 = 1
    if "f6" in enemy_ship_cors:
        enemy_ship_on_f6 = 1
    if "f7" in enemy_ship_cors:
        enemy_ship_on_f7 = 1
    if "f8" in enemy_ship_cors:
        enemy_ship_on_f8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_g1,enemy_ship_on_g2,enemy_ship_on_g3,enemy_ship_on_g4,enemy_ship_on_g4,enemy_ship_on_g5,enemy_ship_on_g6,enemy_ship_on_g7,enemy_ship_on_g8
    if "g1" in enemy_ship_cors:
        enemy_ship_on_g1 = 1
    if "g2" in enemy_ship_cors:
        enemy_ship_on_g2 = 1
    if "g3" in enemy_ship_cors:
        enemy_ship_on_g3 = 1
    if "g4" in enemy_ship_cors:
        enemy_ship_on_g4 = 1
    if "g5" in enemy_ship_cors:
        enemy_ship_on_g5 = 1
    if "g6" in enemy_ship_cors:
        enemy_ship_on_g6 = 1
    if "g7" in enemy_ship_cors:
        enemy_ship_on_g7 = 1
    if "g8" in enemy_ship_cors:
        enemy_ship_on_g8 = 1
    
    # Globalize and set enemy ship variables to contain ships if they are chosen from the random coordinates list
    global enemy_ship_on_h1,enemy_ship_on_h2,enemy_ship_on_h3,enemy_ship_on_h4,enemy_ship_on_h4,enemy_ship_on_h5,enemy_ship_on_h6,enemy_ship_on_h7,enemy_ship_on_h8
    if "h1" in enemy_ship_cors:
        enemy_ship_on_h1 = 1
    if "h2" in enemy_ship_cors:
        enemy_ship_on_h2 = 1
    if "h3" in enemy_ship_cors:
        enemy_ship_on_h3 = 1
    if "h4" in enemy_ship_cors:
        enemy_ship_on_h4 = 1
    if "h5" in enemy_ship_cors:
        enemy_ship_on_h5 = 1
    if "h6" in enemy_ship_cors:
        enemy_ship_on_h6 = 1
    if "h7" in enemy_ship_cors:
        enemy_ship_on_h7 = 1
    if "h8" in enemy_ship_cors:
        enemy_ship_on_h8 = 1


# Define a function to concisely set the grid properties
def set_grid_properties():
    # Globalize variables so other functions can access them
    global x_offset,y_offset,clicker_cors_list,number_of_sides,number_of_squares,squares_per_side,number_of_squares_on_side,width_of_side,width_of_square

    # Define variables that will determine the size and shape of the battleship grid
    number_of_sides = 4
    number_of_squares = 64
    squares_per_side = 8
    number_of_squares_on_side = number_of_squares / squares_per_side
    width_of_side = 520
    width_of_square = width_of_side / squares_per_side
    x_offset = -1 # Turtles aren't perfectly centered, so this variable will be used to realign them
    y_offset = 1 # Turtles aren't perfectly centered, so this variable will be used to realign them

    # Create an empty list to store the values of coordinates
    clicker_cors_list = []

    # Define coordinates on the turtle graphics grid for every single square and create a list to store them, adding each coordinate
    # This will be defining the locations of squares the user will be interacting with
    # They will be globalized so they can be accessed in other functions
    global a1_xcor,a1_ycor,a1_cors
    a1_xcor = (-0.5 * width_of_side) + (0.5 * width_of_square) + x_offset
    a1_ycor = (-0.5 * width_of_side) + (0.5 * width_of_square) + y_offset
    a1_cors = a1_xcor, a1_ycor
    clicker_cors_list.append(a1_cors)

    # Define a2's coordinates
    global a2_xcor,a2_ycor,a2_cors
    a2_xcor = a1_xcor + 0
    a2_ycor = a1_ycor + width_of_square
    a2_cors = a2_xcor, a2_ycor
    clicker_cors_list.append(a2_cors)

    # Define a3's coordinates
    global a3_xcor,a3_ycor,a3_cors
    a3_xcor = a2_xcor + 0
    a3_ycor = a2_ycor + width_of_square
    a3_cors = a3_xcor, a3_ycor
    clicker_cors_list.append(a3_cors)

    # Define a4's coordinates
    global a4_xcor,a4_ycor,a4_cors
    a4_xcor = a3_xcor + 0
    a4_ycor = a3_ycor + width_of_square
    a4_cors = a4_xcor, a4_ycor
    clicker_cors_list.append(a4_cors)

    # Define a5's coordinates
    global a5_xcor,a5_ycor,a5_cors
    a5_xcor = a4_xcor + 0
    a5_ycor = a4_ycor + width_of_square
    a5_cors = a5_xcor, a5_ycor
    clicker_cors_list.append(a5_cors)

    # Define a6's coordinates
    global a6_xcor,a6_ycor,a6_cors
    a6_xcor = a5_xcor + 0
    a6_ycor = a5_ycor + width_of_square
    a6_cors = a6_xcor, a6_ycor
    clicker_cors_list.append(a6_cors)

    # Define a7's coordinates
    global a7_xcor,a7_ycor,a7_cors
    a7_xcor = a6_xcor + 0
    a7_ycor = a6_ycor + width_of_square
    a7_cors = a7_xcor, a7_ycor
    clicker_cors_list.append(a7_cors)

    # Define a8's coordinates
    global a8_xcor,a8_ycor,a8_cors
    a8_xcor = a7_xcor + 0
    a8_ycor = a7_ycor + width_of_square
    a8_cors = a8_xcor, a8_ycor
    clicker_cors_list.append(a8_cors)

    # Define b1's coordinates
    global b1_xcor,b1_ycor,b1_cors
    b1_xcor = a1_xcor + width_of_square
    b1_ycor = a1_ycor + 0
    b1_cors = b1_xcor, b1_ycor
    clicker_cors_list.append(b1_cors)

    # Define b2's coordinates
    global b2_xcor,b2_ycor,b2_cors
    b2_xcor = b1_xcor + 0
    b2_ycor = b1_ycor + width_of_square
    b2_cors = b2_xcor, b2_ycor
    clicker_cors_list.append(b2_cors)

    # Define b3's coordinates
    global b3_xcor,b3_ycor,b3_cors
    b3_xcor = b2_xcor + 0
    b3_ycor = b2_ycor + width_of_square
    b3_cors = b3_xcor, b3_ycor
    clicker_cors_list.append(b3_cors)

    # Define b4's coordinates
    global b4_xcor,b4_ycor,b4_cors
    b4_xcor = b3_xcor + 0
    b4_ycor = b3_ycor + width_of_square
    b4_cors = b4_xcor, b4_ycor
    clicker_cors_list.append(b4_cors)

    # Define b5's coordinates
    global b5_xcor,b5_ycor,b5_cors
    b5_xcor = b4_xcor + 0
    b5_ycor = b4_ycor + width_of_square
    b5_cors = b5_xcor, b5_ycor
    clicker_cors_list.append(b5_cors)

    # Define b6's coordinates
    global b6_xcor,b6_ycor,b6_cors
    b6_xcor = b5_xcor + 0
    b6_ycor = b5_ycor + width_of_square
    b6_cors = b6_xcor, b6_ycor
    clicker_cors_list.append(b6_cors)

    # Define b7's coordinates
    global b7_xcor,b7_ycor,b7_cors
    b7_xcor = b6_xcor + 0
    b7_ycor = b6_ycor + width_of_square
    b7_cors = b7_xcor, b7_ycor
    clicker_cors_list.append(b7_cors)

    # Define b8's coordinates
    global b8_xcor,b8_ycor,b8_cors
    b8_xcor = b7_xcor + 0
    b8_ycor = b7_ycor + width_of_square
    b8_cors = b8_xcor, b8_ycor
    clicker_cors_list.append(b8_cors)

    # Define c1's coordinates
    global c1_xcor,c1_ycor,c1_cors
    c1_xcor = b1_xcor + width_of_square
    c1_ycor = b1_ycor + 0
    c1_cors = c1_xcor, c1_ycor
    clicker_cors_list.append(c1_cors)

    # Define c2's coordinates
    global c2_xcor,c2_ycor,c2_cors
    c2_xcor = c1_xcor + 0
    c2_ycor = c1_ycor + width_of_square
    c2_cors = c2_xcor, c2_ycor
    clicker_cors_list.append(c2_cors)

    # Define c3's coordinates
    global c3_xcor,c3_ycor,c3_cors
    c3_xcor = c2_xcor + 0
    c3_ycor = c2_ycor + width_of_square
    c3_cors = c3_xcor, c3_ycor
    clicker_cors_list.append(c3_cors)

    # Define c4's coordinates
    global c4_xcor,c4_ycor,c4_cors
    c4_xcor = c3_xcor + 0
    c4_ycor = c3_ycor + width_of_square
    c4_cors = c4_xcor, c4_ycor
    clicker_cors_list.append(c4_cors)

    # Define c5's coordinates
    global c5_xcor,c5_ycor,c5_cors
    c5_xcor = c4_xcor + 0
    c5_ycor = c4_ycor + width_of_square
    c5_cors = c5_xcor, c5_ycor
    clicker_cors_list.append(c5_cors)

    # Define c6's coordinates
    global c6_xcor,c6_ycor,c6_cors
    c6_xcor = c5_xcor + 0
    c6_ycor = c5_ycor + width_of_square
    c6_cors = c6_xcor, c6_ycor
    clicker_cors_list.append(c6_cors)

    # Define c7's coordinates
    global c7_xcor,c7_ycor,c7_cors
    c7_xcor = c6_xcor + 0
    c7_ycor = c6_ycor + width_of_square
    c7_cors = c7_xcor, c7_ycor
    clicker_cors_list.append(c7_cors)

    # Define c8's coordinates
    global c8_xcor,c8_ycor,c8_cors
    c8_xcor = c7_xcor + 0
    c8_ycor = c7_ycor + width_of_square
    c8_cors = c8_xcor, c8_ycor
    clicker_cors_list.append(c8_cors)

    # Define d1's coordinates
    global d1_xcor,d1_ycor,d1_cors
    d1_xcor = c1_xcor + width_of_square
    d1_ycor = c1_ycor + 0
    d1_cors = d1_xcor, d1_ycor
    clicker_cors_list.append(d1_cors)

    # Define d2's coordinates
    global d2_xcor,d2_ycor,d2_cors
    d2_xcor = d1_xcor + 0
    d2_ycor = d1_ycor + width_of_square
    d2_cors = d2_xcor, d2_ycor
    clicker_cors_list.append(d2_cors)

    # Define d3's coordinates
    global d3_xcor,d3_ycor,d3_cors
    d3_xcor = d2_xcor + 0
    d3_ycor = d2_ycor + width_of_square
    d3_cors = d3_xcor, d3_ycor
    clicker_cors_list.append(d3_cors)

    # Define d4's coordinates
    global d4_xcor,d4_ycor,d4_cors
    d4_xcor = d3_xcor + 0
    d4_ycor = d3_ycor + width_of_square
    d4_cors = d4_xcor, d4_ycor
    clicker_cors_list.append(d4_cors)

    # Define d5's coordinates
    global d5_xcor,d5_ycor,d5_cors
    d5_xcor = d4_xcor + 0
    d5_ycor = d4_ycor + width_of_square
    d5_cors = d5_xcor, d5_ycor
    clicker_cors_list.append(d5_cors)

    # Define d6's coordinates
    global d6_xcor,d6_ycor,d6_cors
    d6_xcor = d5_xcor + 0
    d6_ycor = d5_ycor + width_of_square
    d6_cors = d6_xcor, d6_ycor
    clicker_cors_list.append(d6_cors)

    # Define d7's coordinates
    global d7_xcor,d7_ycor,d7_cors
    d7_xcor = d6_xcor + 0
    d7_ycor = d6_ycor + width_of_square
    d7_cors = d7_xcor, d7_ycor
    clicker_cors_list.append(d7_cors)

    # Define d8's coordinates
    global d8_xcor,d8_ycor,d8_cors
    d8_xcor = d7_xcor + 0
    d8_ycor = d7_ycor + width_of_square
    d8_cors = d8_xcor, d8_ycor
    clicker_cors_list.append(d8_cors)

    # Define e1's coordinates
    global e1_xcor,e1_ycor,e1_cors
    e1_xcor = d1_xcor + width_of_square
    e1_ycor = d1_ycor + 0
    e1_cors = e1_xcor, e1_ycor
    clicker_cors_list.append(e1_cors)

    # Define e2's coordinates
    global e2_xcor,e2_ycor,e2_cors
    e2_xcor = e1_xcor + 0
    e2_ycor = e1_ycor + width_of_square
    e2_cors = e2_xcor, e2_ycor
    clicker_cors_list.append(e2_cors)

    # Define e3's coordinates
    global e3_xcor,e3_ycor,e3_cors
    e3_xcor = e2_xcor + 0
    e3_ycor = e2_ycor + width_of_square
    e3_cors = e3_xcor, e3_ycor
    clicker_cors_list.append(e3_cors)

    # Define e4's coordinates
    global e4_xcor,e4_ycor,e4_cors
    e4_xcor = e3_xcor + 0
    e4_ycor = e3_ycor + width_of_square
    e4_cors = e4_xcor, e4_ycor
    clicker_cors_list.append(e4_cors)

    # Define e5's coordinates
    global e5_xcor,e5_ycor,e5_cors
    e5_xcor = e4_xcor + 0
    e5_ycor = e4_ycor + width_of_square
    e5_cors = e5_xcor, e5_ycor
    clicker_cors_list.append(e5_cors)

    # Define e6's coordinates
    global e6_xcor,e6_ycor,e6_cors
    e6_xcor = e5_xcor + 0
    e6_ycor = e5_ycor + width_of_square
    e6_cors = e6_xcor, e6_ycor
    clicker_cors_list.append(e6_cors)

    # Define e7's coordinates
    global e7_xcor,e7_ycor,e7_cors
    e7_xcor = e6_xcor + 0
    e7_ycor = e6_ycor + width_of_square
    e7_cors = e7_xcor, e7_ycor
    clicker_cors_list.append(e7_cors)

    # Define e8's coordinates
    global e8_xcor,e8_ycor,e8_cors
    e8_xcor = e7_xcor + 0
    e8_ycor = e7_ycor + width_of_square
    e8_cors = e8_xcor, e8_ycor
    clicker_cors_list.append(e8_cors)

    # Define f1's coordinates
    global f1_xcor,f1_ycor,f1_cors
    f1_xcor = e1_xcor + width_of_square
    f1_ycor = e1_ycor + 0
    f1_cors = f1_xcor, f1_ycor
    clicker_cors_list.append(f1_cors)

    # Define f2's coordinates
    global f2_xcor,f2_ycor,f2_cors
    f2_xcor = f1_xcor + 0
    f2_ycor = f1_ycor + width_of_square
    f2_cors = f2_xcor, f2_ycor
    clicker_cors_list.append(f2_cors)

    # Define f3's coordinates
    global f3_xcor,f3_ycor,f3_cors
    f3_xcor = f2_xcor + 0
    f3_ycor = f2_ycor + width_of_square
    f3_cors = f3_xcor, f3_ycor
    clicker_cors_list.append(f3_cors)

    # Define f4's coordinates
    global f4_xcor,f4_ycor,f4_cors
    f4_xcor = f3_xcor + 0
    f4_ycor = f3_ycor + width_of_square
    f4_cors = f4_xcor, f4_ycor
    clicker_cors_list.append(f4_cors)

    # Define f5's coordinates
    global f5_xcor,f5_ycor,f5_cors
    f5_xcor = f4_xcor + 0
    f5_ycor = f4_ycor + width_of_square
    f5_cors = f5_xcor, f5_ycor
    clicker_cors_list.append(f5_cors)

    # Define f6's coordinates
    global f6_xcor,f6_ycor,f6_cors
    f6_xcor = f5_xcor + 0
    f6_ycor = f5_ycor + width_of_square
    f6_cors = f6_xcor, f6_ycor
    clicker_cors_list.append(f6_cors)

    # Define f7's coordinates
    global f7_xcor,f7_ycor,f7_cors
    f7_xcor = f6_xcor + 0
    f7_ycor = f6_ycor + width_of_square
    f7_cors = f7_xcor, f7_ycor
    clicker_cors_list.append(f7_cors)

    # Define f8's coordinates
    global f8_xcor,f8_ycor,f8_cors
    f8_xcor = f7_xcor + 0
    f8_ycor = f7_ycor + width_of_square
    f8_cors = f8_xcor, f8_ycor
    clicker_cors_list.append(f8_cors)

    # Define g1's coordinates
    global g1_xcor,g1_ycor,g1_cors
    g1_xcor = f1_xcor + width_of_square
    g1_ycor = f1_ycor + 0
    g1_cors = g1_xcor, g1_ycor
    clicker_cors_list.append(g1_cors)

    # Define g2's coordinates
    global g2_xcor,g2_ycor,g2_cors
    g2_xcor = g1_xcor + 0
    g2_ycor = g1_ycor + width_of_square
    g2_cors = g2_xcor, g2_ycor
    clicker_cors_list.append(g2_cors)

    # Define g3's coordinates
    global g3_xcor,g3_ycor,g3_cors
    g3_xcor = g2_xcor + 0
    g3_ycor = g2_ycor + width_of_square
    g3_cors = g3_xcor, g3_ycor
    clicker_cors_list.append(g3_cors)

    # Define g4's coordinates
    global g4_xcor,g4_ycor,g4_cors
    g4_xcor = g3_xcor + 0
    g4_ycor = g3_ycor + width_of_square
    g4_cors = g4_xcor, g4_ycor
    clicker_cors_list.append(g4_cors)

    # Define g5's coordinates
    global g5_xcor,g5_ycor,g5_cors
    g5_xcor = g4_xcor + 0
    g5_ycor = g4_ycor + width_of_square
    g5_cors = g5_xcor, g5_ycor
    clicker_cors_list.append(g5_cors)

    # Define g6's coordinates
    global g6_xcor,g6_ycor,g6_cors
    g6_xcor = g5_xcor + 0
    g6_ycor = g5_ycor + width_of_square
    g6_cors = g6_xcor, g6_ycor
    clicker_cors_list.append(g6_cors)

    # Define g7's coordinates
    global g7_xcor,g7_ycor,g7_cors
    g7_xcor = g6_xcor + 0
    g7_ycor = g6_ycor + width_of_square
    g7_cors = g7_xcor, g7_ycor
    clicker_cors_list.append(g7_cors)

    # Define g8's coordinates
    global g8_xcor,g8_ycor,g8_cors
    g8_xcor = g7_xcor + 0
    g8_ycor = g7_ycor + width_of_square
    g8_cors = g8_xcor, g8_ycor
    clicker_cors_list.append(g8_cors)

    # Define h1's coordinates
    global h1_xcor,h1_ycor,h1_cors
    h1_xcor = g1_xcor + width_of_square
    h1_ycor = g1_ycor + 0
    h1_cors = h1_xcor, h1_ycor
    clicker_cors_list.append(h1_cors)

    # Define h2's coordinates
    global h2_xcor,h2_ycor,h2_cors
    h2_xcor = h1_xcor + 0
    h2_ycor = h1_ycor + width_of_square
    h2_cors = h2_xcor, h2_ycor
    clicker_cors_list.append(h2_cors)

    # Define h3's coordinates
    global h3_xcor,h3_ycor,h3_cors
    h3_xcor = h2_xcor + 0
    h3_ycor = h2_ycor + width_of_square
    h3_cors = h3_xcor, h3_ycor
    clicker_cors_list.append(h3_cors)

    # Define h4's coordinates
    global h4_xcor,h4_ycor,h4_cors
    h4_xcor = h3_xcor + 0
    h4_ycor = h3_ycor + width_of_square
    h4_cors = h4_xcor, h4_ycor
    clicker_cors_list.append(h4_cors)

    # Define h5's coordinates
    global h5_xcor,h5_ycor,h5_cors
    h5_xcor = h4_xcor + 0
    h5_ycor = h4_ycor + width_of_square
    h5_cors = h5_xcor, h5_ycor
    clicker_cors_list.append(h5_cors)

    # Define h6's coordinates
    global h6_xcor,h6_ycor,h6_cors
    h6_xcor = h5_xcor + 0
    h6_ycor = h5_ycor + width_of_square
    h6_cors = h6_xcor, h6_ycor
    clicker_cors_list.append(h6_cors)

    # Define h7's coordinates
    global h7_xcor,h7_ycor,h7_cors
    h7_xcor = h6_xcor + 0
    h7_ycor = h6_ycor + width_of_square
    h7_cors = h7_xcor, h7_ycor
    clicker_cors_list.append(h7_cors)

    # Define h8's coordinates
    global h8_xcor,h8_ycor,h8_cors
    h8_xcor = h7_xcor + 0
    h8_ycor = h7_ycor + width_of_square
    h8_cors = h8_xcor, h8_ycor
    clicker_cors_list.append(h8_cors)


# Define a function to generate a turtle object for each square to detect if it is clicked
def create_grid_clickers():
    # Create a globalized list of all the clickers to easily allow actions to be done on all of them from anywheree
    global master_clickers_list
    master_clickers_list = []

    # Globalize and create turtle objects that the user can click for the a squares, adding them to the master list
    global a1_clicker,a2_clicker,a3_clicker,a4_clicker,a5_clicker,a6_clicker,a7_clicker,a8_clicker
    a1_clicker = trtl.Turtle()
    a2_clicker = trtl.Turtle()
    a3_clicker = trtl.Turtle()
    a4_clicker = trtl.Turtle()
    a5_clicker = trtl.Turtle()
    a6_clicker = trtl.Turtle()
    a7_clicker = trtl.Turtle()
    a8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(a1_clicker)
    master_clickers_list.append(a2_clicker)
    master_clickers_list.append(a3_clicker)
    master_clickers_list.append(a4_clicker)
    master_clickers_list.append(a5_clicker)
    master_clickers_list.append(a6_clicker)
    master_clickers_list.append(a7_clicker)
    master_clickers_list.append(a8_clicker)

    # Globalize and create turtle objects that the user can click for the b squares
    global b1_clicker,b2_clicker,b3_clicker,b4_clicker,b5_clicker,b6_clicker,b7_clicker,b8_clicker
    b1_clicker = trtl.Turtle()
    b2_clicker = trtl.Turtle()
    b3_clicker = trtl.Turtle()
    b4_clicker = trtl.Turtle()
    b5_clicker = trtl.Turtle()
    b6_clicker = trtl.Turtle()
    b7_clicker = trtl.Turtle()
    b8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(b1_clicker)
    master_clickers_list.append(b2_clicker)
    master_clickers_list.append(b3_clicker)
    master_clickers_list.append(b4_clicker)
    master_clickers_list.append(b5_clicker)
    master_clickers_list.append(b6_clicker)
    master_clickers_list.append(b7_clicker)
    master_clickers_list.append(b8_clicker)

    # Globalize and create turtle objects that the user can click for the c squares
    global c1_clicker,c2_clicker,c3_clicker,c4_clicker,c5_clicker,c6_clicker,c7_clicker,c8_clicker
    c1_clicker = trtl.Turtle()
    c2_clicker = trtl.Turtle()
    c3_clicker = trtl.Turtle()
    c4_clicker = trtl.Turtle()
    c5_clicker = trtl.Turtle()
    c6_clicker = trtl.Turtle()
    c7_clicker = trtl.Turtle()
    c8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(c1_clicker)
    master_clickers_list.append(c2_clicker)
    master_clickers_list.append(c3_clicker)
    master_clickers_list.append(c4_clicker)
    master_clickers_list.append(c5_clicker)
    master_clickers_list.append(c6_clicker)
    master_clickers_list.append(c7_clicker)
    master_clickers_list.append(c8_clicker)

    # Globalize and create turtle objects that the user can click for the d squares
    global d1_clicker,d2_clicker,d3_clicker,d4_clicker,d5_clicker,d6_clicker,d7_clicker,d8_clicker
    d1_clicker = trtl.Turtle()
    d2_clicker = trtl.Turtle()
    d3_clicker = trtl.Turtle()
    d4_clicker = trtl.Turtle()
    d5_clicker = trtl.Turtle()
    d6_clicker = trtl.Turtle()
    d7_clicker = trtl.Turtle()
    d8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(d1_clicker)
    master_clickers_list.append(d2_clicker)
    master_clickers_list.append(d3_clicker)
    master_clickers_list.append(d4_clicker)
    master_clickers_list.append(d5_clicker)
    master_clickers_list.append(d6_clicker)
    master_clickers_list.append(d7_clicker)
    master_clickers_list.append(d8_clicker)

    # Globalize and create turtle objects that the user can click for the e squares
    global e1_clicker,e2_clicker,e3_clicker,e4_clicker,e5_clicker,e6_clicker,e7_clicker,e8_clicker
    e1_clicker = trtl.Turtle()
    e2_clicker = trtl.Turtle()
    e3_clicker = trtl.Turtle()
    e4_clicker = trtl.Turtle()
    e5_clicker = trtl.Turtle()
    e6_clicker = trtl.Turtle()
    e7_clicker = trtl.Turtle()
    e8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(e1_clicker)
    master_clickers_list.append(e2_clicker)
    master_clickers_list.append(e3_clicker)
    master_clickers_list.append(e4_clicker)
    master_clickers_list.append(e5_clicker)
    master_clickers_list.append(e6_clicker)
    master_clickers_list.append(e7_clicker)
    master_clickers_list.append(e8_clicker)

    # Globalize and create turtle objects that the user can click for the f squares
    global f1_clicker,f2_clicker,f3_clicker,f4_clicker,f5_clicker,f6_clicker,f7_clicker,f8_clicker
    f1_clicker = trtl.Turtle()
    f2_clicker = trtl.Turtle()
    f3_clicker = trtl.Turtle()
    f4_clicker = trtl.Turtle()
    f5_clicker = trtl.Turtle()
    f6_clicker = trtl.Turtle()
    f7_clicker = trtl.Turtle()
    f8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(f1_clicker)
    master_clickers_list.append(f2_clicker)
    master_clickers_list.append(f3_clicker)
    master_clickers_list.append(f4_clicker)
    master_clickers_list.append(f5_clicker)
    master_clickers_list.append(f6_clicker)
    master_clickers_list.append(f7_clicker)
    master_clickers_list.append(f8_clicker)

    # Globalize and create turtle objects that the user can click for the g squares
    global g1_clicker,g2_clicker,g3_clicker,g4_clicker,g5_clicker,g6_clicker,g7_clicker,g8_clicker
    g1_clicker = trtl.Turtle()
    g2_clicker = trtl.Turtle()
    g3_clicker = trtl.Turtle()
    g4_clicker = trtl.Turtle()
    g5_clicker = trtl.Turtle()
    g6_clicker = trtl.Turtle()
    g7_clicker = trtl.Turtle()
    g8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(g1_clicker)
    master_clickers_list.append(g2_clicker)
    master_clickers_list.append(g3_clicker)
    master_clickers_list.append(g4_clicker)
    master_clickers_list.append(g5_clicker)
    master_clickers_list.append(g6_clicker)
    master_clickers_list.append(g7_clicker)
    master_clickers_list.append(g8_clicker)

    # Globalize and create turtle objects that the user can click for the h squares
    global h1_clicker,h2_clicker,h3_clicker,h4_clicker,h5_clicker,h6_clicker,h7_clicker,h8_clicker
    h1_clicker = trtl.Turtle()
    h2_clicker = trtl.Turtle()
    h3_clicker = trtl.Turtle()
    h4_clicker = trtl.Turtle()
    h5_clicker = trtl.Turtle()
    h6_clicker = trtl.Turtle()
    h7_clicker = trtl.Turtle()
    h8_clicker = trtl.Turtle()

    # Add the turtle objects to the master list
    master_clickers_list.append(h1_clicker)
    master_clickers_list.append(h2_clicker)
    master_clickers_list.append(h3_clicker)
    master_clickers_list.append(h4_clicker)
    master_clickers_list.append(h5_clicker)
    master_clickers_list.append(h6_clicker)
    master_clickers_list.append(h7_clicker)
    master_clickers_list.append(h8_clicker)


# Define a function to apply properties to the grid clickers
def apply_grid_clicker_properties():
    # For loop to apply properties to every turtle in the list
    for i in range(len(master_clickers_list)):
        master_clickers_list[i].penup() # Move the objects' pens up so they don't leave behind tracers
        master_clickers_list[i].speed(0) # Get the objects to their starting positions as soon as possible
        master_clickers_list[i].fillcolor("white")
        master_clickers_list[i].shape("square") # Set the shape of each clicker object
        master_clickers_list[i].shapesize(3) # Set the shapesize of each clicker object
        master_clickers_list[i].goto(clicker_cors_list[i]) # Send each clicker object to its respective square


# Define a function that will print out the grid of ships the user selected in the terminal
def print_user_grid(player_grid):
    for row in player_grid:
        print((" ").join(row))

# Define a function to run when a certain clicker is clicked
def a1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def a8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("a8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def b8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("b8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def c8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("c8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def d8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("d8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def e8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("e8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def f8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("f8_clicker clicked")
# Define a function to run when a certain clicker is clicked
def g1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def g8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("g8_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h1_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h1_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h2_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h2_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h3_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h3_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h4_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h4_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h5_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h5_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h6_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h6_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h7_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h7_clicker clicked")

# Define a function to run when a certain clicker is clicked
def h8_clicker_clicked(x,y):
    if developer_mode == 1:
        print("h8_clicker clicked")

#####-Setup-#####
# Create a list of possible coordinates for the user and enemy's ships to be on
create_coordinates_list()

# Create the grid of letters and numbers that will be used to show the player's board
create_user_grid()

# Set the initial locations and get the locations for where the user wants to place their ship
set_user_ship_properties()
get_user_ship_properties()

# Set the initial locations and get the locations for where the computer wants to place their ship
set_enemy_ship_properties()
get_enemy_ship_properties()

# Call the function to define coordinates for the graphical display
set_grid_properties()

# Call the function to create all of the objects a user can click on and apply their properties
create_grid_clickers()
apply_grid_clicker_properties()

# Print out the initial grid of the user
print_user_grid(player_grid)


# Create a screen for graphical display, set its background
import grid as grid
wn = trtl.Screen()
wn.bgpic("background.gif")

#Draw the grid on screen
grid.draw_grid()


#####-Game Handling-#####
# Wait for user to click which square they want to attack
a1_clicker.onclick(a1_clicker_clicked)
a2_clicker.onclick(a2_clicker_clicked)
a3_clicker.onclick(a3_clicker_clicked)
a4_clicker.onclick(a4_clicker_clicked)
a5_clicker.onclick(a5_clicker_clicked)
a6_clicker.onclick(a6_clicker_clicked)
a7_clicker.onclick(a7_clicker_clicked)
a8_clicker.onclick(a8_clicker_clicked)
b1_clicker.onclick(b1_clicker_clicked)
b2_clicker.onclick(b2_clicker_clicked)
b3_clicker.onclick(b3_clicker_clicked)
b4_clicker.onclick(b4_clicker_clicked)
b5_clicker.onclick(b5_clicker_clicked)
b6_clicker.onclick(b6_clicker_clicked)
b7_clicker.onclick(b7_clicker_clicked)
b8_clicker.onclick(b8_clicker_clicked)
c1_clicker.onclick(c1_clicker_clicked)
c2_clicker.onclick(c2_clicker_clicked)
c3_clicker.onclick(c3_clicker_clicked)
c4_clicker.onclick(c4_clicker_clicked)
c5_clicker.onclick(c5_clicker_clicked)
c6_clicker.onclick(c6_clicker_clicked)
c7_clicker.onclick(c7_clicker_clicked)
c8_clicker.onclick(c8_clicker_clicked)
d1_clicker.onclick(d1_clicker_clicked)
d2_clicker.onclick(d2_clicker_clicked)
d3_clicker.onclick(d3_clicker_clicked)
d4_clicker.onclick(d4_clicker_clicked)
d5_clicker.onclick(d5_clicker_clicked)
d6_clicker.onclick(d6_clicker_clicked)
d7_clicker.onclick(d7_clicker_clicked)
d8_clicker.onclick(d8_clicker_clicked)
e1_clicker.onclick(e1_clicker_clicked)
e2_clicker.onclick(e2_clicker_clicked)
e3_clicker.onclick(e3_clicker_clicked)
e4_clicker.onclick(e4_clicker_clicked)
e5_clicker.onclick(e5_clicker_clicked)
e6_clicker.onclick(e6_clicker_clicked)
e7_clicker.onclick(e7_clicker_clicked)
e8_clicker.onclick(e8_clicker_clicked)
f1_clicker.onclick(f1_clicker_clicked)
f2_clicker.onclick(f2_clicker_clicked)
f3_clicker.onclick(f3_clicker_clicked)
f4_clicker.onclick(f4_clicker_clicked)
f5_clicker.onclick(f5_clicker_clicked)
f6_clicker.onclick(f6_clicker_clicked)
f7_clicker.onclick(f7_clicker_clicked)
f8_clicker.onclick(f8_clicker_clicked)
g1_clicker.onclick(g1_clicker_clicked)
g2_clicker.onclick(g2_clicker_clicked)
g3_clicker.onclick(g3_clicker_clicked)
g4_clicker.onclick(g4_clicker_clicked)
g5_clicker.onclick(g5_clicker_clicked)
g6_clicker.onclick(g6_clicker_clicked)
g7_clicker.onclick(g7_clicker_clicked)
g8_clicker.onclick(g8_clicker_clicked)
h1_clicker.onclick(h1_clicker_clicked)
h2_clicker.onclick(h2_clicker_clicked)
h3_clicker.onclick(h3_clicker_clicked)
h4_clicker.onclick(h4_clicker_clicked)
h5_clicker.onclick(h5_clicker_clicked)
h6_clicker.onclick(h6_clicker_clicked)
h7_clicker.onclick(h7_clicker_clicked)
h8_clicker.onclick(h8_clicker_clicked)



# Keep display running and persistent, listening for user inputs
wn.listen()
wn.mainloop()