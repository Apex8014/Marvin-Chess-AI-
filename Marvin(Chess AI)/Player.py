class Player:
	#playerTurn: equal to w or b, w means the player is white, b means black.
	def __init__(self, playerTurn):
		self.playerTurn = playerTurn

	#gets imput from the player to make their move
	def playerMove(self, board):
		self.moveIsValid = False
		while not self.moveIsValid:
			self.chosenPieceX = int(input("What is the x position of the piece you would like to move?(1 - 8):"))-1
			self.chosenPieceY = int(input("What is the y position of the piece you would like to move?(1 - 8):"))-1
			self.chosenLocationX = int(input("Where would you like to move the piece to? (x position, 1 - 8):"))-1
			self.chosenLocationY = int(input("Where would you like to move the piece to? (y position, 1 - 8):):"))-1
			print(board[self.chosenPieceY][self.chosenPieceX].type)
			self.moveIsValid = (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board)
			if not (-1 < self.chosenPieceX < 8 and -1 < self.chosenPieceY < 8 and -1 < self.chosenLocationX < 8 and -1 < self.chosenLocationY < 8):
				print("X and/or Y values are out of range, make sure they are between 1 and 8 (inclusive).")
				continue
			if self.moveIsValid:
				return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY))
			else:
				print("Invalid input. Make sure you have the right location for the piece you wan to move and a valid location for where you would like to move the piece.")