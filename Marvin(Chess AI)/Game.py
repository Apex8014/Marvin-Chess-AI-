from Board import Board
from Player import Player
import Global

gameBoard = Board()
WhitePlayer = Player("White")
BlackPlayer = Player("Black")
gameOver = False

while not gameOver:
    print("White to move:")
    print("Black")
    gameBoard.printBoard()
    print("White")
    gameBoard.updatePosition(WhitePlayer.playerMove(gameBoard.ChessBoard,gameBoard))
    #if the king is in check and doesn't have any valid moves, checkmate (Does not currently account for moving a piece to prevent check/checkmate)
    if not Global.canEscapeCheckmate("Black",gameBoard.ChessBoard,gameBoard):
        print("White Wins!")
        break
    print("Black to move:")
    print("Black")
    gameBoard.printBoard()
    print("White")
    gameBoard.updatePosition(BlackPlayer.playerMove(gameBoard.ChessBoard,gameBoard))
    #if it finds the white king, it changes the winner value to "!", if winner is not "!", then the king is gone and therefore black wins
    if not Global.canEscapeCheckmate("White",gameBoard.ChessBoard,gameBoard):
        print("Black Wins!")
        gameOver = True
        break