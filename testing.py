# https://trinket.io/python/051179b6d3
squares_per_side = 8

#Define an empty list that will contain the locations of the user's ships
# A 0 corresponds to no ship at that location
# A 1 corresponds to a ship at that location
# An X stands for a hit ship at that location
# The notation will not change for a miss
player_grid = []

for i in range(squares_per_side):
    player_grid.append(["O"] * squares_per_side)

def print_board(player_grid):
    for row in player_grid:
        print((" ").join(row))

column_a = 0
column_b = 1
column_c = 2
column_d = 3
column_e = 4
column_f = 5
column_g = 6
column_h = 7

row_1 = 7
row_2 = 6
row_3 = 5
row_4 = 4
row_5 = 3
row_6 = 2
row_7 = 1
row_8 = 0


# player_grid[y_axis][x_axis]
player_grid[row_4][column_b] = "x"

print_board(player_grid)