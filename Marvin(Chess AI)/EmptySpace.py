from Piece import Piece

class EmptySpace(Piece):
    def __init__(self):
        self.type = "_"
        super().__init__(" ")

    def validMoves(self,board):
        return []
    
    def checkmateDetectionMoves(self,board):
        return []