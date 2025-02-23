import time

class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.playerMove = 'X'  
        self.ai_symbol = 'O'
        self.human_symbol = 'X'

    def printBoard(self):
        print("\033c", end="")  
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)  

    def isValidMove(self, user):
        if not user.isdigit():
            print("Invalid input! Enter a number between 1 and 9.")
            return False
        
        user = int(user)
        if 1 <= user <= 9:
            row, col = divmod(user - 1, 3)
            if self.board[row][col] == " ":
                return True
        
        print("Invalid move! Choose an empty spot between 1 and 9.")
        return False

    def checkWin(self):
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

    def switchPlayer(self):
        self.playerMove = 'O' if self.playerMove == 'X' else 'X'

    def findBestMove(self):
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        best_score = float('-inf')
        best_move = None

        for (r, c) in empty_spots:
            self.board[r][c] = self.ai_symbol 
            score = self.minmax(0, False) 
            self.board[r][c] = ' ' 

            if score > best_score:
                best_score = score
                best_move = (r, c)

        return best_move

    def minmax(self, depth, is_maximizing):
        winner = self.checkWin()
        if winner == self.ai_symbol:
            return 10 - depth  
        elif winner == self.human_symbol:
            return depth - 10  
        elif not any(' ' in row for row in self.board):
            return 0  # Draw

        if is_maximizing:
            best_score = float('-inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == ' ':
                        self.board[r][c] = self.ai_symbol
                        score = self.minmax(depth + 1, False)
                        self.board[r][c] = ' '  
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == ' ':
                        self.board[r][c] = self.human_symbol
                        score = self.minmax(depth + 1, True)
                        self.board[r][c] = ' '  
                        best_score = min(score, best_score)
            return best_score

    def checkFull(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def startGame(self):
        print("The game is about to start. NOOB ")
        agentTurn = False  

        while True:
            self.printBoard()

            if self.checkFull():
                print("DRAW !! ")
                break

            if agentTurn:
                print("AI is thinking... ")
                time.sleep(1)
                row, col = self.findBestMove()
                self.board[row][col] = self.playerMove
            else:
                while True:
                    user = input("Your move (1-9) like a numpad: ")
                    if self.isValidMove(user):
                        row, col = divmod(int(user) - 1, 3)
                        self.board[row][col] = self.playerMove
                        break

            if self.checkWin():
                self.printBoard()
                print(f"Player {self.playerMove} wins!")
                break

            self.switchPlayer()
            agentTurn = not agentTurn 

if __name__ == '__main__':
    game = TicTacToe()
    game.startGame()
