global blackPieces
blackPieces = []
global whitePieces
whitePieces = []
#white king, black king
global kings
kings = [0,0]
global mostRecentMove
mostRecentMove = ((4,4),(4,4))
global pieceIDValue
pieceIDValue = 0

#adds a black piece to the blackPieces list
def addBlackPiece(piece):
    global blackPieces
    global pieceIDValue
    pieceIDValue+=1
    piece.pieceID = pieceIDValue
    blackPieces.append(piece)
    return pieceIDValue

#removes a black piece to the blackPieces list
def removeBlackPiece(index):
    global blackPieces
    blackPieces.pop(index)

#adds a white piece to the whitePieces list
def addWhitePiece(piece):
    global whitePieces
    global pieceIDValue
    pieceIDValue+=1
    piece.pieceID = pieceIDValue
    whitePieces.append(piece)
    return pieceIDValue

#removes a white piece to the whitePieces list
def removeWhitePiece(index):
    global whitePieces
    whitePieces.pop(index)

#adds a king to the kings list
def addKing(piece):
    global kings
    global pieceIDValue
    if piece.color == "White":
        kings[0] = piece
    else:
        kings[1] = piece

#updates the most recent move
def updateMostRecentMove(positions):
    global mostRecentMove
    mostRecentMove = positions

#returns a value equal to how many ways position 2 is in between position1 and position3 (1 means it is directely left, right, up, or down and in between, 2 means it is in between in a diagonal)
def positionBetweenPositions(position1, position2, position3):
    i = 0
    if position1[0] > position2[0] > position3[0]:
        i+=1
    if position1[1] > position2[1] > position3[1]:
        i+=1
    if position1[0] < position2[0] < position3[0]:
        i+=1
    if position1[1] > position2[1] > position3[1]:
        i+=1
    return i

#detects if checkmate can be escaped by taking a piece or blocking an attack
def canEscapeCheckmate(color,board):
    #detects if the king is even in check (failsafe plus makes things easier)
    if kings[{"White":0,"Black":1}[color]].inCheck(board):
        #detects if escaping checkmate is possible
        if len(kings[{"White":0,"Black":1}[color]].attackedByPieces(board)) == 1:
            #detects if a piece can be taken to prevent checkmate
            if kings[{"White":0,"Black":1}[color]].attackedByPieces(board)[0].getPos(board) in kings[{"White":1,"Black":0}[color]].getAttackedSquares():
                return True
            #detects if a piece can be moved in the way to prevent checkmate
            for i in kings[{"White":0,"Black":1}[color]].attackedByPieces(board):
                #you can't block checkmate from a knight or pawn (if you can't take the pawn)
                if i.type == "N" or i.type == "P":
                    return False
                #blocking checkmate from a rook and a queen
                elif i.type == "R" or (i.type == "Q" and (i.getPos(board)[0] == kings[{"White":0,"Black":1}[color]].getPos(board)[0] or i.getPos(board)[1] == kings[{"White":0,"Black":1}[color]].getPos(board)[1])):
                    for move in kings[{"White":1,"Black":0}[color]].getAttackedSquares():
                        return positionBetweenPositions(i.getPos(board), move, kings[{"White":0,"Black":1}[color]].getPos(board)) == 1
                #blocking checkmate from a bishop and a queen
                elif i.type == "B" or (i.type == "Q" and abs(i.getPos(board)[0] - kings[{"White":0,"Black":1}[color]].getPos(board)[0]) == abs(i.getPos(board)[1] - kings[{"White":0,"Black":1}[color]].getPos(board)[1])):
                    for move in kings[{"White":1,"Black":0}[color]].getAttackedSquares():
                        #checks if the move is somewhere in the diagonal
                        if positionBetweenPositions(i.getPos(board), move, kings[{"White":0,"Black":1}[color]].getPos(board)) == 2:
                            #checks if the move is in the bishop/queen diagonal
                            if abs(move[0]-i.getPos(board)[0]) == abs(move[1]-i.getPos(board)[1]):
                                return True
        return False
    else:
        return False