def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) == len(matrix_b):
        elementToTraverse = len(matrix_a[0])
        final_mat_row = len(matrix_a)
        final_mat_col = len(matrix_b[0])
        output = [[0 for _ in range(final_mat_col)] for _ in range(final_mat_row)]
        for i in range(final_mat_row):
            for j in range(final_mat_col):
                for k in range(elementToTraverse):
                    output[i][j] = output[i][j] + (matrix_a[i][k] * matrix_b[k][j])
        return output
    else:
        return [[]]