"""
The Game board is a two D array emulating the X*Y Tic Tac Toe Game
"""
global game_board
# Constants
place_already_filled = "Given place is already filled. Provide an empty place from the board"
invalid_move = "Invalid move. Enter a value within the board dimension."
invalid_value = "Invalid value. Enter an integer value within the board dimension."
game_over_tie = "Game Over. It is a tie."


def initialise_gameboard(dimensions):
    global game_board
    dimensions = int(dimensions)
    # Fill with empty strings
    game_board = [[' ' for _ in range(dimensions)] for _ in range(dimensions)]


def print_board():
    print("**************************")
    for item in game_board:
        print(item)
    print("**************************")


def check_game_status(x_pos, y_pos, player):
    row_match = True
    column_match = True
    left_diagonal_match = True
    right_diagonal_match = True

    for i in range(0, len(game_board)):
        if game_board[x_pos][i] != game_board[x_pos][y_pos]:
            row_match = False

    for i in range(0, len(game_board)):
        if game_board[i][y_pos] != game_board[x_pos][y_pos]:
            column_match = False

    for i in range(0, len(game_board)):
        if game_board[i][i] != game_board[x_pos][y_pos]:
            left_diagonal_match = False
        if game_board[i][len(game_board) - i - 1] != game_board[x_pos][y_pos]:
            right_diagonal_match = False

    print_board()

    if row_match or column_match or left_diagonal_match or right_diagonal_match:
        return f"Player {player} has won"
    else:
        return "Playing"


def game():
    dimensions = input("Enter board dimensions (3 for a 3x3 board): ")
    first_user = input("Enter first user name : ")
    second_user = input("Enter second user name: ")
    initialise_gameboard(dimensions)
    player = first_user
    count = 1

    while True:
        print(f"It's user : {player}'s turn")
        positions = input("Enter move position (x,y) : ").split(",")

        try:
            x_pos = int(positions[0]) - 1
            y_pos = int(positions[1]) - 1
        except ValueError:
            print(invalid_value)
            continue

        if x_pos < 0 or x_pos >= len(game_board) or y_pos < 0 or y_pos >= len(game_board):
            print(invalid_move)
            continue

        if game_board[x_pos][y_pos] != ' ':
            print(place_already_filled)
            continue

        if player is first_user:
            game_board[x_pos][y_pos] = 'X'
        else:
            game_board[x_pos][y_pos] = 'O'

        count = count + 1

        game_status = check_game_status(x_pos, y_pos, player)

        if game_status != "Playing":
            print(game_status)
            break

        if count == len(game_board) * len(game_board) + 1:
            print_board()
            print(game_over_tie)
            break

        # Switch players after
        if player is first_user:
            player = second_user
        else:
            player = first_user

    another_game = input("Do you want to play another game (Y/N) : ")

    if another_game.lower() == 'y' or another_game == 'Y':
        game()


game()