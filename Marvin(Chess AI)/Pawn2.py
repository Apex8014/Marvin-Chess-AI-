from Piece import Piece

class Pawn(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "P"

    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList = []
        #Makes sure to not go out of bounds
        if (pos[1]+{"White":1,"Black":-1}[self.color] < 8 and pos[1]+{"White":1,"Black":-1}[self.color] > -1):
            #Basic move one movement
            if (board[pos[1]+{"White":1,"Black":-1}[self.color]][pos[0]].color == " "):
                self.movesList.append(pos[0],pos[1]+{"White":1,"Black":-1}[self.color])
                #Two movement from start
                if(pos[1] == {"White":1,"Black":6}[self.color]):
                    if (board[pos[1]+{"White":2,"Black":-2}[self.color]][pos[0]].color == " "):
                        self.movesList.append(pos[0],pos[1]+{"White":2,"Black":-2}[self.color])
        #Capturing
        for i in range(-1,2,2):
            if (pos[0]+i < 8 and pos[0]+i > -1):
                if (pos[1]+{"White":1,"Black":-1}[self.color] < 8 and pos[1]+{"White":1,"Black":-1}[self.color] > -1):
                    if (board[pos[1]+{"White":1,"Black":-1}[self.color]][pos[0]+i].color == {"White":"Black","Black":"White"}[self.color]):
                        self.movesList.append(pos[0]+i, pos[1]+{"White":1,"Black":-1}[self.color])
        #En pessant