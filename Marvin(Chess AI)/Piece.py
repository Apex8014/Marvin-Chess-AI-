class Piece:
    def __init__(self,color):
        self.color = color
        self.type = "Piece"
        self.hasMoved = False
        self.attackedSquares = []
        self.blackPieces = []
        self.whitePieces = []
        if color == "White":
            self.whitePieces.append(self)
        if color == "Black":
            self.blackPieces.append(self)

    def getPos(self, board):
        for x in range(8):
            for y in range(8):
                if board[y][x] is self:
                    return (x, y)
        return None
    
    def updateAttackedSquares(self,board):
        self.attackedSquares = self.validMoves(board)

    def getAttackedSquares(self):
        self.squaresUnderAttack = []
        if self.color == "White":
            for i in self.blackPieces:
                self.squaresUnderAttack = sum([i.attackedSquares,self.squaresUnderAttack],[])
        else:
            for i in self.whitePieces:
                self.squaresUnderAttack = sum([i.attackedSquares,self.squaresUnderAttack],[])
        return self.squaresUnderAttack