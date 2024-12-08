""" Day 6: Guard Gallivant

Author: Ic4r0 - https://github.com/Ic4r0

Created: 6th December 2024
"""

# imports
from utils.parse_input import parse_by_line

DIRECTIONS = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
NEXT_DIRECTION = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


# modules
def get_start_position(input_list: list) -> tuple:
    """ Search for start position coordinates

    :param input_list: input list
    :return: coordinates
    """
    for line_idx in range(len(input_list)):
        for step_idx in range(len(input_list[line_idx])):
            current = input_list[line_idx][step_idx]
            if current == '^':
                return line_idx, step_idx
    return 0, 0


def check_loop(input_list: list, obstacle_coords: tuple, direction: str, max_x_len: int, max_y_len: int,
               visited_coords: list) -> bool:
    """ Check for loop presence in input_list

    :param input_list: input list
    :param obstacle_coords: obstacle coordinates
    :param direction: current direction
    :param max_x_len: length of single line
    :param max_y_len: length of input list
    :param visited_coords: visited coordinates
    :return: loop present
    """
    current_direction = direction
    visited_steps = visited_coords[:]
    current_step = visited_steps[-1]
    while True:
        y, x = [DIRECTIONS[current_direction][idx] + current_step[0][idx] for idx in range(len(current_step[0]))]
        out_of_bound_y = y < 0 or y >= max_y_len
        out_of_bound_x = x < 0 or x >= max_x_len
        if out_of_bound_x or out_of_bound_y:
            break
        next_step = input_list[y][x]
        if next_step == '#' or (y, x) == obstacle_coords:
            current_direction = NEXT_DIRECTION[current_direction]
        else:
            current_step = [(y, x), current_direction]
            if current_step in visited_steps:
                return True
            visited_steps.append(current_step)
    return False


def part_1(input_list: list, start_position: tuple, max_x_len: int, max_y_len: int) -> list:
    """ Code for the 1st part of the 6th day of Advent of Code

    :param input_list: input list
    :param start_position: starting coordinates
    :param max_x_len: length of single line
    :param max_y_len: length of input list
    :return: guard path
    """
    current_direction = '^'
    visited_steps = [[start_position, current_direction]]
    current_step = visited_steps[-1]
    while True:
        y, x = [DIRECTIONS[current_direction][idx] + current_step[0][idx] for idx in range(len(current_step[0]))]
        out_of_bound_y = y < 0 or y >= max_y_len
        out_of_bound_x = x < 0 or x >= max_x_len
        if out_of_bound_x or out_of_bound_y:
            break
        next_step = input_list[y][x]
        if next_step == '#':
            current_direction = NEXT_DIRECTION[current_direction]
        else:
            current_step = [(y, x), current_direction]
            visited_steps.append(current_step)
    return visited_steps


def part_2(input_list: list, guard_path: list, start_position: tuple, max_x_len: int, max_y_len: int) -> int:
    """ Code for the 2nd part of the 6th day of Advent of Code

    :param input_list: input list
    :param guard_path: guard path
    :param start_position: starting coordinates
    :param max_x_len: length of single line
    :param max_y_len: length of input list
    :return: numeric result
    """
    obstacles_for_loops = []
    print(len(guard_path))
    for step_idx in range(len(guard_path)):
        if step_idx % 200 == 0:
            print(step_idx)
        guard_step, guard_direction = guard_path[step_idx]
        if guard_step == start_position or guard_step in obstacles_for_loops:
            continue
        visited_steps = guard_path[0: step_idx]
        has_loop = check_loop(input_list, guard_step, visited_steps[-1][1], max_x_len, max_y_len, visited_steps)
        if has_loop:
            obstacles_for_loops.append(guard_step)
    return len(obstacles_for_loops)


def day_6(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 6th day we want to execute

    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    input_list = [
        list(line) for line in parse_by_line(6, int_list=False, is_test=test)
    ]
    max_x_length = len(input_list[0])
    max_y_length = len(input_list)
    start_position = get_start_position(input_list)

    guard_path = []
    if selected_part == 1 or not selected_part:
        guard_path = part_1(input_list, start_position, max_x_length, max_y_length)
        coordinates = list(set([coords for coords, _ in guard_path]))
        result_part_1 = len(coordinates)
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list, guard_path, start_position, max_x_length, max_y_length)
        print('The result of 2nd part of the 6th day of AoC is: ' + str(result_part_2))
