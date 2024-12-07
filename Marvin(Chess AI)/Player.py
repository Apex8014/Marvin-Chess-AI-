import Global
import copy

class Player:
	#playerTurn: equal to White or Black, White means the player is white, Black means black.
	def __init__(self, playerTurn):
		self.playerTurn = playerTurn

	"""
	#gets imput from the player to make their move
	def playerMove(self, board, boardClass):
		self.moveIsValid = False
		self.boardDuplicate = copy.deepcopy(boardClass)
		self.boardBackup = copy.deepcopy(board)
		self.boardDuplicateBackup = copy.deepcopy(boardClass)
		self.mostRecentMove = copy.deepcopy(Global.mostRecentMove)
		self.blackPieces = copy.deepcopy(Global.blackPieces)
		self.whitePieces = copy.deepcopy(Global.whitePieces)
		while not self.moveIsValid:
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
			else:
				self.moveIsValidBase = (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board) or (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board)
			#Verifies you chose a piece of your color
			if board[self.chosenPieceY][self.chosenPieceX].color != self.playerTurn:
				print("Please pick a piece of your color to move.")
				continue
			if Global.testMove(self.chosenPieceX, self.chosenPieceY, self.chosenLocationX, self.chosenLocationY, board, boardClass, self.playerTurn, True):
				#returns the move
				if (self.chosenLocationX,self.chosenLocationY) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
					self.moveIsValid = True
					return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY))
				elif (self.chosenLocationX,self.chosenLocationY,False) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
					self.moveIsValid = True
					return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,False))
				elif (self.chosenLocationX,self.chosenLocationY,True) in board[self.chosenPieceY][self.chosenPieceX].validMoves(board):
					self.moveIsValid = True
					return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY,True))
	"""