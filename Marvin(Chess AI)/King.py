from Piece import Piece

class King(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "K"

    def validMoves(self,board):
        pos = self.getPos(board)
        self.movesList = []
        #Basic movement
        for y in range(-1,1,1):
            for x in range(-1,1,1):
                if (x == 0 and y == 0 and board.ChessBoard[pos[1]+y][pos[0]+x].type != self.type):
                    self.movesList[len(self.movesList)] = (pos[1]+y,pos[0]+x)
        #Checks for invalid moves and removes them from moves list
        self.getAttackedSquares()
        for i in range(len(self.movesList)):
            if (self.movesList[i] in self.squaresUnderAttack):
                self.movesList.pop(i)
                i-=1
        #castling
        #Checks if the king meets the requirements
        if (not self.inCheck and not self.hasMoved):
            #Kingside
            #Checks if the rook meets the requirements
            if (board[0][7].type == "R" and board[0][7].color == self.color and not board[0][7].hasMoved):
                #Checks if the other spaces are free
                if (board[0][6].type == "_" and board[0][5].type == "_" and not (6,0) in self.squaresUnderAttack and not (5,0) in self.squaresUnderAttack):
                    #The true is here to show that a special move (castling in this case) is ocuring in this move
                    self.movesList.append((0,6,True))
            #Queenside
            if (board[0][0].type == "R" and board[0][0].color == self.color and not board[0][0].hasMoved):
                #Checks if the other spaces are free
                if (board[0][3].type == "_" and board[0][2].type == "_" and not (3,0) in self.squaresUnderAttack and not (2,0) in self.squaresUnderAttack):
                    #The true is here to show that a special move (castling in this case) is ocuring in this move
                    self.movesList.append((0,2,True))
        return self.movesList


    def inCheck(self, board):
        pos = self.getPos(board)
        self.getAttackedSquares()
        if (pos in self.squaresUnderAttack):
            return True
        return False