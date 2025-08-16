def slice_matrix(matrix_A, matrix_B, submatrix_coords):
    start_row_A, end_row_A, start_col_A, end_col_A = submatrix_coords[0]
    start_row_B, end_row_B, start_col_B, end_col_B = submatrix_coords[1]
    submatrix_A = [row[start_col_A - 1:end_col_A] for row in matrix_A[start_row_A - 1: end_row_A]]
    submatrix_B = [row[start_col_B - 1:end_col_B] for row in matrix_B[start_row_B - 1: end_row_B]]
    
    result_matrix = [[0 for _ in range(len(submatrix_A[0]) * 2)] for _ in range(len(submatrix_A))]
    for i in range(len(submatrix_A)):
        for j in range(len(submatrix_A[0])):
            result_matrix[i][2 * j] = submatrix_A[i][j]
            result_matrix[i][2 * j + 1] = submatrix_B[i][j]
    
    return result_matrix

a, b, c = (
            [[89, -34, 23], 
            [1, -3, 0]], 

            [[-12, -8, 2], 
            [7, -6, 10]], 

            [(2, 2, 1, 3), 
            (1, 1, 1, 3)]
        )
print(slice_matrix(a, b, c))