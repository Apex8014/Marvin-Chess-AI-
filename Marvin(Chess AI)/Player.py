class Player:
	#playerTurn: equal to w or b, w means the player is white, b means black.
	def __init__(self, playerTurn):
		self.playerTurn = playerTurn

	#gets imput from the player to make their move
	def playerMove(self):
		self.chosenPieceX = int(input("What is the x position of the piece you would like to move?(1 - 8):"))
		self.chosenPieceY = int(input("What is the y position of the piece you would like to move?(1 - 8):"))
		self.chosenLocationX = int(input("Where would you like to move the piece to? (x position, 1 - 8):"))
		self.chosenLocationY = int(input("Where would you like to move the piece to? (y position, 1 - 8):):"))
		return ((self.chosenPieceX-1,self.chosenPieceY-1),(self.chosenLocationX-1,self.chosenLocationY-1))