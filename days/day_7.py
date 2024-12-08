""" Day 7: Camel Cards

Author: Ic4r0 - https://github.com/Ic4r0

Created: 7th December 2024
"""

# imports
from utils.parse_input import parse_by_line
from itertools import product


# modules
def part_1(input_dict: dict) -> int:
    """ Code for the 1st part of the 7th day of Advent of Code

    :param input_dict: input dict
    :return: numeric result
    """
    valid_rows = []
    for result in input_dict:
        result_numbers = input_dict[result]
        if sum(result_numbers) > result:
            continue
        combinations = [list(comb) for comb in product('+*', repeat=len(result_numbers) - 1)]
        is_valid = False
        for single_combination in combinations:
            current_result = result_numbers[0]
            for operation_idx in range(len(single_combination)):
                operation = single_combination[operation_idx]
                next_value = result_numbers[operation_idx + 1]
                if operation == '+':
                    current_result += next_value
                elif operation == '*':
                    current_result *= next_value
            is_valid = result == current_result
            if is_valid:
                break
        if is_valid:
            valid_rows.append(result)
    return sum(valid_rows)


def part_2(input_dict: dict) -> int:
    """ Code for the 2nd part of the 7th day of Advent of Code

    :param input_dict: input dict
    :return: numeric result
    """
    valid_rows = []
    for result in input_dict:
        result_numbers = input_dict[result]
        if sum(result_numbers) > result:
            continue
        combinations = [list(comb) for comb in product('+*|', repeat=len(result_numbers) - 1)]
        is_valid = False
        for single_combination in combinations:
            current_result = result_numbers[0]
            for operation_idx in range(len(single_combination)):
                operation = single_combination[operation_idx]
                next_value = result_numbers[operation_idx + 1]
                if operation == '+':
                    current_result += next_value
                elif operation == '*':
                    current_result *= next_value
                elif operation == '|':
                    new_value = str(current_result) + str(next_value)
                    current_result = int(new_value)
                if current_result > result:
                    break
            is_valid = result == current_result
            if is_valid:
                break
        if is_valid:
            valid_rows.append(result)
    return sum(valid_rows)


def day_7(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 7th day we want to execute

    :param selected_part: selected Advent of Code part of the 7th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(7, int_list=False, is_test=test)
    splitted = [line.split(': ') for line in input_list]
    input_dict = {int(res): [int(elem) for elem in str_list.split()] for res, str_list in splitted}

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_dict)
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_dict)
        print('The result of 2nd part of the 7th day of AoC is: ' + str(result_part_2))
