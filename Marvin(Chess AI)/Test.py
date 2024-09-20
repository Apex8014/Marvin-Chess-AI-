from Board import Board
from Player import Player


winner = ""
WhitePlayer = Player("w")
BlackPlayer = Player("b")
gameBoard = Board()

#gameBoard.printBoard()

pos1, pos2 = 0, 2

print(gameBoard.ChessBoard[pos1][pos2].type)
print(gameBoard.ChessBoard[pos1][pos2].color)
print(gameBoard.ChessBoard[pos1][pos2].getPos(gameBoard.ChessBoard))

print(gameBoard.ChessBoard[pos1][pos2].validMoves(gameBoard.ChessBoard))
