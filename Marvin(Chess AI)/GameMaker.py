from Game import Game

playerOne = ""
playerTwo = ""
while not playerOne in ["a","h"]:
    playerOne = input("Is player 1 and (A)I or (H)uman player?").lower()
while not playerTwo in ["a","h"]:
    playerTwo = input("Is player 2 and (A)I or (H)uman player?").lower()
print("Game Starting!")
game = Game(playerOne, playerTwo)
game.startGame()