from Piece import Piece

class Bishop(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "B"


    def validMoves(self, board):
        # Get the position of this piece
        pos = self.getPos(board)

        moves = []

        # Check diagonals up and to the left
        noPiece = True

        testX, testY = pos[0], pos[1]

        while noPiece:
            testX += 1
            testY += 1
            if testX == 7 or testY == 7:
                noPiece = False
            if testX < 0 or testY < 0:
                noPiece = False
            if board[testY][testX].type == "_":
                moves.append((testX, testY))
            elif board[testY][testX].type != "":
                moves.append((testX, testY))
                noPiece = False
            else:
                noPiece = False

        # Check diagonals up and to the right
        noPiece = True

        testX, testY = pos[0], pos[1]

        while noPiece:
            testX -= 1
            testY += 1
            if testX == 7 or testY == 7:
                noPiece = False
            if testX < 0 or testY < 0:
                noPiece = False
            if board[testY][testX].type == "_":
                moves.append((testX, testY))
            elif board[testY][testX].type != "":
                moves.append((testX, testY))
                noPiece = False
            else:
                noPiece = False

        # Check diagonals down and to the left
        noPiece = True

        testX, testY = pos[0], pos[1]

        while noPiece:
            testX += 1
            testY -= 1
            if testX == 7 or testY == 7:
                noPiece = False
            if testX < 0 or testY < 0:
                noPiece = False
            if board[testY][testX].type == "_":
                moves.append((testX, testY))
            elif board[testY][testX].type != "":
                moves.append((testX, testY))
                noPiece = False
            else:
                noPiece = False

        # Check diagonals down and to the right
        noPiece = True

        testX, testY = pos[0], pos[1]

        while noPiece:
            testX -= 1
            testY -= 1
            if testX == 7 or testY == 7:
                noPiece = False
            if testX < 0 or testY < 0:
                noPiece = False
            if board[testY][testX].type == "_":
                moves.append((testX, testY))
            elif board[testY][testX].type != "":
                moves.append((testX, testY))
                noPiece = False
            else:
                noPiece = False

        return moves