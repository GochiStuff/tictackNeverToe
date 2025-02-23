# Lets make a super awesome yet simple tic tac toe . 

class TicTacToe:



    def __init__(self):
        self.board = [['X']*3 for _ in range(3)]
        self.playerMove = 'X'

    def printBoard(self):
        print("\033c", end="")
        for row in self.board:
            print("|".join(row))
            print("-" * 5)  

    def startGame(self):            
        self.printBoard()   
        # while True:

            





if __name__ == '__main__':
    game = TicTacToe()
    print("The game is about to start and you have the first move , you can try you best but you can not win ! from me ")
    game.startGame()