def travel_matrix(matrix, n):
    directions = {
        "up": 0,
        "down": 1,
        "right": 1,
        "left": 0,
    }
    dir = "right"
    result = []
    rows = cols = len(matrix)
    row = col = layers = 0
    for _ in range(rows * cols):
        #rint(f'fila: {row}| columna {col} |total_columnas: {cols-directions[dir]}')
        if layers < n:
            result.append(matrix[row][col])
            match dir:
                case "right":
                    if col == cols - directions[dir]:
                        directions["up"] += 1
                        dir = "down"
                        row += 1
                    else:
                        col += 1
                case "down":
                    if row == rows - directions[dir]:
                        directions["right"] += 1
                        dir = "left"
                        col -= 1
                    else:
                        row += 1
                case "left":
                    if col == 0 + directions[dir]:
                        directions["down"] += 1
                        dir = "up"
                        row -= 1
                    else:
                        col -= 1
                case "up":
                    if row == 0 + directions[dir]:
                        directions["left"] += 1
                        layers += 1
                        dir = "right"
                        col += 1
                    else:
                        row -= 1
    return result 


def solution(matrix_A, matrix_B, n):
    result = travel_matrix(matrix_A, n) + travel_matrix(matrix_B, n)
    return result
matrix_A = [[1]]
matrix_B = [[-1]]
n = 1
print(solution(matrix_A, matrix_B, 1))