import Global

class Piece:
    def __init__(self,color):
        self.color = color
        self.type = "Piece"
        self.hasMoved = False
        self.attackedSquares = []
        if color == "White":
            Global.addWhitePiece(self)
            if self.type == "K":
                Global.addKing(self)
        if color == "Black":
            Global.addBlackPiece(self)
            if self.type == "K":
                Global.addKing(self)

    def getPos(self, board):
        for x in range(8):
            for y in range(8):
                if board[y][x] is self:
                    return (x, y)
        return None
    
    def updateAttackedSquares(self,board):
        self.attackedSquares = self.validMoves(board)

    #Finds all squares under attack by enemy pieces and updates the self.squaresUnderAttack list
    def getAttackedSquares(self):
        self.squaresUnderAttack = []
        if self.color == "White":
            for i in Global.blackPieces:
                self.squaresUnderAttack = sum([i.attackedSquares,self.squaresUnderAttack],[])
        else:
            for i in Global.whitePieces:
                self.squaresUnderAttack = sum([i.attackedSquares,self.squaresUnderAttack],[])