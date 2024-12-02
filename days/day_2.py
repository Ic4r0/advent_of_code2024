""" Day 2: Red-Nosed Reports

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2024
"""

# imports
from utils.parse_input import parse_by_line
from math import prod


# modules
def check_safe_reports(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        level_idx = 1
        report_positive_sign = True
        valid_report = True
        while level_idx < len(report):
            previous_lvl = report[level_idx - 1]
            current_lvl = report[level_idx]
            if level_idx == 1:
                report_positive_sign = (current_lvl - previous_lvl) >= 0
            report_positive_sign_temp = (current_lvl - previous_lvl) >= 0
            difference = 1 <= abs(current_lvl - previous_lvl) <= 3
            if report_positive_sign != report_positive_sign_temp or not difference:
                valid_report = False
                break
            level_idx += 1
        if valid_report:
            safe_reports += 1
    return safe_reports


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    return check_safe_reports(input_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    safe_reports = 0
    for report in input_list:
        new_input_list = [report]
        for idx in range(len(report)):
            temp_report = report[:]
            del temp_report[idx]
            new_input_list.append(temp_report)
        safe_reports_temp = check_safe_reports(new_input_list)
        if safe_reports_temp > 0:
            safe_reports += 1
    return safe_reports


def day_2(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 2nd day we want to execute

    :param selected_part: selected Advent of Code part of the 2nd day
    :param test: flag to use test input
    """
    reports = [[int(level) for level in report.split()] for report in parse_by_line(2, int_list=False, is_test=test)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(reports)
        print('The result of 1st part of the 2nd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(reports)
        print('The result of 2nd part of the 2nd day of AoC is: ' + str(result_part_2))
