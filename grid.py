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

#####-Functions-#####
# Define a function that will give the painters the proper attributes
def set_painter_attributes():
    #For loop that will give all painters the same attributes
    for i in range(len(master_painters_list)):
        master_painters_list[i].penup()
        # master_painters_list[i].hideturtle()
        master_painters_list[i].shape("classic")
        master_painters_list[i].pencolor("black")
        master_painters_list[i].fillcolor("black")
        master_painters_list[i].speed(5)
        master_painters_list[i].shapesize(1)
        master_painters_list[i].setheading(0)


# Define a function that will be used to draw the battleship grid
def draw_grid():
    # Set the attributes of the painters before drawing
    set_painter_attributes()

    