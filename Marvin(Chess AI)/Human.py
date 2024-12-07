from Player import Player
import copy
import Global

class Human(Player):
    def __init__(self,playerTurn):
        super().__init__(playerTurn)

    def getMove(self,board,boardClass):
        while True:
            try:
                self.chosenPieceX = int(input("What is the x position of the piece you would like to move?(1 - 8):"))-1
                self.chosenPieceY = int(input("What is the y position of the piece you would like to move?(1 - 8):"))-1
                self.chosenLocationX = int(input("Where would you like to move the piece to? (x position, 1 - 8):"))-1
                self.chosenLocationY = int(input("Where would you like to move the piece to? (y position, 1 - 8):):"))-1
            except:
                #failsafe for if a string is entered
                print("numbers only")
                continue
            if not (-1 < self.chosenPieceX < 8 and -1 < self.chosenPieceY < 8 and -1 < self.chosenLocationX < 8 and -1 < self.chosenLocationY < 8):
                print("X and/or Y values are out of range, make sure they are between 1 and 8 (inclusive).")
                continue
            #Verifies you chose a piece of your color
            if board[self.chosenPieceY][self.chosenPieceX].color != self.playerTurn:
                print("Please pick a piece of your color to move.")
                continue
            if Global.testMove(self.chosenPieceX, self.chosenPieceY, self.chosenLocationX, self.chosenLocationY, board, boardClass, self.playerTurn, "h", True):
				#returns the move
                if (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
                    return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY))
                elif (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
                    return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,False))
                elif (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
                    return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,True))