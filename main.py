# Tic Tac Toe game v5 in Python

def print_title():
    print("""
    _____ _     _____         _____
   \|_   _(_)   \|_   _\|_ _  __\|_   _\|__   ___
     \| \| \| \|     \| \|/ _` \|/ __\|\| \|/ _ \ / _      \| \| \| \|     \| \| (_\| \| (__ \| \| (_) \|  __/
     \|_\| \|_\|     \|_\|\__,_\|\___\|\|_\|\___/ \___\|
    """)


def print_board(board):
    print("""
       0   1   2
     ┌───┬───┬───┐
   0 │ {} │ {} │ {} │
     ├───┼───┼───┤
   1 │ {} │ {} │ {} │
     ├───┼───┼───┤
   2 │ {} │ {} │ {} │
     └───┴───┴───┘
    """.format(*[cell for row in board for cell in row]))


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

    print_title()
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                print("""
                 ___________
                '._==_==_=_.'
                .-\:      /-.
               \| (\|:.     \|) \|
                '-\|:.     \|-'
                  \::.    /
                   '::. .'
                     ) (
                   _.' '._
                  `"""""""`
                """)
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already occupied. Try again.")


if __name__ == "__main__":
    play_game()
