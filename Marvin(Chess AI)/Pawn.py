from EmptySpace import EmptySpace
from Piece import Piece

class Pawn(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "P"

    def validMoves(self, board):
        pos = self.getPos(board)

        moves = []

        if self.color == "White":

            if pos[1] == 2:
                #Is at start
                if board[pos[0]][pos[1]+2].type == "_":
                    pass
