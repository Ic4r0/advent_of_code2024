""" Day 3: Mull It Over

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd December 2024
"""

# imports
from utils.parse_input import parse_by_line
from re import findall


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    multiplications = []
    for line in input_list:
        pattern = r"mul\((\d+),(\d+)\)"
        records = findall(pattern, line)
        multiplications.extend(int(a) * int(b) for a, b in records)
    return sum(multiplications)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    multiplications = []
    do = True
    for line in input_list:
        pattern = r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
        records = findall(pattern, line)
        for match in records:
            if match[2] and match[2] == 'don\'t()':
                do = False
            elif match[3] and match[3] == 'do()':
                do = True
            elif match[0] and do:
                multiplications.append(int(match[0]) * int(match[1]))
    return sum(multiplications)


def day_3(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 3rd day we want to execute

    :param selected_part: selected Advent of Code part of the 3rd day
    :param test: flag to use test input
    """
    instructions = parse_by_line(3, int_list=False, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(instructions)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(instructions)
        print('The result of 2nd part of the 3rd day of AoC is: ' + str(result_part_2))
