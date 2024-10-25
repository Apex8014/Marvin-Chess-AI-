from Piece import Piece

class King(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "K"

    def validMoves(self,board):
        pos = self.getPos(board)
        self.movesList = []
        #Basic movement
        for y in range(-1,2,1):
            for x in range(-1,2,1):
                if 8 > pos[1]+y > -1 and 8 > pos[0]+x > -1:
                    if not (x==0 and y == 0) and board[pos[1]+y][pos[0]+x].color != self.color:
                        self.movesList.append((pos[0]+x,pos[1]+y))
        #Checks for invalid moves and removes them from moves list
        self.getAttackedSquares()
        self.checkToItem = len(self.movesList)
        i = 0
        while i < self.checkToItem:
            if self.movesList[i] in self.squaresUnderAttack:
                self.movesList.pop(i)
                self.checkToItem -= 1
            else:
                i += 1
        #castling
        #Checks if the king meets the requirements
        if (not self.inCheck(board) and not self.hasMoved):
            #Kingside
            #Checks if the rook meets the requirements
            if (board[pos[1]][7].type == "R" and board[pos[1]][7].color == self.color and not board[pos[1]][7].hasMoved):
                #Checks if the other spaces are free
                if (board[pos[1]][6].type == "_" and board[pos[1]][5].type == "_" and not (6,pos[1]) in self.squaresUnderAttack and not (5,pos[1]) in self.squaresUnderAttack):
                    #The true is here to show that a special move (castling in this case) is ocuring in this move
                    self.movesList.append((6,pos[1],True))
            #Queenside
            if (board[pos[1]][0].type == "R" and board[pos[1]][0].color == self.color and not board[pos[1]][0].hasMoved):
                #Checks if the other spaces are free
                if (board[pos[1]][3].type == "_" and board[pos[1]][2].type == "_" and not (3,pos[1]) in self.squaresUnderAttack and not (2,pos[1]) in self.squaresUnderAttack):
                    #The true is here to show that a special move (castling in this case) is ocuring in this move
                    self.movesList.append((2,pos[1],True))

        return self.movesList


    def inCheck(self, board):
        pos = self.getPos(board)
        self.getAttackedSquares()
        if (pos in self.squaresUnderAttack):
            return True
        return False