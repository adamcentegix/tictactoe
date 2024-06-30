# Tic Tac Toe game v5 in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
                print(f"
        row=int(input(f"Enter row (0-2) for your {current_player}: "))
                col=int(
                    input(f"Enter column (0-2) for your {current_player}: "))

        if board[row][col] == ' ':
            board[row][col]=current_player
            winner=check_winner(board)
            if winner:
                                print(f"
Congratulations! Player {winner} wins!")
                print(f"Player {winner} wins!")
                break
                            print("
It's a tie! The game ends in a draw.")
                print_board(board)
                print("It's a tie!")
                            print("
Oops! That cell is already occupied. Please try again.")
            current_player='O' if current_player == 'X' else 'X'
            print("Welcome to Tic Tac Toe!")
                print("Player X goes first.
    play_game()
    print("
Thanks for playing Tic Tac Toe!")
if __name__ == "__main__":
    play_game()
