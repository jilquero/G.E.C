def print_matrix(matrix, solutions_order=None):
    size = len(matrix)
    if solutions_order is None:
        solutions_order = [i for i in range(size)]

    for row in range(size):
        for col in solutions_order:
            print(matrix[row][col], end="\t")
        print(matrix[row][size])


def print_equations(matrix, solutions_order=None):
    size = len(matrix)
    if solutions_order is None:
        solutions_order = [i for i in range(size)]

    for row in range(size):
        for col in range(size):
            print(str(matrix[row][col]) + "x" + str(solutions_order[col] + 1) + " ", end="")
            if matrix[row][col + 1] >= 0 and col < size - 1:
                print("+", end="")
        print("=", matrix[row][size])


def get_validated_input(message, min_threshold, max_threshold):
    while True:
        try:
            unvalidated_input = int(input(message))
            assert min_threshold <= unvalidated_input <= max_threshold
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between {} and {}".format(min_threshold, max_threshold))
        else:
            break
    return unvalidated_input


def load_preset_data():
    matrix = [[[1, 2, -1, 2, 0],
               [1, -2, 4, 4, 4],
               [0, -3, 1.5, 7, 0],
               [0, -1, 1, 6, -1]], [[14, -13, 3, -16, -42, -37],
                                    [3.5, -18, 13, -23.75, -21, -5.5],
                                    [3.5, 3, -5.25, 9.25, 10.5, 12.5],
                                    [2, 14.5, -10.5, 18.5, 21, 23.5],
                                    [1.5, 6.75, -9.25, 17, 10.5, -45.25]]]

    print("Select equations to solve: ")
    print("\n[1]")
    print_equations(matrix[0])
    print("\n[2]")
    print_equations(matrix[1])

    selected_matrix = get_validated_input("Option: ", 1, 2)

    if selected_matrix == 1:
        return matrix[0]
    elif selected_matrix == 2:
        return matrix[1]


def load_own_data():
    pass


def load_data():
    print("Select data source")
    print("[1] Preset data")
    print("[2] Own data")

    selected_input_method = get_validated_input("Option: ", 1, 2)

    if selected_input_method == 1:
        return load_preset_data()
    elif selected_input_method == 2:
        return load_own_data()


def to_stop():
    print("Do u want to calculate other equations:")
    print("[1] Yes")
    print("[2] No")

    to_stop_decision = get_validated_input("Option: ", 1, 2)

    if to_stop_decision == 1:
        return False
    elif to_stop_decision == 2:
        return True


def main():
    while True:
        matrix = load_data()
        if to_stop():
            break


if __name__ == "__main__":
    main()
