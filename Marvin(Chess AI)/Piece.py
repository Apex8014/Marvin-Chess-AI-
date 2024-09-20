class Piece:
    def __init__(self,color):
        self.color = color
        self.type = "Piece"
        self.hasMoved = False

    def getPos(self, board):
        for x in range(8):
            for y in range(8):
                if board[y][x] is self:
                    return (x, y)
        return None