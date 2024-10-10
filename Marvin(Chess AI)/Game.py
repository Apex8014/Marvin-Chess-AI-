from Board import Board
from Player import Player


winner = ""
WhitePlayer = Player("w")
BlackPlayer = Player("b")
gameBoard = Board()
print("Black")
print(gameBoard.ChessBoard[1][2].getPos(gameBoard.ChessBoard))
print("White")

while(winner == ""):
    print("White to move:")
    print("Black")
    gameBoard.printBoard()
    print("White")
    gameBoard.updatePosition(WhitePlayer.playerMove(gameBoard.ChessBoard))
    #if it finds the black king, it changes the winner value to "!", if winner is not "!", then the king is gone and therefore white wins
    for x in range(8):
        for y in range(8):
            if gameBoard.ChessBoard[y][x].type == "K" and gameBoard.ChessBoard[y][x].color == "Black":
                winner = "!"
    if winner != "!":
        winner = "White"
    else:
        winner = ""
    print("Black to move:")
    print("Black")
    gameBoard.printBoard()
    print("White")
    gameBoard.updatePosition(BlackPlayer.playerMove(gameBoard.ChessBoard))
    #if it finds the white king, it changes the winner value to "!", if winner is not "!", then the king is gone and therefore black wins
    for x in range(8):
        for y in range(8):
            if gameBoard.ChessBoard[y][x].type == "K" and gameBoard.ChessBoard[y][x].color == "White":
                winner = "!"
    if winner != "!":
        winner = "Black"
    else:
        winner = ""