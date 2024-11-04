import Global

class Piece:
    def __init__(self,color):
        self.color = color
        self.hasMoved = False
        self.attackedSquares = []
        if color == "White":
            print("White Pieces")
            Global.addWhitePiece(self)
            if self.type == "K":
                print("White King")
                Global.addKing(self)
        if color == "Black":
            print("Black Pieces")
            Global.addBlackPiece(self)
            if self.type == "K":
                print("Black King")
                Global.addKing(self)

    def getPos(self, board):
        for x in range(8):
            for y in range(8):
                if board[y][x] is self:
                    return (x, y)
        return None
    
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
        else:
            for i in Global.whitePieces:
                self.squaresUnderAttack = i.attackedSquares
        print("Squares Under Attack")
        print(self.squaresUnderAttack)
        return self.squaresUnderAttack