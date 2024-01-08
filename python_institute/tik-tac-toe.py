from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(len(board)):
        print("+", "+", "+", "+", sep="-" * 7, end="\n")
        for j in range(len(board[0])):
            print("|", " " * 7, sep="" * 7, end="")
        print("|")
        for j in range(len(board[0])):
            print("|", " " * 3, board[i][j], " " * 3, sep="" * 7, end="")
        print("|")
        for j in range(len(board[0])):
            print("|", " " * 7, sep="" * 7, end="")
        print("|")
    print("+", "+", "+", "+", sep="-" * 7, end="\n")

    # print("|", " " * 7, "|", "-" * 7, "|", "-" * 7, "|")
    # print("|", " " * 3, board[0], " " * 3, "|", "-", " " * 3, board[1], " " * 3, "|", " " * 3, board[2], " " * 3, "|")
    # print("|", " " * 7, "|", "-" * 7, "|", "-" * 7, "|")
    # print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    print(free_fields)
    while True:
        try:
            move = int(input("Enter a move: "))
            row = free_fields[move][0]
            col = free_fields[move][1]
            print("Move:", free_fields[move], "[", row, "]", "[", col, "]")
            board[row][col] = "O"
            print(board)
            display_board(board)
            break
        except Exception as e:
            print(e, "Invalid value please try again. Available moves:", free_fields.keys())


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = {}
    count = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields[count] = i, j
            count += 1

    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    victory = False
    for i in range(len(board)):
        if board[i].count(sign) == 3:
            print("board[i].count(sign)",board[i].count(sign))
            victory = True
            break
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            print("board[0][i] == board[1][i] and board[1][i] == board[2][i]", board[0][i] == board[1][i] and board[1][i] == board[2][i])
            victory = True
            break

            victory = True
            break
        else:
            continue
    if board[0][0] == board[1][1] == board[2][2]:
        victory = True
    elif board[0][2] == board[1][1] == board[2][0]:
        victory = True

    return victory


def draw_move(board):
    print("Computer move")
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    print(len(free_fields), " moves available -", free_fields)
    keys = list(free_fields.keys())
    move = randrange(0, len(keys))
    print("Random Generated=", move)
    print("Keys:", keys)
    if len(free_fields) == len(board) * len(board):
        move = 4
    row = free_fields[keys[move]][0]
    col = free_fields[keys[move]][1]
    print("Move:", keys[move], "[", row, "]", "[", col, "]")
    board[row][col] = "X"
    print(board)
    free_fields = make_list_of_free_fields(board)
    print(len(free_fields), " moves available -", free_fields)
    display_board(board)


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(len(board) * len(board[0]))
# display_board(board)
# print(make_list_of_free_fields(board))


# for i in range(9):
#     move = i+1
#     coords = make_list_of_free_fields(board)
#     row = coords[move][0]
#     col = coords[move][1]
#     print("Move:",i, " = [", row, "]", "[", col, "]")

tot =len(board) * len(board)
count = 1
while count < tot:
    print("Round: ", count)

    draw_move(board)
    if victory_for(board,'X'):
        print('Computer wins')
        break
    enter_move(board)
    if victory_for(board,'X'):
        print('You win')
        break
    count += 1
