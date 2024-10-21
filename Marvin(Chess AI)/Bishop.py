from Piece import Piece

class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "B"

    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList= []
        self.upRight = True
        self.downRight = True
        self.upLeft = True
        self.downLeft = True
        for x in range(8):
            for y in range(8):
                #up-right
                if 8 > pos[0] + x > -1 and 8 > pos[0] + y > -1 and self.upRight:
                    if board[pos[1]+y][pos[0]+x] != self.color:
                        self.movesList.append((pos[0]+x,pos[1]+y))
                        if board[pos[1]+y][pos[0]+x] != " ":
                            self.upRight = False
                    else:
                        self.upRight = False
                else:
                    self.upRight = False

                #down-right
                if 8 > pos[0] + x > -1 and 8 > pos[0] - y > -1 and self.downRight:
                    if board[pos[1]-y][pos[0]+x] != self.color:
                        self.movesList.append((pos[0]+x,pos[1]-y))
                        if board[pos[1]-y][pos[0]+x] != " ":
                            self.downRight = False
                    else:
                        self.downRight = False
                else:
                    self.downRight = False

                #down-left
                if 8 > pos[0] - x > -1 and 8 > pos[0] - y > -1 and self.downLeft:
                    if board[pos[1]-y][pos[0]-x] != self.color:
                        self.movesList.append((pos[0]-x,pos[1]-y))
                        if board[pos[1]-y][pos[0]-x] != " ":
                            self.downLeft = False
                    else:
                        self.downLeft = False
                else:
                    self.downLeft = False

                #up-left
                if 8 > pos[0] - x > -1 and 8 > pos[0] + y > -1 and self.upLeft:
                    if board[pos[1]+y][pos[0]-x] != self.color:
                        self.movesList.append((pos[0]-x,pos[1]+y))
                        if board[pos[1]+y][pos[0]-x] != " ":
                            self.upLeft = False
                    else:
                        self.upLeft = False
                else:
                    self.upLeft = False