import copy

currentPositionCoordinate=[3,2]
validationList=[]
n = 4
mylist=["UR","DR","UL"]
def calculateLengthOfPossibleMoves( list ):
   newList = copy.copy(currentPositionCoordinate)
   addMoveToVisitedBlocksList(newList)
   for move in list:
       if(isValidMove(move)): #to check if the move is a valid knight move on chess board
           newList = copy.copy(currentPositionCoordinate)
           if checkIfBlockIsNotAlreadyVisited(newList):  #check if the block is not already been visited by a knight first
               addMoveToVisitedBlocksList(newList) #add move to visited blocks list so you can keep a record not to visit it again
   return validationList.__len__()-1 #return one less of a total is beacause starting position is also kept in validation list so we donot visit it again


def isValidMove(move):
    checkIfMoveIsValid(move)
    if checkIfMoveDoesTakeUsOutOfTheChessBoard(currentPositionCoordinate):
        return True
    else:
        return False

def checkIfMoveDoesTakeUsOutOfTheChessBoard(currentPositionCoordinate):
    return (currentPositionCoordinate[0]>0  and currentPositionCoordinate[0]<=n and currentPositionCoordinate[1]>0 and currentPositionCoordinate[1]<=n)
def checkIfMoveIsValid(move):
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
    validationList.append(move)


print (calculateLengthOfPossibleMoves(mylist))