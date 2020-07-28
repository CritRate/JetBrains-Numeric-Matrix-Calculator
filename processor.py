def make_matrix(counter):
    size = input(f'Enter the size of {counter} matrix:')
    x, y = [int(i) for i in size.split()]
    new_matrix = [[0.0] * y for _ in range(x)]
    print(f'Enter {counter} matrix:')
    for i in range(x):
        values = [float(i) for i in input().split()]
        for j, val in enumerate(values):
            new_matrix[i][j] = val
    return new_matrix


def sum_matrix():
    matrix_one = make_matrix('first')
    matrix_two = make_matrix('second')

    if len(matrix_one) != len(matrix_one):
        return None
    for i in range(len(matrix_two)):
        if len(matrix_one[i]) != len(matrix_two[i]):
            return None
    new_matrix = [[0] * len(matrix_one[0]) for _ in range(len(matrix_one))]
    for i, inner in enumerate(matrix_one):
        for j, val in enumerate(inner):
            new_matrix[i][j] = val + matrix_two[i][j]
    return new_matrix


def mul_matrix_by_constant():
    matrix_one = make_matrix('first')
    multi = float(input('Enter constant: '))

    new_matrix = [[0] * len(matrix_one[0]) for _ in range(len(matrix_one))]
    for i, inner in enumerate(matrix_one):
        for j, val in enumerate(inner):
            new_matrix[i][j] = val * multi
    return new_matrix


def mul_matrix_by_matrix():
    matrix_one = make_matrix('first')
    matrix_two = make_matrix('second')

    if len(matrix_one[0]) != len(matrix_two):
        return None

    new_matrix = [[0] * len(matrix_two[0]) for _ in range(len(matrix_one))]

    for i, inner_one in enumerate(matrix_one):
        for j, val_one in enumerate(inner_one):
            for k, val_two in enumerate(matrix_two[j]):
                new_matrix[i][k] += val_one * val_two

    return new_matrix


def transpose_main_diagonal(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i, inner in enumerate(matrix):
        for j, val in enumerate(inner):
            new_matrix[j][i] = val

    return new_matrix


def transpose_side_diagonal(matrix):
    new_matrix = transpose_main_diagonal(matrix)

    for x in new_matrix:
        x.reverse()

    new_matrix = transpose_horizontal_line(new_matrix)

    return new_matrix


def transpose_vertical_line(matrix):
    for x in matrix:
        x.reverse()

    return matrix


def transpose_horizontal_line(matrix):
    new_matrix = [[0] for _ in range(len(matrix[0]))]

    for i, inner in enumerate(matrix):
        if len(matrix) - 1 - i < i:
            break
        if len(matrix) - 1 - i == i:
            new_matrix[i] = matrix[i]
        new_matrix[i], new_matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]

    return new_matrix


def transpose_matrix():
    choices = [
        '1. Main diagonal\n',
        '2. Side diagonal\n',
        '3. Vertical line\n',
        '4. Horizontal line\n'
    ]
    choice = menu(choices)

    matrix_one = make_matrix('first')

    if choice == 1:
        new_matrix = transpose_main_diagonal(matrix_one)
    elif choice == 2:
        new_matrix = transpose_side_diagonal(matrix_one)
    elif choice == 3:
        new_matrix = transpose_vertical_line(matrix_one)
    else:
        new_matrix = transpose_horizontal_line(matrix_one)

    return new_matrix


def remove_lines_from_matrix(matrix, row, column):
    size = len(matrix) - 1
    new_matrix = [matrix[:-1] for _ in range(size)]

    matrix_str = ''

    # get all the numbers except from the removed row and column
    for i, inner in enumerate(matrix):
        for j, val in enumerate(inner):
            if i != row and j != column:
                matrix_str += f'{val} '

    values = [float(x) for x in matrix_str.split()]

    # add the numbers to the matrix
    for i in range(size):
        for j in range(size):
            new_matrix[i][j] = values[i * size + j]

    return new_matrix


def det_matrix(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    values = []

    for i, val in enumerate(matrix[0]):
        values.append(val * pow(-1, 2 + i) * det_matrix(remove_lines_from_matrix(matrix, 0, i)))

    return sum(values)


def determinant_matrix():
    matrix_one = make_matrix('first')

    det = det_matrix(matrix_one)

    return det


def print_matrix(matrix):
    if not matrix:
        print('ERROR')
        return
    if isinstance(m, float):
        print(matrix)
        return
    for inner in matrix:
        line = ''
        for i, val in enumerate(inner):
            if i == len(inner) - 1:
                line += f'{val:.2f}'
            else:
                line += f'{val:.2f} '
        print(line)


def menu(choices):
    menu_str = ''.join(choices)
    while True:
        print(menu_str)
        i = input('Your choice: ')
        if i in [str(i) for i in range(len(choices) + 1)]:
            return int(i)


if __name__ == '__main__':

    options = [
        '1. Add matrices\n',
        '2. Multiply matrix by a constant\n',
        '3. Multiply matrices\n',
        '4. Transpose matrix\n',
        '5. Calculate a determinant\n'
        '0. Exit'
    ]
    while True:
        option = menu(options)

        if option == 1:
            m = sum_matrix()
        elif option == 2:
            m = mul_matrix_by_constant()
        elif option == 3:
            m = mul_matrix_by_matrix()
        elif option == 4:
            m = transpose_matrix()
        elif option == 5:
            m = determinant_matrix()
        else:
            break

        print('The result is:')
        print_matrix(m)
