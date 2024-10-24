from Piece import Piece

class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "N"

    def validMoves(self,board):
        self.movesList = []
        pos = self.getPos(board)
        for x in range(-2,3,1):
            for y in range(-2,3,1):
                if 8 > pos[1]+y > -1 and 8 > pos[0]+x > -1:
                    if (abs(x)+abs(y) == 3 and board[pos[1]+y][pos[0]+x].color != self.color):
                        self.movesList.append((pos[0]+x,pos[1]+y))
        
        return self.movesList