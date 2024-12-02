from Piece import Piece

class Knight(Piece):
    def __init__(self,color):
        self.type = "N"
        super().__init__(color)
    
    def validMoves(self,board):
        self.movesList = []
        pos = self.getPos(board)
        for x in range(-2,3,1):
            for y in range(-2,3,1):
                if 8 > pos[1]+y > -1 and 8 > pos[0]+x > -1:
                    if abs(x)+abs(y) == 3:
                        self.movesList.append((pos[0]+x,pos[1]+y))
        
        return self.movesList