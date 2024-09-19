import time
import copy


def printGrid(grid, rows, column):
    convertDictToGrid(readDict(grid_dict, rows, column), rows, column)
    with open("grid.txt", "r") as gridfile:
        grid = gridfile.read()
        print(grid)


def convertDictToGrid(dict, rows, columns):
    open('grid.txt', 'w').close()
    for i in range(rows):
        for j in range(columns):
            with open("grid.txt", "a+") as gridfile:
                if j != columns - 1:
                    cell = dict[i, j] + " "
                    gridfile.write(cell)
                else:
                    gridfile.write("%s\n" % dict[i, j])


def readDict(dict, rows, columns):
    newDict = {}
    for i in range(rows):
        for j in range(columns):
            if dict[i, j] == 0:
                newDict[i, j] = "-"
            elif dict[i, j] == 1:
                newDict[i, j] = "o"
            else:
                newDict[i, j] = "x"
    return newDict


def createBlankGrid(rows, column):
    coordinate_dict = {}
    for i in range(rows):
        for j in range(column):
            coordinate_dict[i, j] = 0

    return (coordinate_dict)


def neighborfinder(cell, grid, rows, columns):
    verti = cell[0]
    horiz = cell[1]
    neighbors = {}

    for i in range(verti - 1, verti + 2):
        for j in range(horiz - 1, horiz + 2):
            if i < 0 or j < 0 or i > rows - 1 or j > columns - 1:
                continue
            elif i == verti and j == horiz:
                continue
            else:
                neighbors[i, j] = grid[i, j]

    return neighbors


def advanceByGeneration(grid, row, column, player):
    grid2 = copy.deepcopy(grid)
    for cells in grid2:
        grid2 = ruleCheckCell(cells, grid2, neighborfinder(cells, grid, row, column), player)

    return (copy.deepcopy(grid2))


def ruleCheckCell(cell, grid, neighborsDict, player):
    player1Count = 0
    player2Count = 0
    trueCount = 0
    falseCount = 0

    for cells in neighborsDict:
        if grid[cell] == 1:
            if neighborsDict[cells] == 1:
                player1Count += 1
                trueCount += 1
            elif neighborsDict[cells] == 2:
                falseCount += 1
            else:
                falseCount += 1
        elif grid[cell] == 2:
            if neighborsDict[cells] == 1:
                falseCount += 1
            elif neighborsDict[cells] == 2:
                player2Count += 1
                trueCount += 1
            else:
                falseCount += 1
        else:
            if neighborsDict[cells] == 1:
                player1Count += 1
                trueCount += 1
            elif neighborsDict[cells] == 2:
                player2Count += 1
                trueCount += 1
            else:
                falseCount += 1

    if (grid[cell] == 1 or grid[cell] == 2) and trueCount <= 1:
        grid[cell] = 0
    elif (grid[cell] == 1 or grid[cell] == 2) and (trueCount == 2 or trueCount == 3):
        pass
    elif (grid[cell] == 1 or grid[cell] == 2) and trueCount >= 4:
        grid[cell] = 0
    elif grid[cell] == 0 and trueCount == 3:
        if player1Count > player2Count:
            grid[cell] = 1
        else:
            grid[cell] = 2

    return grid


def turn(grid, player, rows, columns):
    player_name = ""
    if player == 1:
        player_name = "Player1 "
    else:
        player_name = "Player2 "

    print("Destroy\n")
    is_valid = False
    while is_valid == False:

        destrow = int(input(player_name + "Row: "))
        destcolumn = int(input(player_name + "Column: "))

        if destrow < 0 or destcolumn < 0 or destrow > rows - 1 or destcolumn > columns - 1 or grid[
            destrow, destcolumn] == 0:
            is_valid = False
        else:
            is_valid = True
            grid[destrow, destcolumn] = 0

    print("\nAdd\n")
    is_valid = False
    while is_valid == False:
        addrow = int(input(player_name + "Row: "))
        addcol = int(input(player_name + "Column: "))
        if player == 1:
            if addrow < 0 or addcol < 0 or addrow > rows - 1 or addcol > columns - 1 or grid[addrow, addcol] == 2:
                is_valid = False
            else:
                is_valid = True
        else:
            if addrow < 0 or addcol < 0 or addrow > rows - 1 or addcol > columns - 1 or grid[addrow, addcol] == 1:
                is_valid = False
            else:
                is_valid = True

    grid[addrow, addcol] = player
    return grid


def end(grid, player, row, col):
    p1count = 0
    p2count = 0
    for cells in grid:
        if cells == (row - 1, col - 1):
            if p1count == 0:
                print("Player 2 wins")
            elif p2count == 0:
                print("Player 1 wins")
            return True
        if (grid[cells] == 1 or grid[cells] == 2):
            if grid[cells] == 1:
                p1count += 1
            else:
                p2count += 1

            return False


def getValues(str):
    str = str[1:-1]
    coords = str.split(",")
    return int(coords[0]), int(coords[1])


def patternloader(patterntxt, blankgrid, row, column):
    if row % 2 == 0:
        rowcenter = row // 2
    else:
        rowcenter = round(row)

    if column % 2 == 0:
        columncenter = column // 2
    else:
        columncenter = round(column)

    player1center = columncenter // 2
    player2center = columncenter + player1center

    coordlist = []

    with open(patterntxt, "r") as pattern:
        for lines in pattern.readlines():
            lines = lines.strip()
            coordlist.append(lines)

    print(coordlist)

    for coordinate in coordlist:
        xval, yval = getValues(coordinate)
        blankgrid[xval + rowcenter, yval + player1center] = 1
        blankgrid[xval + rowcenter, -yval + player2center] = 2


rows = 30
columns = 60
grid_dict = createBlankGrid(rows, columns)
patternloader("TestPattern.txt", grid_dict, rows, columns)
go = input("Enter: ")

if go == "" or go == " ":
    print("")
    # grid_dict[16, 17] = 1; grid_dict[17, 18] = 1; grid_dict[18, 17] = 1; grid_dict[17, 16] = 1; grid_dict[16, 16] = 1; grid_dict[16, 18] = 1; grid_dict[18, 16] = 1; grid_dict[18, 18] = 1;

isEnded = False
player = 1
while isEnded == False:
    printGrid(grid_dict, rows, columns)
    grid_dict = turn(grid_dict, player, 30, 60)
    printGrid(grid_dict, rows, columns)
    grid_dict = advanceByGeneration(grid_dict, rows, columns, player)
    isEnded = end(grid_dict, player, rows, columns)
    time.sleep(0.2)
    if player == 1:
        player = 2
    else:
        player = 1

# Opponents cells are kept as false, so they dont affect anything