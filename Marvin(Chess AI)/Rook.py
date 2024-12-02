from Piece import Piece

class Rook(Piece):
    def __init__(self,color):
        self.type = "R"
        super().__init__(color)
        
    def validMoves(self,board):
        pos = self.getPos(board)
        #variables to help end a section when it reaches the end of its valid moves
        right = True
        left = True
        up = True
        down = True
        self.movesList= []
        for d in range(8):
            #checks all possible rightward moves
            if (d == 0):
                continue
            if right:
                if (d+pos[0] < 8):
                    self.movesList.append((pos[0]+d,pos[1]))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]+d].color != " "):
                        right = False
                else:
                    right = False

            #checks all possible leftward moves
            if left:
                if (pos[0]-d > -1):
                    self.movesList.append((pos[0]-d,pos[1]))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]-d].color != " "):
                        left = False
                else:
                    left = False
            
            #checks all possible upward moves
            if up:
                if (d+pos[1] < 8):
                    self.movesList.append((pos[0],pos[1]+d))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]+d][pos[0]].color != " "):
                        up = False
                else:
                    up = False

            #checks all possible downward moves
            if down:
                if (pos[1] - d > -1):
                    self.movesList.append((pos[0],pos[1]-d))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]-d][pos[0]].color != " "):
                        down = False
                else:
                    down = False

        return self.movesList