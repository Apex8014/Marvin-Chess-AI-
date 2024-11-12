import Global

class Piece:
    def __init__(self,color):
        self.color = color
        self.hasMoved = False
        self.attackedSquares = []
        self.pieceID = 0
        if color == "White":
            self.pieceID = Global.addWhitePiece(self)
            if self.type == "K":
                Global.addKing(self)
        if color == "Black":
            self.pieceID = Global.addBlackPiece(self)
            if self.type == "K":
                Global.addKing(self)

    #gets the piece's position from the board
    def getPos(self, board):
        for x in range(8):
            for y in range(8):
                if board[y][x].pieceID == self.pieceID:
                    return (x, y)
        return None
    
    #removes the piece from the global list (used for taking a piece)
    def removeFromPieces(self):
        if self.color == "White":
            for i in range(len(Global.whitePieces)):
                if Global.whitePieces[i] is self:
                    Global.removeWhitePiece(i)
                    break
        elif self.color == "Black":
            for i in range(len(Global.blackPieces)):
                if Global.blackPieces[i] is self:
                    Global.removeBlackPiece(i)
                    break
    
    #updates the squares a piece is attacking
    def updateAttackedSquares(self,board):
        pos = self.getPos(board)
        self.attackedSquares = []
        if self.type != "P":
            self.attackedSquares = self.validMoves(board)
        else:
            if 7 > pos[1] > 0:
                if pos[0]-1 > -1:
                    self.attackedSquares.append((pos[0]-1, pos[1] + {"White":1,"Black":-1}[self.color]))
                if pos[0]+1 < 8:
                    self.attackedSquares.append((pos[0]+1, pos[1] + {"White":1,"Black":-1}[self.color]))

    #Finds all squares under attack by enemy pieces and updates the self.squaresUnderAttack list
    def getAttackedSquares(self):
        self.squaresUnderAttack = []
        if self.color == "White":
            for i in Global.blackPieces:
                self.squaresUnderAttack += i.attackedSquares
            self.squaresUnderAttack += Global.kings[1].attackedSquares
        else:
            for i in Global.whitePieces:
                self.squaresUnderAttack += i.attackedSquares
            self.squaresUnderAttack += Global.kings[0].attackedSquares
        return self.squaresUnderAttack
    
    #updates attacked squares in the case of a possible discovered attack
    def discoveredAttack(self, board, updatePosition):
        if not self.type in ["P","K","N"]:
            if updatePosition in self.attackedSquares:
                self.updateAttackedSquares(board)

    #returns a boolean representing wether or not the king is in check
    def inCheck(self, board):
        if self.color == " ":
            return False
        return Global.kings[{"White":0,"Black":1}[self.color]].getPos(board) in self.getAttackedSquares()