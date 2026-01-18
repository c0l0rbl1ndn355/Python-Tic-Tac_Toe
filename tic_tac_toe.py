#Tic Tac Toe game vs a CPU
import random
#Allows X and O to be assigned to the grid
grid_num = [0,
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]
    
def make_grid(grid_num):
    return f"""
{grid_num[1]} | {grid_num[2]} | {grid_num[3]}
--|---|--
{grid_num[4]} | {grid_num[5]} | {grid_num[6]}
--|---|--
{grid_num[7]} | {grid_num[8]} | {grid_num[9]}
"""

def cpu_turn():
    while True:
        cpu_num = random.randint(1, 9)
        if grid_num[cpu_num] != "X" and grid_num[cpu_num] != "O":
            grid_num[cpu_num] = cpu
            break

player = input("Choose either 'X' or 'O' ")
cpu = ""

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
    
            
            
    print(make_grid(grid_num))
    
