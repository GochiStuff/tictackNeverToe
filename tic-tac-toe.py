import tkinter as tk

root = tk.Tk()
root.title("NEVER WIN TIC TAC TOE")
root.geometry("800x600")
frame = tk.Frame(root)
frame.pack(expand=True)
message_label = tk.Label(root, text="Your Turn!", font=("Arial", 16))
message_label.pack(pady=40)

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.ai = 'O'
        self.current_turn = 'player'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text=' ', font=("Arial", 24), width=5, height=2, command=lambda i=i, j=j: self.player_move(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn
    def update_button(self, i, j):
        self.buttons[i][j].config(text=self.board[i][j])
    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
    def check_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    def player_move(self, i, j):
        if self.current_turn != 'player' or self.board[i][j] != ' ':
            return
        self.board[i][j] = self.player
        self.update_button(i, j)
        winner = self.check_win()
        if winner:
            message_label.config(text=f"{winner} wins!")
            self.disable_buttons()
            return
        if self.check_full():
            message_label.config(text="Tie game!")
            self.disable_buttons()
            return
        self.current_turn = 'ai'
        message_label.config(text="AI is thinking...")
        root.after(500, self.ai_move)
    def ai_move(self):
        move = self.find_best_move()
        if move is None:
            message_label.config(text="Tie game!")
            self.disable_buttons()
            return
        i, j = move
        self.board[i][j] = self.ai
        self.update_button(i, j)
        winner = self.check_win()
        if winner:
            message_label.config(text=f"{winner} wins!")
            self.disable_buttons()
            return
        if self.check_full():
            message_label.config(text="Tie game!")
            self.disable_buttons()
            return
        self.current_turn = 'player'
        message_label.config(text="Your Turn!")
    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.ai
                    score = self.minimax(False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move
    def minimax(self, is_maximizing):
        winner = self.check_win()
        if winner == self.ai:
            return 1
        if winner == self.player:
            return -1
        if self.check_full():
            return 0
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.ai
                        score = self.minimax(False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.player
                        score = self.minimax(True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
game = TicTacToe()
root.mainloop()
