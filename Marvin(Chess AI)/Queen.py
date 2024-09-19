from Piece import Piece

class Queen(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "Queen"