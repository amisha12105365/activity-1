import random
from colorama import Fore, init

init(autoreset=True)

def show_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---+---+---")
    print(board[3], "|", board[4], "|", board[5])
    print("---+---+---")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(board, symbol):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == symbol:
            return True

    return False

def game():
    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!")

    name = input("Enter your name: ")

    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        player = input("Choose X or O: ").upper()

        if player not in ["X", "O"]:
            print("Please choose X or O.")
            continue

        ai = "O" if player == "X" else "X"

        while True:
            show_board(board)

            # Player move
            move = int(input("Choose a position (1-9): "))

            if move < 1 or move > 9 or not board[move - 1].isdigit():
                print("Invalid move!")
                continue

            board[move - 1] = player

            if check_win(board, player):
                show_board(board)
                print("Congratulations", name, "you won!")
                break

            if all(not x.isdigit() for x in board):
                show_board(board)
                print("It's a tie!")
                break

            # AI move
            empty = [i for i in range(9) if board[i].isdigit()]
            move = random.choice(empty)
            board[move] = ai

            print("AI chose position", move + 1)

            if check_win(board, ai):
                show_board(board)
                print("AI won!")
                break

        again = input("Play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break

game()