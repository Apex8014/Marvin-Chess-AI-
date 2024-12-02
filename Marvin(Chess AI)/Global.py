import copy

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

#returns true if a possible move is valid, otherwise, it returns false with the option to show print statements explaining why the move isnt valid.
def testMove(chosenPieceX, chosenPieceY, chosenLocationX, chosenLocationY, board, boardClass, playerTurn, printStatements):
    global mostRecentMove
    global whitePieces
    global blackPieces
    boardDuplicate = copy.deepcopy(boardClass)
    boardBackup = copy.deepcopy(board)
    boardDuplicateBackup = copy.deepcopy(boardClass)
    mostRecentMove = copy.deepcopy(mostRecentMove)
    blackPieces = copy.deepcopy(blackPieces)
    whitePieces = copy.deepcopy(whitePieces)
    #Verifies that the move made does not put you in check
    if (chosenLocationX,chosenLocationY) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY)))
    elif (chosenLocationX,chosenLocationY,False) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY,False)))
    elif (chosenLocationX,chosenLocationY,True) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY,True)))
    else:
        if printStatements:
            print("Invalid input. Make sure you have the right location for the piece you want to move and a valid location for where you would like to move the piece.")
        return False
    if boardDuplicate.ChessBoard[chosenLocationY][chosenLocationX].inCheck(boardDuplicate.ChessBoard):
        if printStatements:
            print("Invalid move: Check")
        #resets the attacked squares because they are changed when checking for check
        mostRecentMove = mostRecentMove
        whitePieces = whitePieces
        blackPieces = blackPieces
        board = boardBackup
        boardDuplicate = boardDuplicateBackup
        for i in blackPieces:
            pos = i.getPos(board)
            i.hasMoved = board[pos[1]][pos[0]].hasMoved
            i.updateAttackedSquares(board)
        for i in whitePieces:
            pos = i.getPos(board)
            i.hasMoved = board[pos[1]][pos[0]].hasMoved
            i.updateAttackedSquares(board)
        return False
    if len(whitePieces) != len(whitePieces) and playerTurn == "White":
        if printStatements:
            print("You can not take your own pieces")
        return False
    if len(blackPieces) != len(blackPieces) and playerTurn == "Black":
        if printStatements:
            print("You can not take your own pieces")
        return False
    #resets the attacked squares because they are changed when checking for check
    mostRecentMove = mostRecentMove
    whitePieces = whitePieces
    blackPieces = blackPieces
    board = boardBackup
    for i in blackPieces:
        pos = i.getPos(board)
        i.hasMoved = board[pos[1]][pos[0]].hasMoved
        i.updateAttackedSquares(board)
    for i in whitePieces:
        pos = i.getPos(board)
        i.hasMoved = board[pos[1]][pos[0]].hasMoved
        i.updateAttackedSquares(board)
    return True

#treat this function as a filter for moves that could escape checkmate when in check but a move is possible
#detects if checkmate can be escaped by taking a piece or blocking an attack
def canEscapeCheckmate(color,board,boardClass):
    #detects if the king is even in check (failsafe plus makes things easier)
    if kings[{"White":0,"Black":1}[color]].inCheck(board):
        if len(kings[{"White":0,"Black":1}[color]].filterValidMoves(board)) == 0:
            #detects if escaping checkmate is possible
            if len(kings[{"White":0,"Black":1}[color]].attackedByPieces(board)) == 1:
                #detects if a piece can be taken to prevent checkmate
                if len(kings[{"White":0,"Black":1}[color]].attackedByPieces(board)[0].attackedByPieces(board)) > 0 :
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
        else:
            kingPosition = kings[{"White":0,"Black":1}[color]].getPos(board)
            for move in kings[{"White":0,"Black":1}[color]].filterValidMoves(board):
                if testMove(kingPosition[0],kingPosition[1],move[0],move[1],board,boardClass,color,False):
                    return True
        return False
    else:
        return True