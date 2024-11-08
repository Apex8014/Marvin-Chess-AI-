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

def addBlackPiece(piece):
    global blackPieces
    global pieceIDValue
    pieceIDValue+=1
    piece.pieceID = pieceIDValue
    blackPieces.append(piece)
    return pieceIDValue

def removeBlackPiece(index):
    global blackPieces
    blackPieces.pop(index)

def addWhitePiece(piece):
    global whitePieces
    global pieceIDValue
    pieceIDValue+=1
    piece.pieceID = pieceIDValue
    whitePieces.append(piece)
    return pieceIDValue

def removeWhitePiece(index):
    global whitePieces
    whitePieces.pop(index)

def addKing(piece):
    global kings
    global pieceIDValue
    if piece.color == "White":
        kings[0] = piece
    else:
        kings[1] = piece

def updateMostRecentMove(positions):
    global mostRecentMove
    mostRecentMove = positions