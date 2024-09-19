class Player:
	#playerTurn: equal to w or b, w means the player is white, b means black.
	def __init__(self, playerTurn):
		self.playerTurn = playerTurn

	#gets imput from the player to make their move
	def playerMove(self):
		self.chosenPieceX = input("What is the x position of the piece you would like to move?")
		self.chosenPieceY = input("What is the y position of the piece you would like to move?")
		self.chosenLocationX = input("Where would you like to move the piece to? (x position):")
		self.chosenLocationY = input("Where would you like to move the piece to? (y position):")
		return ((self.chosenPieceX,self.chosenPieceY),(self.chosenLocationX,self.chosenLocationY))