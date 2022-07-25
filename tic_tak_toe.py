# tic tak toe
import random

board = []

for i in range(3):
    # temporary variable
    row = []
    for j in range(3):
        row.append("-")
    board.append(row)

def show_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def is_board_filled():
    for row in board:
        for item in row:
            if item != "-":
                return False

        return True
# after every chance we will check is player win or not
def is_player_win(player) :
    # this function take input of any player and check is player win or not
    win = None

    # checking rows
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != player:
                win = False
                break
        if win :
            return win

    # checking columns
    for i in range(3):
        win= True
        for j in range(3):
            if board[j][i] != player:
                win= False
                break
        if win :
            return win

    # checking diagonals
    for i in range(3):
        win =True
        if board[i][i] != player:
            win = False
            break
    if win == True:
        return win
    # for diagonal position [0,2],[1,1],[2,0]
    win = True

    for i in range(3):
        if board[i][3-1-i] != player :
            win = False
            break
    if win == True:
        return win
    return False

    # if theres "-" in board

def start():
    #this function is use to start a game

    # two player X and O
    player = "X" if random.randint(0,1) == 1 else "O"
    while True :
        show_board()
        print(" %s Player Turn "%player)

        r, c = [int(x) for x in input("Enter position(row and column :  )").split()]
        board[r-1][c-1] = player

        if is_player_win(player) == True:
            print("player %s wins"%player)
            break

        if is_board_filled() == True:
            print("No one wins ")
            break
        player = "X" if player == "O" else "O"

start()