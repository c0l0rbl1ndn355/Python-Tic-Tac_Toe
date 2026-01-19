#Tic Tac Toe game vs a CPU
import random
import math

player = ""
cpu = ""
difficulty = ""

#Allows player and cpu turns to be assigned to the grid
global grid_num
grid_num = [0] + [" "] * 9
    
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

#defines Hard difficulty CPU using minimax
def minimax(is_maximizing):
    if check_winner(grid_num, cpu):
        return 1
    if check_winner(grid_num, player):
        return -1
    if is_draw(grid_num):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(1, 10):
            if grid_num[i] not in ("X", "O"):
                grid_num[i] = cpu
                score = minimax(False)
                grid_num[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if grid_num[i] not in ("X", "O"):
                grid_num[i] = player
                score = minimax(True)
                grid_num[i] = " "
                best_score = min(score, best_score)
        return best_score

    #CPU turn
def cpu_turn(difficulty):
    mistake_chance = 0.25  # 25% chance to make a mistake

    #just plays random moves
    if difficulty == "Easy":
        while True:
            cpu_num = random.randint(1, 9)
            #Checks if move is valid
            if grid_num[cpu_num] != "X" and grid_num[cpu_num] != "O":
                grid_num[cpu_num] = cpu
                break

    #win > block > random
    elif difficulty == "Medium":

        #Mistake: random move
        if random.random() < mistake_chance:
            while True:
                cpu_num = random.randint(1, 9)
                if grid_num[cpu_num] != "X" and grid_num[cpu_num] != "O":
                    grid_num[cpu_num] = cpu
                    return

        #1: Try to WIN
        for i in range(1, 10):
            if grid_num[i] != "X" and grid_num[i] != "O":
                grid_num[i] = cpu
                if check_winner(grid_num, cpu):
                    return
                grid_num[i] = " "

        #2: Try to BLOCK player
        for i in range(1, 10):
            if grid_num[i] != "X" and grid_num[i] != "O":
                grid_num[i] = player
                if check_winner(grid_num, player):
                    grid_num[i] = cpu
                    return
                grid_num[i] = " "

        #3: Otherwise RANDOM
        while True:
            cpu_num = random.randint(1, 9)
            if grid_num[cpu_num] != "X" and grid_num[cpu_num] != "O":
                grid_num[cpu_num] = cpu
                return
   
   #minimax
    elif difficulty == "Hard":
        best_score = -math.inf
        move = 0
        for i in range(1, 10):
            if grid_num[i] == " ":
                grid_num[i] = cpu
                score = minimax(False)
                grid_num[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        grid_num[move] = cpu
        

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
    
#This runs the game:
def run_game(difficulty, player):
    for num in range(1, 10):
        #checks if player input is a valid spot
        while True:
            move = input("Where do you want to place your symbol at? ")
            
            if move == "exit":
                quit()
                
            player_grid = int(move)

            if grid_num[player_grid] in ("X", "O"):
                print("That spot is taken!")
            else:
                grid_num[player_grid] = player
                break
        
        #Checks if the game is finished, if it is, prints the result
        if check_winner(grid_num, player):
            print(make_grid(grid_num)) 
            print("You win!")
            replay = input(f"Do you want to start a new game? (Y/n): \n")
            check_replay(replay)
        elif check_winner(grid_num, cpu):
            print(make_grid(grid_num)) 
            print("CPU wins!")
            replay = input(f"Do you want to start a new game? (Y/n): \n")
            check_replay(replay)
        elif is_draw(grid_num):
            print(make_grid(grid_num)) 
            print("Draw!")
            replay = input(f"Do you want to start a new game? (Y/n): \n")
            check_replay(replay)
        
        cpu_turn(difficulty)
        print(make_grid(grid_num)) 

#checks if the player wants to start a new game
def check_replay(replay):
    while True:
        if replay == "y" or replay == "Y":
            grid_num = [0] + [" "] * 9
            start()
        else:
            quit()

#player input starts
def start():
    global player, cpu, difficulty
    player = input("Choose either 'X' or 'O' ")
    #Updates the Player letter to be Capital
    if player == "x":
        player = "X"
    elif player == "o":
        player = "O"
    cpu = ""

    #sets the cpu letter to the opposite of the player's letter
    if player == "X":
        cpu = "O"
    elif player == "O":
        cpu = "X"

    print("This is how the Tic Tac Toe grid is setup:")
    print(make_grid(grid_num))
    print(f"The grid is numbered from left to right, \n as the top left is 1 to the bottom right is 9")
    advance = input("Enter Y to continue: ")

    #Inputs the CPU difficulty
    if advance == "Y" or advance == "y":
        while True:
            cpu_difficulty = input("""
                Enter the CPU difficulty:
                    1 for Easy
                    2 for Medium
                    3 for Hard
                """
            )   

            if cpu_difficulty == "1":
                difficulty = "Easy"
                break
            elif cpu_difficulty == "2":
                difficulty = "Medium"
                break
            elif cpu_difficulty == "3":
                difficulty = "Hard"
                print("good luck. you'll need it to win")
                break
            else: 
                print("Invalid difficulty")
        
        run_game(difficulty, player)

start()