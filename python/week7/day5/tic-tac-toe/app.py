from re import X


print("welcome to tic tac toe")
turn = 1
winner = None 

board = [[" "," "," "],
[" "," "," "],
[" "," "," "]]


def check_win():
    for i in range(2):
        if (board[i][0] == "X" or board[i][0] == "O") and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            winner = turn
            print(f"🎉🎉🎉 player {winner} wins 🎉🎉🎉")

    for i in range(2):
        if (board[0][i] == "X" or board[0][i] == "O") and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            winner = turn
            print(f"🎉🎉🎉 player {winner} wins 🎉🎉🎉")

    if (board[0][0] == "X" or board[0][0] == "O") and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = turn
        print(f"🎉🎉🎉 player {winner} wins 🎉🎉🎉")

    if (board[0][2] == "X" or board[0][2] == "O") and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        winner = turn
        print(f"🎉🎉🎉 player {winner} wins 🎉🎉🎉")

while winner == None:
    print(f""" 
         0      1      2
      **********************
    0 *  {board[0][0]}   |  {board[0][1]}   |  {board[0][2]}   |
      *------|------|------|
    1 *  {board[1][0]}   |  {board[1][1]}   |  {board[1][2]}   |
      *------|------|------|
    2 *  {board[2][0]}   |  {board[2][1]}   |  {board[2][2]}   |
      **********************
    player {turn}'s turn:""")

    
    row = input("choose a row: ")
    while int(row) < 0 or int(row) > 2:
        row = input("choose a row: ")
    column = input("choose a column: ")
    while int(column) < 0 or int(column) > 2:
        column = input("choose a column: ")
    
    while board[int(row)][int(column)] != " ":
        print("taken already")

        row = input("choose a row: ")
        while int(row) < 0 or int(row) > 2:
            row = input("choose a row: ")
        column = input("choose a column: ")
        while int(column) < 0 or int(column) > 2:
            column = input("choose a column: ")
    
    if turn == 1:
        board[int(row)][int(column)] = "X"
    else:
        board[int(row)][int(column)] = "O"

    check_win()

    if turn == 1:
        turn = 2
    else:
        turn = 1

