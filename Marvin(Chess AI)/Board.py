import EmptySpace
import Pawn
import Knight
import Bishop
import Rook
import Queen
import King

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
