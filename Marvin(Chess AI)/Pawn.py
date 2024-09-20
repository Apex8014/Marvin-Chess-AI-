from Piece import Piece

class Pawn(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.type = "P"

    def validMoves(self, board):
        #Get the position of this pawn
        pos = self.getPos(board)

        moves = []
        #Check if we are white or black
        if self.color == "White":
            #Check if space in front of pawn is open
            if board[pos[0]][pos[1] + 1].type == "_":
                moves.append((pos[0], pos[1] + 1))
            #Logic for a pawn at its starting location
            if pos[1] == 1:
                print(board[pos[0]][pos[1]+2].type)
                if board[pos[0]][pos[1]+2].type == "_":
                    moves.append((pos[0], pos[1]+2))

            """#Check if there is a piece to the left or right diagonally
            if pos[0] + 1 < len(board) and board[pos[0] + 1][pos[1] + 1].type == (not "_") and board[pos[0] + 1][
                pos[1] + 1].color != self.color:
                moves.append((pos[0] + 1, pos[1] + 1))
            if pos[0] - 1 >= 0 and board[pos[0] - 1][pos[1] + 1].type == (not "_") and board[pos[0] - 1][
                pos[1] + 1].color != self.color:
                moves.append((pos[0] - 1, pos[1] + 1))"""

        #If this gets through we are black
        else:
            #Yeah, were black
            #Now I just copy and paste all the code from white and change a few values :)
            #Equality ✊🏻

            # Check if space in front of pawn is open
            if board[pos[0]][pos[1] - 1].type == "_":
                moves.append((pos[0], pos[1] - 1))
            # Logic for a pawn at its starting location
            if pos[1] == 6:
                print(board[pos[0]][pos[1] - 2].type)
                if board[pos[0]][pos[1] - 2].type == "_":
                    moves.append((pos[0], pos[1] - 2))

            """# Check if there is a piece to the left or right diagonally
            if pos[0] + 1 < len(board) and board[pos[0] + 1][pos[1] - 1].type == (not "_") and board[pos[0] + 1][
                pos[1] - 1].color != self.color:
                print(board[pos[0] + 1][pos[0] -1])
                moves.append((pos[0] + 1, pos[1] - 1))
            if pos[0] - 1 >= 0 and board[pos[0] - 1][pos[1] - 1].type == (not "_") and board[pos[0] - 1][
                pos[1] - 1].color != self.color:
                print(board[pos[0] - 1][pos[0] - 1])
                moves.append((pos[0] - 1, pos[1] - 1))"""


        return moves
