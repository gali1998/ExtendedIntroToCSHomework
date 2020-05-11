def concat_hor(mat1, mat2):
    new_matrix = []
    for i in range(len(mat1)):
        new_line = []
        for value1 in mat1[i]:
            new_line.append(value1)
        for value2 in mat2[i]:
            new_line.append(value2)
        new_matrix.append(new_line)
    return new_matrix

# b
def concat_vert(mat1, mat2):
    new_matrix = []
    for value1 in mat1:
        new_matrix.append(value1)
    for value2 in mat2:
        new_matrix.append(value2)
    return new_matrix

# c
def inv(mat):
    new_matrix = []
    for row in mat:
        new_line = []
        for value in row:
            new_line.append(abs(value - 1))
        new_matrix.append(new_line)
    return new_matrix

# d
def had(n):
    if n == 0:
        return [[0]]
    first_line = concat_hor(had(n-1), had(n-1))
    second_line = concat_hor(had(n-1), inv(had(n-1)))
    return concat_vert(first_line,second_line)
