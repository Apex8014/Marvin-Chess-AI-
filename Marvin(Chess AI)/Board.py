from EmptySpace import EmptySpace
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

class Board:
    def __init__(self):
        #make list of the board
        self.ChessBoard = [[Rook("White"),Knight("White"),Bishop("White"),Queen("White"),King("White"),Bishop("White"),Knight("White"),Rook("White")],
                           [Pawn("White") for i in range(8)],
                           [EmptySpace() for i in range(8)],
                           [EmptySpace() for i in range(8)],
                           [EmptySpace() for i in range(8)],
                           [EmptySpace() for i in range(8)],
                           [Pawn("Black") for i in range(8)],
                           [Rook("Black"),Knight("Black"),Bishop("Black"),Queen("Black"),King("Black"),Bishop("Black"),Knight("Black"),Rook("Black")]]

    def updatePosition(self,Positions):
        pieceToBeMoved = self.ChessBoard[Positions[0,0],Positions[0,1]]
        self.ChessBoard[Positions[0,0],Positions[0,1]] = EmptySpace()
        self.ChessBoard[Positions[1,0],Positions[1,1]] = pieceToBeMoved

    def printBoard(self):
        for y in range(8):
            line = ""
            for x in range(8):
                line = line + self.ChessBoard[7-y][x].type + " "
            print(line)
