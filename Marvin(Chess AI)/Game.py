from Board import Board
from Player import Player


winner = ""
WhitePlayer = Player("w")
BlackPlayer = Player("b")
gameBoard = Board()

print(gameBoard.ChessBoard[1][2].getPos(gameBoard.ChessBoard))
"""
while(winner != ""):
    Board.updatePosition(WhitePlayer.playerMove())
    Board.updatePosition(BlackPlayer.playerMove())
    """

