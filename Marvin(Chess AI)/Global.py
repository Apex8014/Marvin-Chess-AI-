blackPieces = []
whitePieces = []
#white king, black king
kings = [0,0]

def addBlackPiece(piece):
    blackPieces.append(piece)

def removeBlackPiece(index):
    blackPieces.pop(index)

def addWhitePiece(piece):
    whitePieces.append(piece)

def removeWhitePiece(index):
    whitePieces.pop(index)

def addKing(piece):
    if piece.color == "White":
        kings[0] = piece
    else:
        kings[1] = piece