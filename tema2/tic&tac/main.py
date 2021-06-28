import random

board = [["-" for i in range(4)] for j in range(4)]


def valid(nr):
    try:
        nr_int = int(nr)
        return nr
    except ValueError:
        return 0


def show(current_board):
    print(' ', current_board[1][1], '|', current_board[1][2], '|', current_board[1][3])
    print('----+---+---')
    print(' ', current_board[2][1], '|', current_board[2][2], '|', current_board[2][3])
    print('----+---+---')
    print(' ', current_board[3][1], '|', current_board[3][2], '|', current_board[3][3])
    print('----+---+---')


choices = ["x", "o"]


def check_end(current_board, symbol):
    if current_board[1][1] == current_board[1][2] == current_board[1][3] == symbol:
        return 1
    if current_board[2][1] == current_board[2][2] == current_board[2][3] == symbol:
        return 1
    if current_board[3][1] == current_board[3][2] == current_board[3][3] == symbol:
        return 1
    if current_board[1][1] == current_board[2][1] == current_board[3][1] == symbol:
        return 1
    if current_board[1][2] == current_board[2][2] == current_board[3][2] == symbol:
        return 1
    if current_board[1][3] == current_board[2][3] == current_board[3][3] == symbol:
        return 1
    if current_board[1][1] == current_board[2][2] == current_board[3][3] == symbol:
        return 1
    if current_board[3][1] == current_board[2][2] == current_board[1][3] == symbol:
        return 1
    return 0


def place(current_board, choice):
    row = input("Choose empty row position:")
    while valid(row) == 0 or int(row) > 3 or int(row) < 1:
        print("Wrong move, try again")
        row = input("Choose empty row position:")
    column = input("Choose empty column position:")
    while valid(column) == 0 or int(column) > 3 or int(column) < 1:
        print("Wrong move, try again")
        column = input("Choose empty column position:")
    current_board[int(row)][int(column)] = choice


def game():
    player = random.choice(choices)
    count = 0
    while 1:
        show(board)
        place(board, player)
        count += 1
        if count >= 5:
            if check_end(board, player) == 1:
                print("Player", player, "won!")
                break
        elif count == 9:
            print("Tie")
            break
        if player == "x":
            player = "o"
        else:
            player = "x"

    decision = input("Do you want to play again?")
    if decision == "yes":
        for i in range(4):
            for j in range(4):
                board[i][j] = "-"
        game()


game()
