# Tic Tac Toe game v6 in Python

def print_board(board):
    print("
          0   1   2")
    print(" ┌───┬───┬───┐")
    for i, row in enumerate(board):
        print(f"{i}│ {' │ '.join(row)} │")
        if i < 2:
            print(" ├───┼───┼───┤")
    print(" └───┴───┴───┘")


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

    print("
          🎮 Welcome to Tic Tac Toe! 🎮")
    print("Player X goes first.
          ")

    while True:
        print_board(board)
        print(f"
              🔹 Player {current_player}'s turn 🔹")

        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    break
                else:
                    print("❌ Invalid move. Try again.")
            except ValueError:
                print("❌ Please enter numbers between 0 and 2.")

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"
                  🎉 Congratulations! Player {winner} wins! 🏆")
            break
        elif is_full(board):
            print_board(board)
            print("
                  😮 It's a tie! Well played, both! 🤝")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    print("
          Thank you for playing Tic Tac Toe! 👋")


if __name__ == "__main__":
    play_game()
