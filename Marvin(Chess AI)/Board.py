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
        #A list of blank pieces to make promotion easier and more efficient
        self.promotions = {"queen": {"Black": Queen("Black"), "White": Queen("White")},"knight": {"Black": Knight("Black"), "White": Knight("White")},"rook": {"Black": Rook("Black"), "White": Rook("White")},"bishop": {"Black": Bishop("Black"), "White": Bishop("White")}}

    def updatePosition(self,Positions):
        pieceToBeMoved = self.ChessBoard[Positions[0][1]][Positions[0][0]]
        self.ChessBoard[Positions[0][1]][Positions[0][0]] = EmptySpace()
        self.ChessBoard[Positions[1][1]][Positions[1][0]] = pieceToBeMoved
        #Special Moves
        if (len(Positions[1]) == 3):
            #Pawn
            if (self.ChessBoard[Positions[1][1]][Positions[1][0]].type == "P"):
                #Promotion
                if (Positions[1][2] == True):
                    self.promotionPiece = input("What piece would you like to promote to?:").lower()
                    while self.promotionPiece not in ["knight","bishop","rook","queen"]:
                        self.promotionPiece = input("Invalid response; enter full name of piece. What piece would you like to promote to?:").lower()
                    self.ChessBoard[Positions[1][1]][Positions[1][0]] = self.promotions[self.promotionPiece][self.ChessBoard[Positions[1][1]][Positions[1][0]].color]
                #En pessant
                if (Positions[1][2] == False):
                    self.ChessBoard[Positions[1][1]-{"Black":-1,"White":1}[pieceToBeMoved.color]][Positions[1][0]] == EmptySpace()
        self.ChessBoard[Positions[1][1]][Positions[1][0]].hasMoved = True
        self.ChessBoard[Positions[1][1]][Positions[1][0]].updateAttackedSquares(self.ChessBoard)


    def printBoard(self):
        for y in range(8):
            line = ""
            for x in range(8):
                line = line + self.ChessBoard[7-y][x].type + " "
            print(line)
