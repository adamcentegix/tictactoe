import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text=' ', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo(
                    'Game Over', f'Player {self.current_player} wins!')
                self.master.quit()
            elif self.is_full():
                messagebox.showinfo('Game Over', 'It\'s a tie!')
                self.master.quit()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
