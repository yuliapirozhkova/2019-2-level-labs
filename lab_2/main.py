"""
Labour work #2. Levenshtein distance.
"""
from typing import List


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    matrix: List[List[int]] = []
    m_element = []
    if isinstance(num_rows, int) and isinstance(num_cols, int):
        while len(matrix) != num_rows:
            while len(m_element) != num_cols:
                m_element.append(0)
            matrix.append(m_element)
            m_element = []
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if edit_matrix:
        if edit_matrix[0]:
            if isinstance(add_weight, int) and isinstance(remove_weight, int):
                for i in range(1, len(edit_matrix)):
                    edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
                for j in range(1, len(edit_matrix[0])):
                    edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
    return list(edit_matrix)


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if edit_matrix and edit_matrix[0]:
        if isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(
                substitute_weight, int) and isinstance(original_word, str) and isinstance(target_word, str):
            for i in range(1, len(edit_matrix)):
                for j in range(1, len(edit_matrix[0])):
                    edit_matrix[i][j] = minimum_value((edit_matrix[i - 1][j] + remove_weight,
                                                       edit_matrix[i][j - 1] + add_weight,
                                                       edit_matrix[i - 1][j - 1] + (
                                                           substitute_weight if original_word[i - 1] != target_word[
                                                               j - 1]
                                                           else 0)))
    return list(edit_matrix)


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if isinstance(original_word, str) and isinstance(target_word, str) and isinstance(add_weight, int) and isinstance(
            remove_weight, int) and isinstance(substitute_weight, int):
        num_rows = len(original_word) + 1
        num_cols = len(target_word) + 1
        matrix = fill_edit_matrix(tuple(initialize_edit_matrix(tuple(generate_edit_matrix(num_rows, num_cols)),
                                                               add_weight, remove_weight)), add_weight, remove_weight,
                                  substitute_weight, original_word, target_word)
        distance = matrix[-1][-1]
    else:
        distance = -1
    return distance


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    file_csv = open(path_to_file, 'w')
    dop = ''
    for row in edit_matrix:
        for element in row:
            dop = str(element) + ','
            file_csv.write(dop)
        file_csv.write('\n')
        dop = ''
    file_csv.close()


def load_from_csv(path_to_file: str) -> list:
    file_csv = open(path_to_file)
    matrix = []
    row = []
    for line in file_csv:
        for element in line:
            if element.isdigit():
                row.append(int(element))
        matrix.append(row)
        row = []
    file_csv.close()
    return matrix
