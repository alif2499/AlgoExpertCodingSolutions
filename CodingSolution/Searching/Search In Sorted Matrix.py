def searchInSortedMatrix(matrix, target):
    return searching(matrix, target, 0, len(matrix[0])-1)

def searching(matrix, target, row, col):
    while (row<len(matrix) and col>=0):
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
    
    return [-1, -1]