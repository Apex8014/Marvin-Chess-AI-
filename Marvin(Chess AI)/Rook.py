from Piece import Piece

class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "R"