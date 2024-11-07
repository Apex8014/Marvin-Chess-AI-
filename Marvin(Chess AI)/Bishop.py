from Piece import Piece

class Bishop(Piece):
    def __init__(self,color):
        self.type = "B"
        super().__init__(color)

    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList= []
        self.upRight = True
        self.downRight = True
        self.upLeft = True
        self.downLeft = True
        for d in range(8):
            if d == 0:
                continue
            #up-right
            if 8 > pos[0] + d > -1 and 8 > pos[1] + d > -1 and self.upRight:
                if board[pos[1]+d][pos[0]+d] != self.color:
                    self.movesList.append((pos[0]+d,pos[1]+d))
                    if board[pos[1]+d][pos[0]+d] != " ":
                        self.upRight = False
                else:
                    self.upRight = False
            else:
                self.upRight = False

            #down-right
            if 8 > pos[0] + d > -1 and 8 > pos[1] - d > -1 and self.downRight:
                if board[pos[1]-d][pos[0]+d] != self.color:
                    self.movesList.append((pos[0]+d,pos[1]-d))
                    if board[pos[1]-d][pos[0]+d] != " ":
                        self.downRight = False
                else:
                    self.downRight = False
            else:
                self.downRight = False

            #down-left
            if 8 > pos[0] - d > -1 and 8 > pos[1] - d > -1 and self.downLeft:
                if board[pos[1]-d][pos[0]-d] != self.color:
                    self.movesList.append((pos[0]-d,pos[1]-d))
                    if board[pos[1]-d][pos[0]-d] != " ":
                        self.downLeft = False
                else:
                    self.downLeft = False
            else:
                self.downLeft = False

            #up-left
            if 8 > pos[0] - d > -1 and 8 > pos[1] + d > -1 and self.upLeft:
                if board[pos[1]+d][pos[0]-d] != self.color:
                    self.movesList.append((pos[0]-d,pos[1]+d))
                    if board[pos[1]+d][pos[0]-d] != " ":
                        self.upLeft = False
                else:
                    self.upLeft = False
            else:
                self.upLeft = False

        return self.movesList