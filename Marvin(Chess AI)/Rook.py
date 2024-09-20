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
            if (x+pos[0] < 7):
                if (board[pos[1]][pos[0]+x].color == self.color):
                    break
                else: 
                    self.movesList[len(self.movesList)] = (pos[0]+x,pos[1])
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]+x].color != "None"):
                        break
            else:
                break

            #checks all possible leftward moves
            if (pos[0]-x < 7):
                if (board[pos[1]][pos[0]-x].color == self.color):
                    break
                else: 
                    self.movesList[len(self.movesList)] = (pos[0]-x,pos[1])
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]-x].color != "None"):
                        break
            else:
                break


        #!#!#!INCOMPLETE!#!#!#

        for y in range(8):
            #checks all possible rightward moves
            if (x == 0):
                continue
            if (x+pos[0] < 7):
                if (board[pos[1]][pos[0]+x].color == self.color):
                    break
                else: 
                    self.movesList[len(self.movesList)] = (pos[0]+x,pos[1])
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]+x].color != "None"):
                        break
            else:
                break

            #checks all possible leftward moves
            if (pos[0]-x < 7):
                if (board[pos[1]][pos[0]-x].color == self.color):
                    break
                else: 
                    self.movesList[len(self.movesList)] = (pos[0]-x,pos[1])
                    #allows the loop to keep going if there is an empty space, but ends it if taking a piece is the las possible option
                    if (board[pos[1]][pos[0]-x].color != "None"):
                        break
            else:
                break