#!/usr/bin/env python3

def sudoku(grid):
    print("Original Grid:")
    printGrid(grid)
    cond = False
    while (not cond):
        #printGrid(grid)
        grid = scan(grid)
        cond = True
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    cond = False
    print("Final Grid:")
    printGrid(grid)

# grid is board, i is row (0-8), j is column (0-8), e is number considering (1-9)
def isValid(grid, i, j, e):
    for k in range(8):
        if k < i:
            if grid[k][j] == e:
                return False
        else:
            if grid[k+1][j] == e:
                return False
    for k in range(8):
        if k < j:
            if grid[i][k] == e:
                return False
        else:
            if grid[i][k+1] == e:
                return False
    for k in range((i//3)*3, (i//3)*3+3):
        for l in range((j//3)*3, (j//3)*3+3):
            if grid[k][l] == e:
                return False
    return True

def scan(grid):
    for i in range(9):
        grid = checkRow(grid, i)
        grid = checkColumn(grid, i)
        grid = checkSector(grid, i)
        for j in range(9):
            if grid[i][j] == 0:
                numValids = 0
                valids = []
                for k in range(1, 10):
                    if isValid(grid, i, j, k):
                        numValids += 1
                        valids.append(k)
                if numValids == 1:
                    #print(str(valids[0]) + " inserted at (" + str(i) + "," + str(j) + ") by scan")
                    grid[i][j] = valids[0]
    return grid

def checkRow(grid, i):
    values = [1,2,3,4,5,6,7,8,9]
    for j in range(9):
        values = list(filter(lambda a: a != grid[i][j], values))
    for k in range(len(values)):
        indicies = []
        for j in range(9):
            if grid[i][j] == 0 and isValid(grid, i, j, values[k]):
                indicies.append(j)
        if len(indicies) == 1:
            #print(str(values[k]) + " inserted at (" + str(i) + "," + str(indicies[0]) + ") by checkRow")
            grid[i][indicies[0]] = values[k]
    return grid

def checkColumn(grid, j):
    values = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        values = list(filter(lambda a: a != grid[i][j], values))
    for k in range(len(values)):
        indicies = []
        for i in range(9):
            if grid[i][j] == 0 and isValid(grid, i, j, values[k]):
                indicies.append(i)
        if len(indicies) == 1:
            #print(str(values[k]) + " inserted at (" + str(indicies[0]) + "," + str(j) + ") by checkColumn")
            grid[indicies[0]][j] = values[k]
    return grid

def checkSector(grid, k):
    values = [1,2,3,4,5,6,7,8,9]
    i = 3 * (k // 3)
    j = 3 * (k % 3)
    for l in range(3):
        for m in range(3):
            values = list(filter(lambda a:a != grid[i+l][j+m], values))
    for n in range(len(values)):
        indicies = []
        for l in range(3):
            for m in range(3):
                if grid[i+l][j+m] == 0 and isValid(grid,i+l,j+m,values[n]):
                    indicies.append(i+l)
                    indicies.append(j+m)
        if len(indicies) == 2:
            #print(str(values[n]) + " inserted at (" + str(indicies[0]) + "," + str(indicies[1]) + ") by checkSector")
            grid[indicies[0]][indicies[1]] = values[n]
    return grid

def main():
    grid = [[1,6,0,0,0,3,0,0,9],
            [8,0,0,0,5,0,2,6,0],
            [0,0,0,0,6,7,0,8,0],
            [0,0,8,0,0,9,0,5,4],
            [5,0,0,6,0,8,7,0,0],
            [6,0,9,0,0,0,0,1,0],
            [0,0,0,0,1,4,9,7,0],
            [4,0,5,0,7,6,8,0,1],
            [7,0,6,0,0,0,0,3,5]]
    grid2 = [[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,7],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]
    grid3 = [[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,3,0,8,5],
             [0,0,1,0,2,0,0,0,0],
             [0,0,0,5,0,7,0,0,0],
             [0,0,4,0,0,0,1,0,0],
             [0,9,0,0,0,0,0,0,0],
             [5,0,0,0,0,0,0,7,3],
             [0,0,2,0,1,0,0,0,0],
             [0,0,0,0,4,0,0,0,9]]
    sudoku(grid)
    sudoku(grid2)
    sudoku(grid3)

def printGrid(grid):
    string = "+-------+-------+-------+\n"
    for i in range(3): # For each group of three rows
        for j in range(3): # For each line in those groups
            for k in range(3): # For each group of three numbers in those lines
                string += "| "
                string += str(grid[3*i+j][3*k]) + " "
                string += str(grid[3*i+j][3*k+1]) + " "
                string += str(grid[3*i+j][3*k+2]) + " "
            string += "|\n"
        string += "+-------+-------+-------+\n"
    print(string)
    
main()
