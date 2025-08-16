def submatrix_swap(matrix, coord_S1, coord_S2):

    start_rowA, end_rowA , start_colA , end_colA = coord_S1
    start_rowB , end_rowB, start_colB, end_colB = coord_S2
    sub_matrix_A = [row[start_colA:end_colA] for row in matrix[start_rowA:end_rowA]]
    sub_matrix_B = [row[start_colB:end_colB] for row in matrix[start_rowB:end_rowB]]
    
    for i in range(start_rowA, end_rowA):
        for j in range(start_colA, end_colA):
            matrix[i][j] = sub_matrix_B[i - start_rowA][j - start_colA]
    for i in range(start_rowB, end_rowB):
        for j in range(start_colB, end_colB):
            matrix[i][j] = sub_matrix_A[i - start_rowB][j - start_colB]
    return matrix
    
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
coord_S1 = [0, 2, 0, 2]
coord_S2 = [3, 5, 0, 2]
          
print(submatrix_swap(matrix, coord_S1, coord_S2))