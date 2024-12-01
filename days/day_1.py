""" Day 1: Historian Hysteria

Author: Ic4r0 - https://github.com/Ic4r0

Created: 1st December 2024
"""

# imports
from utils.parse_input import parse_by_line
from collections import Counter


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    separated_numbers = [line.split() for line in input_list]
    sorted_first = [int(line[0]) for line in separated_numbers]
    sorted_second = [int(line[1]) for line in separated_numbers]
    sorted_first.sort()
    sorted_second.sort()
    distances = [abs(sorted_second[idx] - sorted_first[idx]) for idx in range(len(input_list))]
    return sum(distances)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    separated_numbers = [line.split() for line in input_list]
    first = [int(line[0]) for line in separated_numbers]
    second = [line[1] for line in separated_numbers]
    count = Counter(second)
    similarity_score = [num * count.get(str(num), 0) for num in first]
    return sum(similarity_score)


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    input_list = parse_by_line(1, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
