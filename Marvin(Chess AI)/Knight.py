from Piece import Piece

class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "N"

    def validMoves(self,board):
        self.movesList = []
        pos = self.getPos(board)
        for x in range(-2,2,1):
            for y in range(-2,2,1):
                if (abs(x)+abs(y) == 3 and board.ChessBoard[y][x].color != self.color):
                    self.movesList[len(self.movesList)] = (x,y)
        return self.movesList