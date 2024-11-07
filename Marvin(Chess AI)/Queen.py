from Piece import Piece

class Queen(Piece):
    def __init__(self,color):
        self.type = "Q"
        super().__init__(color)
    
    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList= []
        for x in range(8):
            #checks all possible rightward moves
            if (x == 0):
                continue
            if (x+pos[0] < 8):
                if (board[pos[1]][pos[0]+x].color == self.color):
                    break
                else: 
                    self.movesList.append((pos[0]+x,pos[1]))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]+x].color != " "):
                        break
            else:
                break
        
        
        for x in range(8):
            #checks all possible leftward moves
            if (x == 0):
                continue
            if (pos[0]-x > -1):
                if (board[pos[1]][pos[0]-x].color == self.color):
                    #print(pos[0]-x)
                    break
                else: 
                    self.movesList.append((pos[0]-x,pos[1]))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]-x].color != " "):
                        break
            else:
                break
        
        
        for y in range(8):
            #checks all possible upward moves
            if (y == 0):
                continue
            if (y+pos[1] < 8):
                if (board[pos[1]+y][pos[0]].color == self.color):
                    break
                else: 
                    self.movesList.append((pos[0],pos[1]+y))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]+y][pos[0]].color != " "):
                        break
            else:
                break
        

        for y in range(8):
            #checks all possible upward moves
            if (y == 0):
                continue
            if (pos[1] - y > -1):
                if (board[pos[1]-y][pos[0]].color == self.color):
                    break
                else: 
                    self.movesList.append((pos[0],pos[1]-y))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]-y][pos[0]].color != " "):
                        break
            else:
                break

        self.upRight = True
        self.downRight = True
        self.upLeft = True
        self.downLeft = True
        for d in range(8):
            if d == 0:
                continue
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