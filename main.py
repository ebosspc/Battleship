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


#####-Setup-#####
# Call the function to define coordinates for the graphical display
set_grid_properties()

# Call the function to create all of the objects a user can click on and apply their properties
create_grid_clickers()
apply_grid_clicker_properties()

# Create a screen for graphical display, set its background
import grid as grid
wn = trtl.Screen()
wn.bgpic("background.gif")

#Draw the grid on screen
grid.draw_grid()


#####-Game Handling-#####



# Keep display running and persistent, listening for user inputs
wn.listen()
wn.mainloop()