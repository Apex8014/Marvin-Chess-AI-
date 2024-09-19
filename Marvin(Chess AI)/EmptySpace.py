from Piece import Piece

class EmptySpace(Piece):
    def __init__(self):
        super().__init__(" ")
        self.type = "_"