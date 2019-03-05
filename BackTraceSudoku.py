#!/usr/bin/env python3
import copy

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
    print("Original Grid:")
    printGrid(grid)
    print("Final Grid")
    printGrid(backtrace(grid,0,0))
    print("Original Grid:")
    printGrid(grid2)
    print("Final Grid")
    printGrid(backtrace(grid2,0,0))
    print("Original Grid:")
    printGrid(grid3)
    print("Final Grid")
    printGrid(backtrace(grid3,0,0))

def isValid(grid, i, j, e):
    if e == 0:
        print("0 is never valid")
        return false
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

def backtrace(grid,i,j):
    #print("\nbacktrace " + str(i) + ":" + str(j))
    #printGrid(grid)
    if i == 9:
        #print("Reached end of puzzle. Solution found.")
        return grid
    elif grid[i][j] != 0 and j < 8:
        #print("Value exists: " + str(grid[i][j]), end='')
        return backtrace(grid,i,j+1)
    elif grid[i][j] != 0:
        #print("Value exists: " + str(grid[i][j]), end='')
        return backtrace(grid,i+1,0)
    #print("Testing: ", end='')
    for k in range(1,10):
        if i == 0 and j == 0:
            print(k)
        #print(str(k) + ",", end='')
        if isValid(grid,i,j,k):
            #print("*", end='')
            grid2 = copy.deepcopy(grid)
            grid2[i][j] = k
            if j < 8:
                result = backtrace(grid2,i,j+1)
            else:
                result = backtrace(grid2,i+1,0)
            if len(result):
                return result
    #print(" No solutions")
    return []

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
