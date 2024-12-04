""" Day 4: Ceres Search

Author: Ic4r0 - https://github.com/Ic4r0

Created: 4th December 2024
"""

# imports
from utils.parse_input import parse_by_line
from re import findall


# modules
def extract_backwards(input_list: list) -> list:
    """ Code needed to extract backward strings from a list of strings

    :param input_list: input list
    :return: backward strings
    """
    return [line[::-1] for line in input_list]


def extract_diagonals(matrix: list, min_length: int = 4) -> list:
    """ Code needed to extract diagonal strings from a list of strings

    :param matrix: input list
    :param min_length: output string min length
    :return: list of diagonals
    """
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals = []

    # Diagonals from top-left to bottom-right (↘)
    for diagonal in range(-(rows - 1), cols):
        string = ''
        for i in range(rows):
            j = diagonal + i
            if 0 <= j < cols:
                string += matrix[i][j]
        if len(string) >= min_length:
            diagonals.append(string)

    # Diagonals from top-right to bottom-left (↙)
    for diagonal in range(0, rows + cols - 1):
        string = ''
        for i in range(rows):
            j = diagonal - i
            if 0 <= j < cols:
                string += matrix[i][j]
        if len(string) >= min_length:
            diagonals.append(string)

    return diagonals


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    xmas_counter = 0
    rows_to_be_checked = input_list[:]  # horizontal lines
    rows_to_be_checked.extend(extract_backwards(input_list))  # horizontal backward lines
    vertical = [''.join(row[idx] for row in input_list) for idx in range(len(input_list[0]))]
    rows_to_be_checked.extend(vertical)  # vertical lines
    rows_to_be_checked.extend(extract_backwards(vertical))  # vertical backward lines
    diagonals = extract_diagonals(input_list)
    rows_to_be_checked.extend(diagonals)  # diagonal lines
    rows_to_be_checked.extend(extract_backwards(diagonals))  # diagonal backward lines
    pattern = r"XMAS"
    for row in rows_to_be_checked:
        matches = findall(pattern, row)
        xmas_counter += len(matches)
    return xmas_counter


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    x_mas_counter = 0
    for row_idx in range(1, len(input_list) - 1):
        row = input_list[row_idx]
        for char_idx in range(1, len(row) - 1):
            if row[char_idx] == 'A':
                row_before = input_list[row_idx - 1]
                row_after = input_list[row_idx + 1]
                char_l_u = row_before[char_idx - 1]
                char_l_d = row_after[char_idx - 1]
                char_r_u = row_before[char_idx + 1]
                char_r_d = row_after[char_idx + 1]
                hor_check = char_l_u == char_l_d and char_r_u == char_r_d
                ver_check = char_l_u == char_r_u and char_l_d == char_r_d
                hor = hor_check and char_l_u == 'M' and char_r_u == 'S'
                hor_bw = hor_check and char_l_u == 'S' and char_r_u == 'M'
                ver = ver_check and char_l_u == 'M' and char_l_d == 'S'
                ver_bw = ver_check and char_l_u == 'S' and char_l_d == 'M'
                if hor or hor_bw or ver or ver_bw:
                    x_mas_counter += 1
    return x_mas_counter


def day_4(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 4th day we want to execute

    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(4, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
