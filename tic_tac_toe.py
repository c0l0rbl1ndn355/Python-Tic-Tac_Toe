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

def cpu_turn(cpu_num):
    for cpu_num in grid_num:
        if grid_num != "X" and grid_num != "O":
            grid_num[int(cpu_num)] = cpu

player = input("Choose either 'X' or 'O' ")
cpu = ""

if player == "X" or player == "x":
    cpu = "O"
elif player == "O" or player == "o":
    cpu = "X"

print("This is how the Tic Tac Toe grid is setup")
print(make_grid(grid_num))
advance = input("Enter Y to continue ")

for num in range(1, 10):
    player_grid = input("Where do you want to place your symbol at? ")
    grid_num[int(player_grid)] = player
    
    cpu_num = int(random.randint(1, 9))
    cpu_turn(cpu_num)
        
            
            
    print(make_grid(grid_num))
    
