from Piece import Piece

class King(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "K"