from EmptySpace import EmptySpace
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
import Global
import random
import copy

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
        #Removes the extra 8 pieces added from the previous line from the white and black pieces list
        for i in range(4):
            Global.removeBlackPiece(len(Global.blackPieces)-1)
            Global.removeWhitePiece(len(Global.whitePieces)-1)
        #Gets all attacked squares for the start of the game
        for y in range(len(self.ChessBoard)):
            for x in range(len(self.ChessBoard[y])):
                if not self.ChessBoard[y][x].type == "K":
                    self.ChessBoard[y][x].updateAttackedSquares(self.ChessBoard)
        for i in range(2):
            Global.kings[i].updateAttackedSquares(self.ChessBoard)

    def updatePosition(self,Positions,player):
        self.pieceToBeMoved = self.ChessBoard[Positions[0][1]][Positions[0][0]]
        self.pieceToBeMovedID = self.pieceToBeMoved.pieceID
        self.ChessBoard[Positions[1][1]][Positions[1][0]].removeFromPieces()
        self.ChessBoard[Positions[0][1]][Positions[0][0]] = EmptySpace()
        self.ChessBoard[Positions[1][1]][Positions[1][0]] = self.pieceToBeMoved
        Global.updateMostRecentMove(Positions)
        #Special Moves
        if (len(Positions[1]) == 3):
            #Pawn
            if (self.ChessBoard[Positions[1][1]][Positions[1][0]].type == "P"):
                #Promotion
                if (Positions[1][2] == True):
                    if player == "h":
                        self.promotionPiece = input("What piece would you like to promote to?:").lower()
                        while self.promotionPiece not in ["knight","bishop","rook","queen"]:
                            self.promotionPiece = input("Invalid response; enter full name of piece. What piece would you like to promote to?:").lower()
                    else:
                        self.promotionPiece = ["knight","bishop","rook","queen"][random.randint(0,3)]
                    self.ChessBoard[Positions[1][1]][Positions[1][0]].removeFromPieces()
                    self.ChessBoard[Positions[1][1]][Positions[1][0]] = copy.deepcopy(self.promotions[self.promotionPiece][self.ChessBoard[Positions[1][1]][Positions[1][0]].color])
                    self.ChessBoard[Positions[1][1]][Positions[1][0]].pieceID = self.pieceToBeMovedID
                    if self.ChessBoard[Positions[1][1]][Positions[1][0]].color == "White":
                        Global.addWhitePiece(self.ChessBoard[Positions[1][1]][Positions[1][0]])
                        Global.whitePieces[len(Global.whitePieces)-1].pieceID = self.pieceToBeMovedID
                    elif self.ChessBoard[Positions[1][1]][Positions[1][0]].color == "Black":
                        Global.addBlackPiece(self.ChessBoard[Positions[1][1]][Positions[1][0]])
                        Global.blackPieces[len(Global.blackPieces)-1].pieceID = self.pieceToBeMovedID
                #En pessant
                if (Positions[1][2] == False):
                    self.ChessBoard[Positions[0][1]][Positions[1][0]].removeFromPieces()
                    self.ChessBoard[Positions[0][1]][Positions[1][0]] = EmptySpace()
            #Castling
            if (self.ChessBoard[Positions[1][1]][Positions[1][0]].type == "K"):
                self.updatePosition( ( ( {6:7,2:0}[Positions[1][0]] , Positions[1][1] ), ( {6:5,2:3}[Positions[1][0]] , Positions[1][1]) ) ,player)
        #updating the piece in the global list
        if self.ChessBoard[Positions[1][1]][Positions[1][0]].color == "White":
            for i in Global.whitePieces:
                if i.pieceID == self.ChessBoard[Positions[1][1]][Positions[1][0]].pieceID:
                    i.updateAttackedSquares(self.ChessBoard)
                    i.hasMoved = True
        elif self.ChessBoard[Positions[1][1]][Positions[1][0]].color == "Black":
            for i in Global.blackPieces:
                if i.pieceID == self.ChessBoard[Positions[1][1]][Positions[1][0]].pieceID:
                    i.updateAttackedSquares(self.ChessBoard)
                    i.hasMoved = True
        #updating the piece
        self.ChessBoard[Positions[1][1]][Positions[1][0]].hasMoved = True
        self.ChessBoard[Positions[1][1]][Positions[1][0]].updateAttackedSquares(self.ChessBoard)
        #discovered attacks
        for i in Global.blackPieces:
            i.discoveredAttack(self.ChessBoard, Positions[0])
        for i in Global.whitePieces:
            i.discoveredAttack(self.ChessBoard, Positions[0])
        #undiscovered attacks
        for i in Global.blackPieces:
            i.discoveredAttack(self.ChessBoard, Positions[1])
        for i in Global.whitePieces:
            i.discoveredAttack(self.ChessBoard, Positions[1])

    def printBoard(self):
        for y in range(8):
            line = ""
            for x in range(8):
                line += {"White":"W","Black":"B", " ":"_"}[self.ChessBoard[7-y][x].color] + self.ChessBoard[7-y][x].type + " "
            print(line)

    def printIDs(self):
        for y in range(8):
            line = ""
            for x in range(8):
                if len(str(self.ChessBoard[7-y][x].pieceID)) == 2:
                    line += str(self.ChessBoard[7-y][x].pieceID)
                if len(str(self.ChessBoard[7-y][x].pieceID)) == 1:
                    line += "_" + str(self.ChessBoard[7-y][x].pieceID)
                line += " "
            print(line)