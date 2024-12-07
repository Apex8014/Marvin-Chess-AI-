from Board import Board
from Player import Player
from AI import AI
from Human import Human
import Global

class Game():
    def __init__(self,playerOne,playerTwo):
        self.gameBoard = Board()
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.killedTheKing = True
        if playerOne == "a":
            self.WhitePlayer = AI("White")
        else:
            self.WhitePlayer = Human("White")
        if playerTwo == "a":
            self.BlackPlayer = AI("Black")
        else:
            self.BlackPlayer = Human("Black")
        self.gameOver = False

    def startGame(self):
        while not self.gameOver:
            print("White to move:")
            print("Black")
            self.gameBoard.printBoard()
            print("White")
            self.gameBoard.updatePosition(self.WhitePlayer.getMove(self.gameBoard.ChessBoard,self.gameBoard),self.playerOne)
            #if the king is in check and doesn't have any valid moves, checkmate (Does not currently account for moving a piece to prevent check/checkmate)
            if Global.inStalemate(self.gameBoard.ChessBoard, "Black",self.gameBoard,self.playerOne):
                print("Tie Game")
                self.gameBoard.printBoard()
                break
            if not Global.canEscapeCheckmate("Black",self.gameBoard.ChessBoard,self.gameBoard,self.playerOne):
                print("White Wins!")
                self.gameBoard.printBoard()
                break
            print("Black to move:")
            print("Black")
            self.gameBoard.printBoard()
            print("White")
            self.gameBoard.updatePosition(self.BlackPlayer.getMove(self.gameBoard.ChessBoard,self.gameBoard),self.playerTwo)
            #if it finds the white king, it changes the winner value to "!", if winner is not "!", then the king is gone and therefore black wins
            if Global.inStalemate(self.gameBoard.ChessBoard, "White",self.gameBoard,self.playerTwo):
                print("Tie Game")
                self.gameBoard.printBoard()
                break
            if not Global.canEscapeCheckmate("White",self.gameBoard.ChessBoard,self.gameBoard,self.playerTwo):
                print("Black Wins!")
                self.gameBoard.printBoard()
                break