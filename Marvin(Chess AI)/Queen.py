from Piece import Piece

class Queen(Piece):
    def __init__(self,color):
        self.type = "Q"
        super().__init__(color)
    
    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList= []
        #variables to help end a section when it reaches the end of its valid moves
        self.upRight = True
        self.downRight = True
        self.upLeft = True
        self.downLeft = True
        right = True
        left = True
        up = True
        down = True
        for d in range(8):
            if d == 0:
                continue
            #checks all possible rightward moves
            if right:
                if (d+pos[0] < 8):
                    if (board[pos[1]][pos[0]+d].color == self.color):
                        right = False
                    else: 
                        self.movesList.append((pos[0]+d,pos[1]))
                        #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                        if (board[pos[1]][pos[0]+d].color != " "):
                            right = False
                else:
                    right = False

            #checks all possible leftward moves
            if left:
                if (pos[0]-d > -1):
                    if (board[pos[1]][pos[0]-d].color == self.color):
                        left = False
                    else: 
                        self.movesList.append((pos[0]-d,pos[1]))
                        #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                        if (board[pos[1]][pos[0]-d].color != " "):
                            left = False
                else:
                    left = False
            
            #checks all possible upward moves
            if up:
                if (d+pos[1] < 8):
                    if (board[pos[1]+d][pos[0]].color == self.color):
                        up = False
                    else: 
                        self.movesList.append((pos[0],pos[1]+d))
                        #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                        if (board[pos[1]+d][pos[0]].color != " "):
                            up = False
                else:
                    up = False

            #checks all possible downward moves
            if down:
                if (pos[1] - d > -1):
                    if (board[pos[1]-d][pos[0]].color == self.color):
                        down = False
                    else: 
                        self.movesList.append((pos[0],pos[1]-d))
                        #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                        if (board[pos[1]-d][pos[0]].color != " "):
                            down = False
                else:
                    down = False
            #up-right
            if 8 > pos[0] + d > -1 and 8 > pos[1] + d > -1 and self.upRight:
                if board[pos[1]+d][pos[0]+d].color != self.color:
                    self.movesList.append((pos[0]+d,pos[1]+d))
                    if board[pos[1]+d][pos[0]+d].color != " ":
                        self.upRight = False
                else:
                    self.upRight = False
            else:
                self.upRight = False

            #down-right
            if 8 > pos[0] + d > -1 and 8 > pos[1] - d > -1 and self.downRight:
                if board[pos[1]-d][pos[0]+d].color != self.color:
                    self.movesList.append((pos[0]+d,pos[1]-d))
                    if board[pos[1]-d][pos[0]+d].color != " ":
                        self.downRight = False
                else:
                    self.downRight = False
            else:
                self.downRight = False

            #down-left
            if 8 > pos[0] - d > -1 and 8 > pos[1] - d > -1 and self.downLeft:
                if board[pos[1]-d][pos[0]-d].color != self.color:
                    self.movesList.append((pos[0]-d,pos[1]-d))
                    if board[pos[1]-d][pos[0]-d].color != " ":
                        self.downLeft = False
                else:
                    self.downLeft = False
            else:
                self.downLeft = False

            #up-left
            if 8 > pos[0] - d > -1 and 8 > pos[1] + d > -1 and self.upLeft:
                if board[pos[1]+d][pos[0]-d].color != self.color:
                    self.movesList.append((pos[0]-d,pos[1]+d))
                    if board[pos[1]+d][pos[0]-d].color != " ":
                        self.upLeft = False
                else:
                    self.upLeft = False
            else:
                self.upLeft = False

        return self.movesList