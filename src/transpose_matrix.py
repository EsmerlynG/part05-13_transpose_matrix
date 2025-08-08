def print_matrix(matrix: list):
    for r in matrix:
        for num in r:
            print(f"{num} ", end="")
        print()

def transpose(matrix: list):
    matrix_length = len(matrix)

    for row in range(matrix_length):
        for column in range(row, matrix_length):
            number = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = number



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(matrix)
    transpose(matrix)
    print()
    print_matrix(matrix)