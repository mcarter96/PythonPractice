# June 22
# Given a boolean matrix, update it so that if any cell is true, all the cells in that row and column are true.
# Problem source: https://www.byte-by-byte.com/zeromatrix/

def trueMatrix(matrix):
    alterMat = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    cols = [0 for i in range(len(matrix[0]))]
    rows = [0 for i in range(len(matrix))]

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 1:
                rows[x] = 1
                cols[y] = 1
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if rows[x] == 1 or cols[y] == 1:
                alterMat[x][y] = 1
    
    return alterMat



boolMat = [[1, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
boolMat2 = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
print(trueMatrix(boolMat))
print(trueMatrix(boolMat2))