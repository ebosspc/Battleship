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
#Define variables that will determine the size and shape of the battleship grid
number_of_sides = 4
number_of_squares = 100
number_of_squares_on_side = number_of_squares / 10
width_of_side = 520
width_of_square = width_of_side / 10

#Define coordinates on the turtle graphics grid for every single square
a1_xcor = -260 + 0.5 * width_of_square
a1_ycor = -260 + 0.5 * width_of_square
a1_cors = a1_xcor, a1_ycor

# Define a2's coordinates
a2_xcor = a1_xcor + 0
a2_ycor = a1_ycor + width_of_square
a2_cors = a2_xcor, a2_ycor

# Define a3's coordinates
a3_xcor = a2_xcor + 0
a3_ycor = a2_ycor + width_of_square
a3_cors = a3_xcor, a3_ycor

# Define a4's coordinates
a4_xcor = a3_xcor + 0
a4_ycor = a3_ycor + width_of_square
a4_cors = a4_xcor, a4_ycor

# Define a5's coordinates
a5_xcor = a4_xcor + 0
a5_ycor = a4_ycor + width_of_square
a5_cors = a5_xcor, a5_ycor

# Define a6's coordinates
a6_xcor = a5_xcor + 0
a6_ycor = a5_ycor + width_of_square
a6_cors = a6_xcor, a6_ycor

# Define a7's coordinates
a7_xcor = a6_xcor + 0
a7_ycor = a6_ycor + width_of_square
a7_cors = a7_xcor, a7_ycor

# Define a8's coordinates
a8_xcor = a7_xcor + 0
a8_ycor = a7_ycor + width_of_square
a8_cors = a8_xcor, a8_ycor

# Define b1's coordinates
b1_xcor = a1_xcor + width_of_square
b1_ycor = a1_ycor + 0
b1_cors = b1_xcor, b1_ycor

# Define b2's coordinates
b2_xcor = b1_xcor + 0
b2_ycor = b1_ycor + width_of_square
b2_cors = b2_xcor, b2_ycor

# Define b3's coordinates
b3_xcor = b2_xcor + 0
b3_ycor = b2_ycor + width_of_square
b3_cors = b3_xcor, b3_ycor

# Define b4's coordinates
b4_xcor = b3_xcor + 0
b4_ycor = b3_ycor + width_of_square
b4_cors = b4_xcor, b4_ycor

# Define b5's coordinates
b5_xcor = b4_xcor + 0
b5_ycor = b4_ycor + width_of_square
b5_cors = b5_xcor, b5_ycor

# Define b6's coordinates
b6_xcor = b5_xcor + 0
b6_ycor = b5_ycor + width_of_square
b6_cors = b6_xcor, b6_ycor

# Define b7's coordinates
b7_xcor = b6_xcor + 0
b7_ycor = b6_ycor + width_of_square
b7_cors = b7_xcor, b7_ycor

# Define b8's coordinates
b8_xcor = b7_xcor + 0
b8_ycor = b7_ycor + width_of_square
b8_cors = b8_xcor, b8_ycor

# Define c1's coordinates
c1_xcor = b1_xcor + width_of_square
c1_ycor = b1_ycor + 0
c1_cors = c1_xcor, c1_ycor

# Define c2's coordinates
c2_xcor = c1_xcor + 0
c2_ycor = c1_ycor + width_of_square
c2_cors = c2_xcor, c2_ycor

# Define c3's coordinates
c3_xcor = c2_xcor + 0
c3_ycor = c2_ycor + width_of_square
c3_cors = c3_xcor, c3_ycor

# Define c4's coordinates
c4_xcor = c3_xcor + 0
c4_ycor = c3_ycor + width_of_square
c4_cors = c4_xcor, c4_ycor

# Define c5's coordinates
c5_xcor = c4_xcor + 0
c5_ycor = c4_ycor + width_of_square
c5_cors = c5_xcor, c5_ycor

# Define c6's coordinates
c6_xcor = c5_xcor + 0
c6_ycor = c5_ycor + width_of_square
c6_cors = c6_xcor, c6_ycor

# Define c7's coordinates
c7_xcor = c6_xcor + 0
c7_ycor = c6_ycor + width_of_square
c7_cors = c7_xcor, c7_ycor

# Define c8's coordinates
c8_xcor = c7_xcor + 0
c8_ycor = c7_ycor + width_of_square
c8_cors = c8_xcor, c8_ycor

# Define d1's coordinates
d1_xcor = c1_xcor + width_of_square
d1_ycor = c1_ycor + 0
d1_cors = d1_xcor, d1_ycor

# Define d2's coordinates
d2_xcor = d1_xcor + 0
d2_ycor = d1_ycor + width_of_square
d2_cors = d2_xcor, d2_ycor

# Define d3's coordinates
d3_xcor = d2_xcor + 0
d3_ycor = d2_ycor + width_of_square
d3_cors = d3_xcor, d3_ycor

# Define d4's coordinates
d4_xcor = d3_xcor + 0
d4_ycor = d3_ycor + width_of_square
d4_cors = d4_xcor, d4_ycor

# Define d5's coordinates
d5_xcor = d4_xcor + 0
d5_ycor = d4_ycor + width_of_square
d5_cors = d5_xcor, d5_ycor

# Define d6's coordinates
d6_xcor = d5_xcor + 0
d6_ycor = d5_ycor + width_of_square
d6_cors = d6_xcor, d6_ycor

# Define d7's coordinates
d7_xcor = d6_xcor + 0
d7_ycor = d6_ycor + width_of_square
d7_cors = d7_xcor, d7_ycor

# Define d8's coordinates
d8_xcor = d7_xcor + 0
d8_ycor = d7_ycor + width_of_square
d8_cors = d8_xcor, d8_ycor

# Define e1's coordinates
e1_xcor = d1_xcor + width_of_square
e1_ycor = d1_ycor + 0
e1_cors = e1_xcor, e1_ycor

# Define e2's coordinates
e2_xcor = e1_xcor + 0
e2_ycor = e1_ycor + width_of_square
e2_cors = e2_xcor, e2_ycor

# Define e3's coordinates
e3_xcor = e2_xcor + 0
e3_ycor = e2_ycor + width_of_square
e3_cors = e3_xcor, e3_ycor

# Define e4's coordinates
e4_xcor = e3_xcor + 0
e4_ycor = e3_ycor + width_of_square
e4_cors = e4_xcor, e4_ycor

# Define e5's coordinates
e5_xcor = e4_xcor + 0
e5_ycor = e4_ycor + width_of_square
e5_cors = e5_xcor, e5_ycor

# Define e6's coordinates
e6_xcor = e5_xcor + 0
e6_ycor = e5_ycor + width_of_square
e6_cors = e6_xcor, e6_ycor

# Define e7's coordinates
e7_xcor = e6_xcor + 0
e7_ycor = e6_ycor + width_of_square
e7_cors = e7_xcor, e7_ycor

# Define e8's coordinates
e8_xcor = e7_xcor + 0
e8_ycor = e7_ycor + width_of_square
e8_cors = e8_xcor, e8_ycor

# Define f1's coordinates
f1_xcor = e1_xcor + width_of_square
f1_ycor = e1_ycor + 0
f1_cors = f1_xcor, f1_ycor

# Define f2's coordinates
f2_xcor = f1_xcor + 0
f2_ycor = f1_ycor + width_of_square
f2_cors = f2_xcor, f2_ycor

# Define f3's coordinates
f3_xcor = f2_xcor + 0
f3_ycor = f2_ycor + width_of_square
f3_cors = f3_xcor, f3_ycor

# Define f4's coordinates
f4_xcor = f3_xcor + 0
f4_ycor = f3_ycor + width_of_square
f4_cors = f4_xcor, f4_ycor

# Define f5's coordinates
f5_xcor = f4_xcor + 0
f5_ycor = f4_ycor + width_of_square
f5_cors = f5_xcor, f5_ycor

# Define f6's coordinates
f6_xcor = f5_xcor + 0
f6_ycor = f5_ycor + width_of_square
f6_cors = f6_xcor, f6_ycor

# Define f7's coordinates
f7_xcor = f6_xcor + 0
f7_ycor = f6_ycor + width_of_square
f7_cors = f7_xcor, f7_ycor

# Define f8's coordinates
f8_xcor = f7_xcor + 0
f8_ycor = f7_ycor + width_of_square
f8_cors = f8_xcor, f8_ycor

# Define g1's coordinates
g1_xcor = f1_xcor + width_of_square
g1_ycor = f1_ycor + 0
g1_cors = g1_xcor, g1_ycor

# Define g2's coordinates
g2_xcor = g1_xcor + 0
g2_ycor = g1_ycor + width_of_square
g2_cors = g2_xcor, g2_ycor

# Define g3's coordinates
g3_xcor = g2_xcor + 0
g3_ycor = g2_ycor + width_of_square
g3_cors = g3_xcor, g3_ycor

# Define g4's coordinates
g4_xcor = g3_xcor + 0
g4_ycor = g3_ycor + width_of_square
g4_cors = g4_xcor, g4_ycor

# Define g5's coordinates
g5_xcor = g4_xcor + 0
g5_ycor = g4_ycor + width_of_square
g5_cors = g5_xcor, g5_ycor

# Define g6's coordinates
g6_xcor = g5_xcor + 0
g6_ycor = g5_ycor + width_of_square
g6_cors = g6_xcor, g6_ycor

# Define g7's coordinates
g7_xcor = g6_xcor + 0
g7_ycor = g6_ycor + width_of_square
g7_cors = g7_xcor, g7_ycor

# Define g8's coordinates
g8_xcor = g7_xcor + 0
g8_ycor = g7_ycor + width_of_square
g8_cors = g8_xcor, g8_ycor

# Define h1's coordinates
h1_xcor = g1_xcor + width_of_square
h1_ycor = g1_ycor + 0
h1_cors = h1_xcor, h1_ycor

# Define h2's coordinates
h2_xcor = h1_xcor + 0
h2_ycor = h1_ycor + width_of_square
h2_cors = h2_xcor, h2_ycor

# Define h3's coordinates
h3_xcor = h2_xcor + 0
h3_ycor = h2_ycor + width_of_square
h3_cors = h3_xcor, h3_ycor

# Define h4's coordinates
h4_xcor = h3_xcor + 0
h4_ycor = h3_ycor + width_of_square
h4_cors = h4_xcor, h4_ycor

# Define h5's coordinates
h5_xcor = h4_xcor + 0
h5_ycor = h4_ycor + width_of_square
h5_cors = h5_xcor, h5_ycor

# Define h6's coordinates
h6_xcor = h5_xcor + 0
h6_ycor = h5_ycor + width_of_square
h6_cors = h6_xcor, h6_ycor

# Define h7's coordinates
h7_xcor = h6_xcor + 0
h7_ycor = h6_ycor + width_of_square
h7_cors = h7_xcor, h7_ycor

# Define h8's coordinates
h8_xcor = h7_xcor + 0
h8_ycor = h7_ycor + width_of_square
h8_cors = h8_xcor, h8_ycor

#####-Setup-#####


#####-Game Handling-#####

