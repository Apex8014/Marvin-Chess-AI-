from Piece import Piece

class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "R"

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
            if (pos[0]-x > -1):
                if (board[pos[1]][pos[0]-x].color == self.color):
                    break
                else: 
                    self.movesList.append((pos[0]-x,pos[1]))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]-x].color != " "):
                        break
            else:
                break

        for y in range(8):
            #checks all possible rightward moves
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
            #checks all possible leftward moves
            if (pos[1]-y > -1):
                if (board[pos[1]-y][pos[0]].color == self.color):
                    break
                else: 
                    self.movesList.append((pos[0],pos[1]-y))
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]-y][pos[0]].color != " "):
                        break
            else:
                break

        return self.movesList