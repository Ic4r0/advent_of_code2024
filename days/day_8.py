""" Day 8: Resonant Collinearity

Author: Ic4r0 - https://github.com/Ic4r0

Created: 8th December 2024
"""

# imports
from utils.parse_input import parse_by_line
from itertools import combinations


# modules
def get_antinodes(first_antenna: tuple, second_antenna: tuple, max_x_value: int, max_y_value: int) -> list:
    """ Get antinodes positions

    :param first_antenna: tuple (y,x)
    :param second_antenna: tuple (y,x)
    :param max_x_value: max index for single line
    :param max_y_value: max index for number of lines
    :return: list of antinodes
    """
    first_y, first_x = first_antenna
    second_y, second_x = second_antenna
    difference_y, difference_x = [second_antenna[idx] - first_antenna[idx] for idx in range(len(first_antenna))]
    first_antinode = (first_y - difference_y, first_x - difference_x)
    second_antinode = (second_y + difference_y, second_x + difference_x)
    total = [first_antinode, second_antinode]
    return [(y, x) for y, x in total if 0 <= y <= max_y_value and 0 <= x <= max_x_value]


def get_resonant_antinodes(first_antenna: tuple, second_antenna: tuple, max_x_value: int, max_y_value: int) -> list:
    """ Get resonant antinodes positions

    :param first_antenna: tuple (y,x)
    :param second_antenna: tuple (y,x)
    :param max_x_value: max index for single line
    :param max_y_value: max index for number of lines
    :return: list of antinodes
    """
    first_y, first_x = first_antenna
    second_y, second_x = second_antenna
    difference_y, difference_x = [second_antenna[idx] - first_antenna[idx] for idx in range(len(first_antenna))]
    total = []
    curr_first_y, curr_first_x = first_antenna
    while True:
        curr_first_y, curr_first_x = (curr_first_y - difference_y, curr_first_x - difference_x)
        if 0 <= curr_first_y <= max_y_value and 0 <= curr_first_x <= max_x_value:
            total.append((curr_first_y, curr_first_x))
        else:
            break
    curr_second_y, curr_second_x = second_antenna
    while True:
        curr_second_y, curr_second_x = (curr_second_y + difference_y, curr_second_x + difference_x)
        if 0 <= curr_second_y <= max_y_value and 0 <= curr_second_x <= max_x_value:
            total.append((curr_second_y, curr_second_x))
        else:
            break
    return total


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    antenna_positions = {}
    antinodes_positions = set()
    max_x_value = len(input_list[0]) - 1
    max_y_value = len(input_list) - 1
    for line_idx in range(len(input_list)):
        line = input_list[line_idx]
        for position_idx in range(len(line)):
            character = line[position_idx]
            if character == '.':
                continue
            position = (line_idx, position_idx)
            if character not in antenna_positions:
                antenna_positions[character] = []
            antenna_positions[character].append(position)
    for character in antenna_positions:
        char_combinations = list(combinations(antenna_positions[character], 2))
        for comb in char_combinations:
            first_antenna, second_antenna = comb
            antinodes = get_antinodes(first_antenna, second_antenna, max_x_value, max_y_value)
            for antinode in antinodes:
                antinodes_positions.add(antinode)
    return len(antinodes_positions)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    antenna_positions = {}
    antinodes_positions = set()
    max_x_value = len(input_list[0]) - 1
    max_y_value = len(input_list) - 1
    for line_idx in range(len(input_list)):
        line = input_list[line_idx]
        for position_idx in range(len(line)):
            character = line[position_idx]
            if character == '.':
                continue
            position = (line_idx, position_idx)
            if character not in antenna_positions:
                antenna_positions[character] = []
            antenna_positions[character].append(position)
    for character in antenna_positions:
        positions = antenna_positions[character]
        if len(positions) > 1:
            for pos in positions:
                antinodes_positions.add(pos)
            char_combinations = list(combinations(positions, 2))
            for comb in char_combinations:
                first_antenna, second_antenna = comb
                antinodes = get_resonant_antinodes(first_antenna, second_antenna, max_x_value, max_y_value)
                for antinode in antinodes:
                    antinodes_positions.add(antinode)
    return len(antinodes_positions)


def day_8(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 8th day we want to execute

    :param selected_part: selected Advent of Code part of the 8th day
    :param test: flag to use test input
    """

    input_list = parse_by_line(8, int_list=False, is_test=test)
    line_by_line = [list(line) for line in input_list]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(line_by_line)
        print('The result of 1st part of the 8th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(line_by_line)
        print('The result of 2nd part of the 8th day of AoC is: ' + str(result_part_2))
