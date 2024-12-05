""" Day 5: If You Give A Seed A Fertilizer

Author: Ic4r0 - https://github.com/Ic4r0

Created: 5th December 2024
"""
from collections import defaultdict, deque

# imports
from utils.parse_input import parse_by_line
from math import floor


# modules
def fix_page_order(orders: list, page: list) -> list:
    """ Topological sorting

    :param orders: orders for the given page
    :param page: unordered page
    :return: ordered page
    """
    graph = defaultdict(list)
    indegree = {node: 0 for node in page}

    for before, after in orders:
        graph[before].append(after)
        indegree[after] += 1

    queue = deque([node for node in page if indegree[node] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) != len(page):
        raise ValueError("Graph contains cycles or isolated nodes")

    return sorted_list


def part_1(orders: list, pages: list) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code

    :param orders: orders
    :param pages: pages
    :return: numeric result
    """
    valid_pages = []
    for page in pages:
        orders_involved = list(filter((lambda x: x[0] in page and x[1] in page), orders))
        valid = True
        for elem in orders_involved:
            first_page, second_page = elem
            idx_first = page.index(first_page)
            idx_second = page.index(second_page)
            if idx_second < idx_first:
                valid = False
                break
        if valid:
            valid_pages.append(page)
    middle_pages = [page[floor(len(page) / 2)] for page in valid_pages]
    return sum(middle_pages)


def part_2(orders: list, pages: list) -> int:
    """ Code for the 2nd part of the 5th day of Advent of Code

    :param orders: orders
    :param pages: pages
    :return: numeric result
    """
    invalid_pages = []
    for page in pages:
        orders_involved = list(filter((lambda x: x[0] in page and x[1] in page), orders))
        valid = True
        for elem in orders_involved:
            first_page, second_page = elem
            idx_first = page.index(first_page)
            idx_second = page.index(second_page)
            if idx_second < idx_first:
                valid = False
                break
        if not valid:
            invalid_pages.append(fix_page_order(orders_involved, page))
    middle_pages = [page[floor(len(page) / 2)] for page in invalid_pages]
    return sum(middle_pages)


def day_5(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 5th day we want to execute

    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(5, int_list=False, is_test=test)
    orders = []
    pages = []
    for line in input_list:
        if '|' in line:
            a, b = line.split('|')
            orders.append([int(a), int(b)])
        elif ',' in line:
            line_pages = line.split(',')
            pages.append([int(elem) for elem in line_pages])

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(orders, pages)
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(orders, pages)
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
