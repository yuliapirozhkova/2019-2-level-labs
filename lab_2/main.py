"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if isinstance(num_rows, int) and isinstance(num_cols, int):
        number = 0
        f_matrix = []
        for _ in range(num_rows):
            for_count = []
            for _ in range(num_cols):
                for_count.append(number)
            f_matrix.append(for_count)
        return f_matrix
    return []


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    matrix = list(edit_matrix)
    if matrix and isinstance(add_weight, int) and isinstance(remove_weight, int):
        length = len(matrix[0])
        if length:
            for i in range(1, len(matrix)):
                matrix[i][0] = matrix[i - 1][0] + remove_weight
            for j in range(1, len(matrix[0])):
                matrix[0][j] = matrix[0][j - 1] + add_weight
    return list(matrix)


def minimum_value(numbers: tuple) -> int:
    value = min(numbers)
    return value


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    matrix1 = list(edit_matrix)
    if matrix1:
        if isinstance(add_weight, int) and isinstance(remove_weight, int) \
            and isinstance(substitute_weight, int) \
                and isinstance(original_word, str) and isinstance(target_word, str):
            for i in range(1, len(matrix1)):
                for j in range(1, len(matrix1[i])):
                    for_add = matrix1[i][j - 1] + add_weight
                    for_remove = matrix1[i - 1][j] + remove_weight
                    if original_word[i - 1] == target_word[j - 1]:
                        for_sub = matrix1[i - 1][j - 1]
                    else:
                        for_sub = matrix1[i - 1][j - 1] + substitute_weight
                    matrix1[i][j] = minimum_value((for_add, for_remove, for_sub))

    print(matrix1)
    return list(matrix1)


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if isinstance(original_word, str) and isinstance(target_word, str) and isinstance(add_weight, int)\
            and isinstance(remove_weight, int) and isinstance(substitute_weight, int):
        return \
            fill_edit_matrix(
                tuple(initialize_edit_matrix(tuple(generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)),
                                             add_weight,
                                             remove_weight)),
                add_weight,
                remove_weight,
                substitute_weight,
                original_word,
                target_word)[-1][-1]
    return -1


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    with open(path_to_file, 'w') as file:
        for row in edit_matrix:
            line = ''
            for i in row:
                line += str(i)
                line += ','
            file.write(line[:-1] + '\n')


def load_from_csv(path_to_file: str) -> list:
    if isinstance(path_to_file, str):
        with open(path_to_file) as file:
            first_matrix = []
            var = file.read().split('\n')[:-1]
            for row in var:
                first_matrix.append(row.split(','))
        return first_matrix
