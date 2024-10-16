class Player:
	#playerTurn: equal to White or Black, White means the player is white, Black means black.
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
			#Debug printing statements
			#print(board[self.chosenPieceY][self.chosenPieceX].type)
			#print((self.chosenLocationX+1,self.chosenLocationY+1))
			#print((self.chosenPieceX+1,self.chosenPieceY+1))
			self.moveIsValidBase = (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board)
			if not (-1 < self.chosenPieceX < 8 and -1 < self.chosenPieceY < 8 and -1 < self.chosenLocationX < 8 and -1 < self.chosenLocationY < 8):
				print("X and/or Y values are out of range, make sure they are between 1 and 8 (inclusive).")
				continue
			if board[self.chosenPieceY][self.chosenPieceX].color != self.playerTurn:
				print("Please pick a piece of your color to move.")
				continue
			if (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
				return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY))
			elif (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
				return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,False))
			elif (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
				return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,True))
			else:
				print("Invalid input. Make sure you have the right location for the piece you wan to move and a valid location for where you would like to move the piece.")