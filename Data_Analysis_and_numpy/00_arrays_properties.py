import numpy as np

print('####### Array Operations and functions over matrixes ########')
print('#############################################################')

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 3, 6, 8, 1], dtype=int)
print(f'Array a: {a}   ||   Array b: {b}')
#  We can add same lenght matrixes only using the + operator
print(f'Sum of arrays using "a + b": {a + b}')
print(f'Substraction of arrays using "a - b": {a - b}')
print(f'Multiplication  of arrays using "a * b": {a * b}')
print(f'Logic functions "a < 3": {a<3}')
help1 = np.array( [[1,1],[2,1]] )
help2 = np.array( [[2,4],[3,4]] )
print(f'multiplication of 2x2 arays:\n {help1 * help2}')
#  Also we can sum all the matrix values without using for loop
total_sum_a = a.sum()
print(f'Sum of all the values of "a" array using a.sum(): {total_sum_a}')
#  In the case, we have an multidimensional array, we have to specify the axis
c = np.array([[1, 10, 3],[4, 5, 20]])
sum_ax0_c = c.sum(axis=0)
sum_ax1_c = c.sum(axis=1)
max_value1, max_value2 = c.max(axis=0), c.max(axis=1)
min_value1, min_value2 = c.min(axis=0), c.min(axis=1)
print(f'New array c: \n{c}')
print(f'Sum over axis=0 (column sums): {sum_ax0_c}, Max: {max_value1}, Min: {min_value1}')
print(f'Sum over axis=1 (row sums):    {sum_ax1_c}, Max: {max_value2}, Min: {min_value2}\n\n')
#  Yes, you can use trigonometical functions and divitions. 
print(f'Trigonometrical funcion np.sin(c): {np.sin(c)}\n')

print('################### Modifying rows ##########################')
print('#############################################################')

'''
Using functions over a row or column 
'''
arr = np.arange(1, 10).reshape(3, 3)
print(f'Array previous applying a function: \n{arr}')
print(f'\nDoing sum function over the row: {np.apply_along_axis(sum, axis=0, arr=arr)}\n\n') # axis = 1 is for a funcion applied vertically


print('#################### Dot Product ############################')
print('#############################################################')
'''
Dot Product

It's the formal way to multiply 2 matrixes it's the lineal combination bewtween values.
'''
def dot_multiplication(array1, array2):
    m, n = array1.shape
    n2, p = array2.shape
    if n != n2:
        raise ValueError("Columns of array1 has to be same as rows in array2")
    final_matrix = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
            for k in range(n):
                final_matrix[i][j] += array1[i][k] * array2[k][j]
    return final_matrix

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print(f'Dot multiplication using dot_multiplication:\n {dot_multiplication(A, B)}\n Dot multiplication using A@B and A.dot(B):\n {A@B}\n {A.dot(B)}')