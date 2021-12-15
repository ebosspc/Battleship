#####-Imports-#####
# Import turtle library for drawing and display functions
import turtle as trtl

#####-Setup-#####
# Define lists to store all painters, letters, and numbers used in creating the grid
master_painters_list = []
grid_letters_list = ["A","B","C","D","E","F","G","H"]
grid_numbers_list = ["1","2","3","4","5","6","7","8"]

# Create turtle objects that will be used to draw the battleship grid and label it and add them to the master list
grid_painter = trtl.Turtle()
label_painter = trtl.Turtle()
master_painters_list.append(grid_painter)
master_painters_list.append(label_painter)

# Define variables that will determine the size and shape of the battleship grid
number_of_sides = 4
number_of_squares = 64
squares_per_side = 8
number_of_squares_on_side = number_of_squares / squares_per_side
width_of_side = 520
width_of_square = width_of_side / squares_per_side
grid_painter_starting_location = -260, -260
label_painter_starting_location = -228,-295

#####-Functions-#####
# Define a function that will give the painters the proper attributes
def set_painter_attributes():
    #For loop that will give all painters the same attributes
    for i in range(len(master_painters_list)):
        master_painters_list[i].penup()
        master_painters_list[i].hideturtle()
        master_painters_list[i].shape("classic")
        master_painters_list[i].pencolor("black")
        master_painters_list[i].pensize(2)
        master_painters_list[i].fillcolor("black")
        master_painters_list[i].speed(0)
        master_painters_list[i].shapesize(1)
        master_painters_list[i].setheading(0)
    
    # Set individual starting locations
    grid_painter.goto(grid_painter_starting_location)
    label_painter.goto(label_painter_starting_location)

# Define a function to draw the borders of the grid
def draw_borders():
    # For loop to draw the border
    for i in range(3):
        grid_painter.pendown()
        grid_painter.forward(width_of_side)
        grid_painter.left(90)


# Define a function to draw the vertical lines
def draw_vert_lines():
    # For loop to draw the vertical lines
    for i in range(4):
        grid_painter.forward(width_of_side)
        grid_painter.left(90)
        grid_painter.forward(width_of_square)
        grid_painter.left(90)
        grid_painter.forward(width_of_side)
        grid_painter.right(90)
        grid_painter.forward(width_of_square)
        grid_painter.right(90)
        

# Define a function to draw the horizontal lines
def draw_horiz_lines():
    # For loop to draw the horizontal lines
    for i in range(4):
        grid_painter.forward(width_of_square)
        grid_painter.right(90)
        grid_painter.forward(width_of_side)
        grid_painter.left(90)
        grid_painter.forward(width_of_square)
        grid_painter.left(90)
        grid_painter.forward(width_of_side)
        grid_painter.right(90)

def draw_labels():
    #Display label drawering turtle
    label_painter.showturtle()

    #For loop to draw all of the letters and numbers on the board
    for i in range(number_of_sides):
        # Draw the letters on the bottom
        if i < 1:
            #For loop to label the bottom row of the chessboard with letters
            for a in range(int(number_of_squares_on_side)): 
                #Write the appropirate letter from the list of letters with the index of a and move to the next square
                label_painter.write(grid_letters_list[a], align = "center", font = ("Times New Roman", 20, "normal"))
                label_painter.forward(width_of_square)

        # Draw the numbers on the right
        elif i < 2:    
            #Move and turn the labeler turtle to the appropriate position
            label_painter.setheading(180)
            label_painter.forward(10)
            label_painter.setheading(90)
            label_painter.forward(50)

            #For loop to lable the right side of the chessboard with numbers
            for b in range(int(number_of_squares_on_side)):
                #Write the appropirate number from the list of numbers with the index of b and move to the next square
                label_painter.write(grid_numbers_list[b], align = "center", font = ("Times New Roman", 20, "normal"))
                label_painter.forward(width_of_square)

        # Draw the letters on the top
        elif i < 3:
            #Move and turn the labeler turtle to the appropriate position
            label_painter.goto(-228, 260)
            label_painter.setheading(0)

            #For loop to label the bottom row of the chessboard with letters
            for c in range(int(number_of_squares_on_side)):
                #Write the appropirate letter from the list of letters with the index of c and move forward
                label_painter.write(grid_letters_list[c], align = "center", font = ("Times New Roman", 20, "normal"))
                label_painter.forward(width_of_square)
        
        # Draw the numbers on the left
        elif i < 4:
            #Move and turn the labeler turtle to the appropriate position
            label_painter.goto(-275, -245)
            label_painter.setheading(90)

            #For loop to label the bottom row of the chessboard with letters
            for d in range(int(number_of_squares_on_side)):
                #Write the appropirate letter from the list of letters with the index of d and move forward
                label_painter.write(grid_numbers_list[d], align = "center", font = ("Times New Roman", 20, "normal"))
                label_painter.forward(width_of_square)

    #Ensure the pen is down because the trails will make the board and hide the turtle when its finished
    label_painter.pendown()
    label_painter.hideturtle()


# Define a function that will be used to draw the battleship grid
def draw_grid():
    # Set the attributes of the painters before drawing
    set_painter_attributes()

    # Draw the borders of the grid
    draw_borders()

    # Draw the lines of the grid
    draw_vert_lines()
    draw_horiz_lines()

    # Draw the labels of the grid
    draw_labels()

    