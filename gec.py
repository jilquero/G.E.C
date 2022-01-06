from os import system, name

epsilon = 1e-7


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def sort_solutions(solutions, order):
    return [x for _, x in sorted(zip(order, solutions))]


def to_zero_solutions(solutions):
    return [0 if is_zero(num) else num for num in solutions]


def to_zero_matrix(matrix):
    return [[0 if is_zero(num) else num for num in row] for row in matrix]


def is_zero(number) -> bool:
    return True if abs(number) < epsilon else False


def get_solutions(matrix, size, order=None):
    if matrix[size - 1][size - 1] == 0:
        if matrix[size - 1][size] != 0:
            return "\nThe system has no solutions"
        else:
            return "\nThe system has an infinite number of solutions"
    solutions = reverse_procedure(matrix, size)
    if order is not None:
        solutions = sort_solutions(solutions, order)
    return print_solutions(solutions)


def reverse_procedure(matrix, size):
    solutions = [0] * size
    solutions[size - 1] = matrix[size - 1][size] / matrix[size - 1][size - 1]

    for i in range(size - 2, -1, -1):
        solutions[i] = matrix[i][size]
        for j in range(i + 1, size):
            solutions[i] -= matrix[i][j] * solutions[j]
        solutions[i] /= matrix[i][i]
    return solutions


def swap_column(matrix, order, x, y):
    order[x], order[y] = order[y], order[x]
    for row in matrix:
        row[x], row[y] = row[y], row[x]


def swap_row(matrix, x, y):
    matrix[x][:], matrix[y][:] = matrix[y][:], matrix[x][:]


def step(matrix, size, row_col):
    for i in range(row_col+1, size):
        p = matrix[i][row_col] / matrix[row_col][row_col]
        for j in range(row_col, size + 1):
            matrix[i][j] -= p * matrix[row_col][j]


def basic_gauss(matrix, size):
    for i in range(size - 1):
        if is_zero(matrix[i][i]):
            return print_message()
        step(matrix, len(matrix), i)
    return get_solutions(matrix, size)


def advanced_gauss(matrix, size):
    order = [i for i in range(size)]
    for i in range(size - 1):
        col = i
        maximum = abs(matrix[i][i])
        for j in range(i, size):
            if abs(matrix[i][j]) > maximum:
                maximum = abs(matrix[i][j])
                col = j
        if col != i:
            swap_column(matrix, order, col, i)
        if is_zero(matrix[i][i]):
            return print_message()
        step(matrix, len(matrix), i)
    return get_solutions(matrix, size, order)


def super_advanced_gauss(matrix, size):
    order = [i for i in range(size)]
    for i in range(size - 1):
        col = row = i
        maximum = abs(matrix[i][i])
        for j in range(i, size):
            for k in range(i, size):
                if abs(matrix[j][k]) > maximum:
                    maximum = abs(matrix[j][k])
                    row = j
                    col = k
        if col != i:
            swap_column(matrix, order, col, i)
        if row != i:
            swap_row(matrix, row, i)
        if is_zero(matrix[i][i]):
            return print_message()
        step(matrix, len(matrix), i)
    return get_solutions(matrix, size, order)


def print_matrix(matrix, size):
    matrix = to_zero_matrix(matrix)
    print("Matrix:")
    for row in range(size):
        for col in range(size):
            print("{:g}".format(matrix[row][col]), end="\t")
        print("{:g}".format(matrix[row][size]))


def print_equations(matrix, size):
    matrix = to_zero_matrix(matrix)
    print("Equations:")
    for row in range(size):
        for col in range(size):
            print("{:g}".format(matrix[row][col]) + "x" + str(col + 1) + " ", end="")
            if matrix[row][col + 1] >= 0 and col < size - 1:
                print("+", end="")
        print("= {:g}".format(matrix[row][size]))


def print_solutions(solutions) -> str:
    solutions = to_zero_solutions(solutions)
    result = "\nSolutions:"
    for i in range(len(solutions)):
        result += "\nx{} = {:g}".format(i + 1, solutions[i])
    return result


def print_message() -> str:
    return "\nA zero appeared as a(kk), precisely one solution of system doesnt exist"


def get_validated_input_int(min_threshold, max_threshold, message=None) -> int:
    while True:
        try:
            unvalidated_int_input = int(input(message))
            assert min_threshold <= unvalidated_int_input <= max_threshold
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between {} and {}".format(min_threshold, max_threshold))
        else:
            break
    return unvalidated_int_input


def get_validated_input_float(message=None) -> float:
    while True:
        try:
            unvalidated_float_input = float(input(message))
        except ValueError:
            print("Not a float! Please enter a float.")
        else:
            break
    return unvalidated_float_input


def load_preset_data():
    clear()
    matrix = [[[1, 2, -1, 2, 0],
               [1, 0, -2, 4, 4],
               [0, -3, 1.5, 7, 0],
               [0, -1, 1, 6, -1]], [[14, -13, 3, -16, -42, -37],
                                    [3.5, -18, 13, -23.75, -21, -5.5],
                                    [3.5, 3, -5.25, 9.25, 10.5, 12.5],
                                    [2, 14.5, -10.5, 18.5, 21, 23.5],
                                    [1.5, 6.75, -9.25, 17, -10.5, -45.25]], [[2.25, -2.5, 4, -5.25, -1],
                                                                             [-3, -7.5, 6.5, 0, 17],
                                                                             [-6.25, -12.5, 0.25, 5.25, 24.25],
                                                                             [9, 10, 7, -21, -33]]]

    print("Select equations to solve: ")
    print("\n[1]")
    print_equations(matrix[0], len(matrix[0]))
    print("\n[2]")
    print_equations(matrix[1], len(matrix[1]))
    print("\n[3]")
    print_equations(matrix[2], len(matrix[2]))

    selected_matrix = get_validated_input_int(1, 3, "Option: ")

    if selected_matrix == 1:
        return matrix[0]
    elif selected_matrix == 2:
        return matrix[1]
    elif selected_matrix == 3:
        return matrix[2]


def load_own_data():
    clear()
    size = get_validated_input_int(2, 6, "Enter number of equations (max 6): ")
    matrix = [[0 for col in range(size + 1)] for row in range(size)]
    print()
    for row in range(size):
        print("Equation " + str(row + 1) + "\n ", end="")
        for col in range(size):
            matrix[row][col] = get_validated_input_float("x{} * ".format(col + 1))
            print("+", end="") if col < size - 1 else print("    = ", end="")
        matrix[row][size] = float(input())
    return matrix


def load_data():
    clear()
    print("Select data source")
    print("[1] Preset data")
    print("[2] Own data")

    selected_input_method = get_validated_input_int(1, 2, "Option: ")

    if selected_input_method == 1:
        return load_preset_data()
    elif selected_input_method == 2:
        return load_own_data()


def select_method(matrix):
    print("\nSelect a method:")
    print("[1] Basic gauss")
    print("[2] Advanced gauss")
    print("[3] Super advanced gauss")

    selected_method = get_validated_input_int(1, 3, "Option: ")

    if selected_method == 1:
        calculate(matrix, basic_gauss, "basic gauss")
    elif selected_method == 2:
        calculate(matrix, advanced_gauss, "gauss with rows")
    elif selected_method == 3:
        calculate(matrix, super_advanced_gauss, "full gauss")


def to_stop():
    print("\nDo u want to calculate other equations:")
    print("[1] Yes")
    print("[2] No")

    to_stop_decision = get_validated_input_int(1, 2, "Option: ")

    if to_stop_decision == 1:
        return False
    elif to_stop_decision == 2:
        return True


def calculate(matrix, gauss, message):
    size = len(matrix)
    clear()
    print_equations(matrix, size)
    print("\nBefore {} elimination:".format(message))
    print_matrix(matrix, size)
    solutions = gauss(matrix, size)
    print("\nAfter {} elimination:".format(message))
    print_matrix(matrix, size)
    print(solutions)


def main():
    while True:
        matrix = load_data()
        select_method(matrix)
        if to_stop():
            break


if __name__ == "__main__":
    main()
