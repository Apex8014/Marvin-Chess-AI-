from Piece import Piece

class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "N"