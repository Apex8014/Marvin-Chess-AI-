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