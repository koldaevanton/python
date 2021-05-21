class Matrix:
    matrix_data: []

    def __init__(self, matrix):
        self.matrix_data = matrix

    def __str__(self):
        result = []
        for line in self.matrix_data:
            s_line = '\t'.join([str(i) for i in line])
            result.append(s_line)
        return "\n".join(result)

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix_data) != len(other.matrix_data):
            raise ArithmeticError("Matrices are not same size")
        for line_number in range(len(self.matrix_data)):
            self_line = self.matrix_data[line_number]
            other_line = other.matrix_data[line_number]
            if len(self_line) != len(other_line):
                raise ArithmeticError("Matrices are not same size")
            new_matrix_line = []
            for value_num in range(len(self_line)):
                new_matrix_line.append(self_line[value_num] + other_line[value_num])
            new_matrix.append(new_matrix_line)
        return Matrix(new_matrix)


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[6, 5], [4, 3], [2, 1]])
matrix3 = Matrix([[10, 11], [12, 13], [14, 15]])
print(matrix1)
print(matrix1 + matrix3)
print(matrix1 + matrix2 + matrix3)
