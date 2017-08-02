import copy
currentPositionCoordinate=[3,2]
mylist=["UR","DR","UR","DR","DR","DR","UL"]
validationList = []


def possibleMoves(moveList, start, boardDimensionality):
   global validationList
   validationList = []
   newList = list(start)
   addMoveToVisitedBlocksList(newList)
   for move in moveList:
       if(isValidMove(move, newList,boardDimensionality)): #to check if the move is a valid knight move on chess board
           if checkIfBlockIsNotAlreadyVisited(newList):  #check if the block is not already been visited by a knight first
               addMoveToVisitedBlocksList(newList) #add move to visited blocks list so you can keep a record not to visit it again
           else:
               break
   return validationList #return one less of a total is beacause starting position is also kept in validation list so we donot visit it again




def calculateLengthOfPossibleMoves(moveList, start, boardDimensionality):
    return len(possibleMoves(moveList, start, boardDimensionality))


def isValidMove(move, newList, boardDimensionality):
    checkIfMoveIsValid(move, newList)
    return checkIfMoveDoesTakeUsOutOfTheChessBoard(newList, boardDimensionality)

def checkIfMoveDoesTakeUsOutOfTheChessBoard(currentPositionCoordinate, boardDimensionality):
    return (currentPositionCoordinate[0]>0  and currentPositionCoordinate[0]<=boardDimensionality and currentPositionCoordinate[1]>0 and currentPositionCoordinate[1]<=boardDimensionality)
def checkIfMoveIsValid(move, currentPositionCoordinate):
    if (move == "UR"):
        currentPositionCoordinate[0] = currentPositionCoordinate[0] - 2
        currentPositionCoordinate[1] = currentPositionCoordinate[1] + 1
    elif (move == "UL"):
        currentPositionCoordinate[0] = currentPositionCoordinate[0] - 2
        currentPositionCoordinate[1] = currentPositionCoordinate[1] - 1
    elif (move == "DR"):
        currentPositionCoordinate[0] = currentPositionCoordinate[0] + 2
        currentPositionCoordinate[1] = currentPositionCoordinate[1] + 1
    elif (move == "DL"):
        currentPositionCoordinate[0] = currentPositionCoordinate[0] + 2
        currentPositionCoordinate[1] = currentPositionCoordinate[1] - 1
    elif (move == "RU"):
        currentPositionCoordinate[1] = currentPositionCoordinate[1] + 2
        currentPositionCoordinate[0] = currentPositionCoordinate[0] - 1
    elif (move == "RD"):
        currentPositionCoordinate[1] = currentPositionCoordinate[1] + 2
        currentPositionCoordinate[0] = currentPositionCoordinate[0] + 1
    elif (move == "LU"):
        currentPositionCoordinate[1] = currentPositionCoordinate[1] - 2
        currentPositionCoordinate[0] = currentPositionCoordinate[0] - 1
    elif (move == "LD"):
        currentPositionCoordinate[1] = currentPositionCoordinate[1] - 2
        currentPositionCoordinate[0] = currentPositionCoordinate[0] + 1


def checkIfBlockIsNotAlreadyVisited(currentPositionCoordinate):
    if currentPositionCoordinate in validationList:
        return False
    else:
        return True

def addMoveToVisitedBlocksList(move):
    validationList.append(list(move))


print (calculateLengthOfPossibleMoves(mylist, [3,2],8))
print (calculateLengthOfPossibleMoves(mylist, [3,2],8))
