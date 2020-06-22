# June 16
# Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.
# Problem source: https://www.byte-by-byte.com/matrixproduct/

def maxSum(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    maxPath = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    minPath = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            maxValue = 1
            minValue = 1

            # Starting value
            if x == 0 and y == 0: 
                maxValue = matrix[x][y]
                minValue = matrix[x][y]
            
            if x > 0:
                tempMax = max( matrix[x][y]*maxPath[x-1][y], matrix[x][y]*minPath[x-1][y] )
                maxValue = max(tempMax, maxValue)
                tempMin = min( matrix[x][y]*maxPath[x-1][y], matrix[x][y]*minPath[x-1][y] )
                minValue = min(tempMin, minValue)

            if y > 0:
                tempMax = max( matrix[x][y]*maxPath[x][y-1], matrix[x][y]*minPath[x][y-1] )
                maxValue = max(tempMax, maxValue)
                tempMin = min( matrix[x][y]*maxPath[x][y-1], matrix[x][y]*minPath[x][y-1] )
                minValue = min(tempMin, minValue)

            maxPath[x][y] = maxValue
            minPath[x][y] = minValue

    return maxPath[-1][-1]


matrixA = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrixB = [[-1, 2, 3],
           [4, 5, -6],
           [7, 8, 9]]
matrixC = [[4, 2, 5],
            [1, 1, 1],
            [8, 2, 11]]
print(maxSum(matrixA))
print(maxSum(matrixB))
print(maxSum(matrixC))