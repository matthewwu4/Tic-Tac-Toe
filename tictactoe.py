#board (Done)
#display board (Done)
#play game (Done)
#handle turn (Done)
#check win
    #check rows
    #check cols
    #check diags
#check tie
#flip player

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display():
    print("   1" + "   " + "2" + "   " + "3")
    print("1  " + board[0] + " | " + board[1] + " | " + board[2])
    print("2  " + board[3] + " | " + board[4] + " | " + board[5])
    print("3  " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def player1():
    print("Player 1")
    print("========")
    global player1_input
    player1_input = input("Enter your move (Row + Col): ")

def player2():
    print("Player 2")
    print("========")
    global player2_input
    player2_input = input("Enter your move (Row + Col): ")

def play_game1():
    global spot1
    spot1 = 99
    while spot1 == 99:
        row1 = int(player1_input[0])
        col1 = int(player1_input[1])
        if row1 == 1 and col1 == 1:
            spot1 = 0
        elif row1 == 1 and col1 == 2:
            spot1 = 1
        elif row1 == 1 and col1 == 3:
            spot1 = 2
        elif row1 == 2 and col1 == 1:
            spot1 = 3
        elif row1 == 2 and col1 == 2:
            spot1 = 4
        elif row1 == 2 and col1 == 3:
            spot1 = 5
        elif row1 == 3 and col1 == 1:
            spot1 = 6
        elif row1 == 3 and col1 == 2:
            spot1 = 7
        elif row1 == 3 and col1 == 3:
            spot1 = 8
        else:
            print()
            print("Invalid Move!")
            print()
            player1()

def play_game2():
    global spot2
    spot2 = 99
    while spot2 == 99:
        row2 = int(player2_input[0])
        col2 = int(player2_input[1])
        if row2 == 1 and col2 == 1:
            spot2 = 0
        elif row2 == 1 and col2 == 2:
            spot2 = 1
        elif row2 == 1 and col2 == 3:
            spot2 = 2
        elif row2 == 2 and col2 == 1:
            spot2 = 3
        elif row2 == 2 and col2 == 2:
            spot2 = 4
        elif row2 == 2 and col2 == 3:
            spot2 = 5
        elif row2 == 3 and col2 == 1:
            spot2 = 6
        elif row2 == 3 and col2 == 2:
            spot2 = 7
        elif row2 == 3 and col2 == 3:
            spot2 = 8
        else:
            print()
            print("Invalid Move!")
            print()
            player2()

def mark_game1():
    while True:
        if board[spot1] == "-":
            board[spot1] = "O"
            check_win()
            break
        else:
            print()
            print("Invalid Move!")
            print()
            player1()
            play_game1()

def mark_game2():
    while True:
        if board[spot2] == "-":
            board[spot2] = "X"
            check_win()
            break
        else:
            print()
            print("Invalid Move!")
            print()
            player2()
            play_game2()

def check_win():
    #Check 3 in a row
    open = 0
    if ((board[0] == "O" and board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[4] == "O" and board[5] == "O") or (board[6] == "O" and board[7] == "O" and board[8] == "O") or (board[0] == "O" and board[4] == "O" and board[8] == "O") or (board[2] == "O" and board[4] == "O" and board[6] == "O") or (board[0] == "O" and board[3] == "O" and board[6] == "O") or (board[1] == "O" and board[4] == "O" and board[7] == "O") or (board[2] == "O" and board[5] == "O" and board[8] == "O")):
        print()
        print("Player 1 wins!!!")
        print()
        play_again()
    elif ((board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X") or (board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X") or (board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X")):
        print()
        print("Player 2 wins!!!")
        print()
        play_again()
    else:
        for i in range(0,9):
            if board[i] == "-":
                open += 1
    if open == 0:
        print("It's a Tie!!!")
        play_again()

def play_again():
    print("Do you want to play again?")
    print("[1] Yes")
    print("[2] No")
    user_input = input("Choice : ")

global no_win
no_win = True
display()
while no_win:
    player1()
    play_game1()
    mark_game1()
    display()
    player2()
    play_game2()
    mark_game2()
    display()
