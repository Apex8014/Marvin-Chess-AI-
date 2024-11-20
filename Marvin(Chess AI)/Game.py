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
    for i in Global.whitePieces:
        if Global.kings[1].getPos(gameBoard.ChessBoard) in i.attackedSquares and len(i.attackedSquares) > 0:
            if len(Global.kings[1].validMoves(gameBoard.ChessBoard)) == 0:
                if not Global.canEscapeCheckmate("White",gameBoard.ChessBoard):
                    print("White Wins!")
                    gameOver = True
                    break
    if gameOver:
        break
    print("Black to move:")
    print("Black")
    gameBoard.printBoard()
    print("White")
    gameBoard.updatePosition(BlackPlayer.playerMove(gameBoard.ChessBoard,gameBoard))
    #if it finds the white king, it changes the winner value to "!", if winner is not "!", then the king is gone and therefore black wins
    for i in Global.blackPieces:
        if Global.kings[0].getPos(gameBoard.ChessBoard) in i.attackedSquares:
            if len(Global.kings[0].validMoves(gameBoard.ChessBoard)) == 0:
                if not Global.canEscapeCheckmate("Black",gameBoard.ChessBoard):
                    print("Black Wins!")
                    gameOver = True
                    break