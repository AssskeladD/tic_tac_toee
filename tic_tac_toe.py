import tkinter as tk
from tkinter import messagebox
import time

class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Крестики-Нолики")
        self.configure(bg="black")
        self.player1_name = ""
        self.player2_name = ""
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # виджеты для ввода имен
        self.label_player1 = tk.Label(self, text="Игрок 1:", bg="black", fg="white", font=("Helvetica", 18))
        self.entry_player1 = tk.Entry(self, font=("Helvetica", 18))
        self.label_player2 = tk.Label(self, text="Игрок 2:", bg="black", fg="white", font=("Helvetica", 18))
        self.entry_player2 = tk.Entry(self, font=("Helvetica", 18))
        self.button_start_game = tk.Button(self, text="Начать Игру", command=self.start_game, bg="white", fg="black", font=("Helvetica", 18))

        # виджеты в окне
        self.label_player1.grid(row=0, column=0, padx=10, pady=10)
        self.entry_player1.grid(row=0, column=1, padx=10, pady=10)
        self.label_player2.grid(row=1, column=0, padx=10, pady=10)
        self.entry_player2.grid(row=1, column=1, padx=10, pady=10)
        self.button_start_game.grid(row=2, columnspan=2, padx=10, pady=20)

    def start_game(self):
        # Записываем имена игроков
        self.player1_name = self.entry_player1.get()
        self.player2_name = self.entry_player2.get()

        # кнопки для игры
        self.create_buttons()

        # виджеты для ввода имен
        self.label_player1.grid_forget()
        self.entry_player1.grid_forget()
        self.label_player2.grid_forget()
        self.entry_player2.grid_forget()
        self.button_start_game.grid_forget()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self, text=" ", font=("Arial", 24, "bold"), width=8, height=4,
                    command=lambda row=i, col=j: self.on_button_click(row, col),
                    bg="black", fg="white", bd=3  # Черный фон, белый текст, обводка кнопки
                )
                self.buttons[i][j].grid(row=i + 3, column=j, padx=8, pady=8)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED, fg="black", font=("Arial", 30, "bold"))  # Черный текст

            if self.check_winner():
                winner_name = self.player1_name if self.current_player == "X" else self.player2_name
                messagebox.showinfo("Game Over", f"{winner_name} выиграл!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " " or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)  # Восстанавливаем текст и активируем кнопки

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
    time.sleep(5)
    game.run()
