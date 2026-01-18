#Tic Tac Toe game vs a CPU
import random
#Allows player and cpu turns to be assigned to the grid
grid_num = [0,
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]
    
#All possible win combonations
WIN_COMBOS = [
    (1, 2, 3),  # rows
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),  # columns
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),  # diagonals
    (3, 5, 7)
]

#Grid of the game being printed on screen
def make_grid(grid_num):
    return f"""
{grid_num[1]} | {grid_num[2]} | {grid_num[3]}
--|---|--
{grid_num[4]} | {grid_num[5]} | {grid_num[6]}
--|---|--
{grid_num[7]} | {grid_num[8]} | {grid_num[9]}
"""

#CPU turn
def cpu_turn():
    while True:
        cpu_num = random.randint(1, 9)
        #Checks if move is valid
        if grid_num[cpu_num] != "X" and grid_num[cpu_num] != "O":
            grid_num[cpu_num] = cpu
            break

#Checks to see if the game is won  
def check_winner(grid, symbol):
    for a, b, c in WIN_COMBOS:
        if grid[a] == grid[b] == grid[c] == symbol:
            return True
    return False

#Checks to see if the game is a draw
def is_draw(grid):
    for i in range(1, 10):
        if grid[i] != "X" and grid[i] != "O":
            return False
    return True
player = input("Choose either 'X' or 'O' ")
#Updates the Player letter to be Capital
if player == "x":
    player = "X"
elif player == "o":
    player = "O"
cpu = ""

#sets the cpu letter to the opposite of the player's letter
if player == "X" or player == "x":
    cpu = "O"
elif player == "O" or player == "o":
    cpu = "X"

print("This is how the Tic Tac Toe grid is setup")
print(make_grid(grid_num))
advance = input("Enter Y to continue ")

#This runs the game:
for num in range(1, 10):
    #player input
    player_grid = int(input("Where do you want to place your symbol at? "))
    #checks if player input is a valid spot
    if grid_num[player_grid] != "X" and grid_num[player_grid] != "O":
        grid_num[player_grid] = player
    else:
        print("That spot is taken!")
    
    #updates the grid
    grid_num[int(player_grid)] = player
    
    cpu_num = int(random.randint(1, 9))
    cpu_turn()
    
    if check_winner(grid_num, player):
        print("You win!")
        break
    elif check_winner(grid_num, cpu):
        print("CPU wins!")
        break
    elif is_draw(grid_num):
        print("Draw!")
        break
            
            
    print(make_grid(grid_num))
    
