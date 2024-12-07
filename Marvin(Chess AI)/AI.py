from Player import Player
import Global
import random

class AI(Player):
    def __init__(self,playerTurn):
        super().__init__(playerTurn)

    #returns a random move from the possible moves (depth 0)
    def getMove(self,board,boardClass):
        possibleMoves = []
        if self.playerTurn == "White":
            for piece in Global.whitePieces:
                position = piece.getPos(board)
                for move in piece.validMoves(board):
                    if board[move[1]][move[0]].color != "White":
                        possibleMoves.append((position,move))
        if self.playerTurn == "Black":
            for piece in Global.blackPieces:
                position = piece.getPos(board)
                for move in piece.validMoves(board):
                    if board[move[1]][move[0]].color != "Black":
                        possibleMoves.append((position,move))
        i = 0
        while i < len(possibleMoves):
            if board[possibleMoves[i][1][1]][possibleMoves[i][1][0]].color == self.playerTurn or not Global.testMove(possibleMoves[i][0][0], possibleMoves[i][0][1], possibleMoves[i][1][0], possibleMoves[i][1][1], board, boardClass, self.playerTurn, "a", False):
                possibleMoves.pop(i)
            else:
                i+=1
        return possibleMoves[random.randint(0,len(possibleMoves)-1)]