from Piece import Piece
import Global

class Pawn(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "P"

    def validMoves(self, board):
        pos = self.getPos(board)
        self.movesList = []
        #Makes sure to not go out of bounds
        if 8 > pos[1]+{"White":1, "Black":-1}[self.color] > -1:
            #Basic move one movement
            if board[pos[1] + {"White":1, "Black":-1}[self.color]][pos[0]].color == " ":
                self.movesList.append((pos[0],pos[1]+{"White":1,"Black":-1}[self.color]))
                #Two movement from start
                if pos[1] == {"White":1, "Black":6}[self.color]:
                    if board[pos[1] + {"White":2, "Black":-2}[self.color]][pos[0]].color == " ":
                        self.movesList.append((pos[0],pos[1]+{"White":2,"Black":-2}[self.color]))
        #Capturing
        for i in range(-1,2,2):
            if 8 > pos[0]+i > -1:
                if 8 > pos[1]+{"White":1, "Black":-1}[self.color] > -1:
                    if board[pos[1] + {"White":1, "Black":-1}[self.color]][pos[0] + i].color == {"White": "Black", "Black": "White"}[self.color]:
                        self.movesList.append((pos[0]+i, pos[1]+{"White":1,"Black":-1}[self.color]))
        #En pessant
        if pos[1] == {"White":4,"Black":3}[self.color]:
            if board[Global.mostRecentMove[1][1]][Global.mostRecentMove[1][0]].type == "P":
                if Global.mostRecentMove[1][1] == pos[1]:
                    if abs(Global.mostRecentMove[1][1]-Global.mostRecentMove[0][1]) == 2:
                        if Global.mostRecentMove[1][0] == pos[0]+1:
                            self.movesList.append((pos[0]+1,{"White":5,"Black":2}[self.color],False))
                        elif Global.mostRecentMove[1][0] == pos[0]-1:
                            self.movesList.append((pos[0]-1,{"White":5,"Black":2}[self.color],False))
        
        #Promotion
        for i in range(len(self.movesList)):
            if self.movesList[i][1] == {"White":7,"Black":0}[self.color]:
                print("Promotion available:")
                print(self.movesList[i])
                self.movesList[i] = (self.movesList[i][0],self.movesList[i][1],True)
        return self.movesList