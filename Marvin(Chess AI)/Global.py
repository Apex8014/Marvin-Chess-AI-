global blackPieces
blackPieces = []
global whitePieces
whitePieces = []
#white king, black king
global kings
kings = [0,0]
global mostRecentMove
mostRecentMove = ((4,4),(4,4))

def addBlackPiece(piece):
    global blackPieces
    blackPieces.append(piece)

def removeBlackPiece(index):
    global blackPieces
    blackPieces.pop(index)

def addWhitePiece(piece):
    global whitePieces
    whitePieces.append(piece)

def removeWhitePiece(index):
    global whitePieces
    whitePieces.pop(index)

def addKing(piece):
    global kings
    if piece.color == "White":
        kings[0] = piece
    else:
        kings[1] = piece

def updateMostRecentMove(positions):
    global mostRecentMove
    mostRecentMove = positions