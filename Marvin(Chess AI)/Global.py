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