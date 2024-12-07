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
global promoteToPiece
promoteToPiece = ""

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
    if position1[1] < position2[1] < position3[1]:
        i+=1
    return i

#returns true if a possible move is valid, otherwise, it returns false with the option to show print statements explaining why the move isnt valid.
def testMove(chosenPieceX, chosenPieceY, chosenLocationX, chosenLocationY, board, boardClass, playerTurn, player, printStatements):
    global mostRecentMove
    global whitePieces
    global blackPieces
    boardDuplicate = copy.deepcopy(boardClass)
    boardBackup = copy.deepcopy(board)
    boardDuplicateBackup = copy.deepcopy(boardClass)
    mostRecentMoveBackup = copy.deepcopy(mostRecentMove)
    blackPiecesBackup = copy.deepcopy(blackPieces)
    whitePiecesBackup = copy.deepcopy(whitePieces)
    #Verifies that the move made does not put you in check
    if (chosenLocationX,chosenLocationY) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY)),player)
    elif (chosenLocationX,chosenLocationY,False) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY,False)),player)
    elif (chosenLocationX,chosenLocationY,True) in boardDuplicate.ChessBoard[chosenPieceY][chosenPieceX].validMoves(boardDuplicate.ChessBoard):
        boardDuplicate.updatePosition(((chosenPieceX,chosenPieceY),(chosenLocationX,chosenLocationY,True)),player)
    else:
        if printStatements:
            print("Invalid input. Make sure you have the right location for the piece you want to move and a valid location for where you would like to move the piece.")
        return False
    if boardDuplicate.ChessBoard[chosenLocationY][chosenLocationX].inCheck(boardDuplicate.ChessBoard):
        if printStatements:
            print("Invalid move: Check")
        #resets the attacked squares because they are changed when checking for check
        mostRecentMove = mostRecentMoveBackup
        whitePieces = whitePiecesBackup
        blackPieces = blackPiecesBackup
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
    if len(whitePiecesBackup) != len(whitePieces) and playerTurn == "White":
        if printStatements:
            print("You can not take your own pieces")
        return False
    if len(blackPiecesBackup) != len(blackPieces) and playerTurn == "Black":
        if printStatements:
            print("You can not take your own pieces")
        return False
    #resets the attacked squares because they are changed when checking for check
    mostRecentMove = mostRecentMoveBackup
    whitePieces = whitePiecesBackup
    blackPieces = blackPiecesBackup
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
def canEscapeCheckmate(color,board,boardClass,player):
    #detects if the king is even in check (failsafe plus makes things easier)
    if kings[{"White":0,"Black":1}[color]].inCheck(board):
        #detects if the king can move
        if len(kings[{"White":0,"Black":1}[color]].filterValidMoves(board,boardClass,player)) == 0:
            #detects if escaping checkmate is possible
            if len(kings[{"White":0,"Black":1}[color]].attackedByPieces(board)) == 1:
                #detects if a piece can be taken to prevent checkmate
                if len(kings[{"White":0,"Black":1}[color]].attackedByPieces(board)[0].attackedByPieces(board)) > 0 :
                    return True
                #detects if a piece can be moved in the way to prevent checkmate
                for i in kings[{"White":0,"Black":1}[color]].attackedByPieces(board):
                    #you can't block checkmate from a knight or pawn
                    if i.type == "N" or i.type == "P":
                        return False
                    #blocking checkmate from a rook and a queen
                    elif i.type == "R" or (i.type == "Q" and (i.getPos(board)[0] == kings[{"White":0,"Black":1}[color]].getPos(board)[0] or i.getPos(board)[1] == kings[{"White":0,"Black":1}[color]].getPos(board)[1])):
                        testList = {"White": whitePieces, "Black":blackPieces}
                        for piece in testList[color]:
                            if piece.type == "K":
                                continue
                            for move in piece.validMoves(board):
                                if positionBetweenPositions(i.getPos(board), move, kings[{"White":0,"Black":1}[color]].getPos(board)) == 1:
                                    if piece.getPos(board)[0] == i.getPos(board)[0] or piece.getPos(board)[1] == i.getPos(board)[0]:
                                        return True
                    #blocking checkmate from a bishop and a queen
                    elif i.type == "B" or (i.type == "Q" and abs(i.getPos(board)[0] - kings[{"White":0,"Black":1}[color]].getPos(board)[0]) == abs(i.getPos(board)[1] - kings[{"White":0,"Black":1}[color]].getPos(board)[1])):
                        testList = {"White": whitePieces, "Black":blackPieces}
                        for piece in testList[color]:
                            if piece.type == "K":
                                continue
                            for move in piece.validMoves(board):
                                #checks if the move is somewhere in the diagonal
                                if positionBetweenPositions(i.getPos(board), move, kings[{"White":0,"Black":1}[color]].getPos(board)) == 2:
                                    #checks if the move is in the bishop/queen diagonal
                                    if abs(move[0]-i.getPos(board)[0]) == abs(move[1]-i.getPos(board)[1]):
                                        return True
            return False
        else: 
            return True
    else:
        return True
    
#returns a boolean related to wether or not a stalemate has occured for a given color
def inStalemate(board,color,boardClass,player):
    global whitePieces
    global blackPieces
    global kings
    possibleMoves = []
    #special stalemate conditions
    if len(whitePieces) + len(blackPieces) == 2:
        return True
    elif len(whitePieces) + len(blackPieces) < 5:
        allPieces = blackPieces + whitePieces
        valuablePiece = False
        Bishop = ""
        Knight = ""
        for piece in allPieces:
            if piece.type == "Q" or piece.type == "R" or piece.type == "P":
                valuablePiece = True
                break
            else:
                if len(whitePieces) + len(blackPieces) == 4:
                    if piece.type == "B":
                        if Bishop != "":
                            if Bishop.color == piece.color:
                                bishopPos = Bishop.getPos(board)
                                piecePos = piece.getPos(board)
                                if (bishopPos[0] + bishopPos[1])/2 != round((bishopPos[0] + bishopPos[1])/2) or (piecePos[0] + piecePos[1])/2 != round((piecePos[0] + piecePos[1])/2):
                                    if (bishopPos[0] + bishopPos[1])/2 == round((bishopPos[0] + bishopPos[1])/2) or (piecePos[0] + piecePos[1])/2 == round((piecePos[0] + piecePos[1])/2):
                                        valuablePiece = True
                                        break
                                    else:
                                        return True
                                else:
                                    return True
                        if Knight != "":
                            if Knight.color == piece.color:
                                valuablePiece = True
                                break
                        Bishop = piece
                    elif piece.type == "N":
                        if Bishop != "":
                            if Bishop.color == piece.color:
                                valuablePiece = True
                                break
                        Knight = piece
        if not valuablePiece:
            return True
    #normal stalemate
    if not kings[{"White":0,"Black":1}[color]].inCheck(board):
        if color == "White":
            for piece in whitePieces:
                for move in piece.validMoves(board):
                    possibleMoves.append((piece.getPos(board),move))
        if color == "Black":
            for piece in blackPieces:
                for move in piece.validMoves(board):
                    possibleMoves.append((piece.getPos(board),move))
        i = 0
        while i < len(possibleMoves):
            if board[possibleMoves[i][1][1]][possibleMoves[i][1][0]].color == color or not testMove(possibleMoves[i][0][0], possibleMoves[i][0][1], possibleMoves[i][1][0], possibleMoves[i][1][1], board, boardClass, color, player, False):
                possibleMoves.pop(i)
            else:
                i+=1
        return len(possibleMoves) == 0
    else:
        return False
    
#encodes a move to UCI before it has benn made by the board class
def encodeUCI(positions,board):
    global promoteToPiece
    lettersList = ["a","b","c","d","e","f","g","h"]
    UCIstring = ""
    #row
    UCIstring+=lettersList[positions[0][0]]
    #collumn
    UCIstring+=str(positions[0][1]+1)
    #row
    UCIstring+=lettersList[positions[1][0]]
    #collumn
    UCIstring+=str(positions[1][1]+1)
    #promotion
    if positions[1][1] == 7 and board[positions[0][1]][positions[0][0]].type:
        UCIstring+=promoteToPiece.lower()

#decodes UCI to a positions list
def decodeUCI(UCI):
    positions = [[0,0],[0,0]]
    for i in range(2):
        positions[i][1] = UCI[i*2+1]
    for i in range(2):
        positions[i][0] = ["a","b","c","d","e","f","g","h"].index(UCI[i*2])
    return positions