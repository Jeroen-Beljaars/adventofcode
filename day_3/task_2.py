import re


def count_trees_in_path(biome, path_instructions):
    """
    Find the amount of trees which cross the provided path of 3 right 1 down

    :param biome:               The biome. Must be made of . for empty spaces and # for trees
    :param path_instructions:   Instructions on what path to take. First index must be the amount of positions to the
                                right per step. Second index must be the amount of positions down per step.
    """
    amount_of_trees = 0
    positions_to_right = path_instructions[0]
    positions_down = path_instructions[1]

    for row_num, row in enumerate(biome[::positions_down]):
        if not row:
            continue

        current_position = (row_num * positions_to_right) % len(row)
        if row[current_position] == "#":
            amount_of_trees += 1

    return amount_of_trees


if __name__ == '__main__':
    multiplied_trees = 1
    input_data = open("input.txt", "r").read().split("\n")

    # Path to take
    # index 1: amount of positions to the right per step
    # index 2: amount of rows down per step
    path_instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for instruction in path_instructions:
        multiplied_trees *= count_trees_in_path(input_data, instruction)

    print(multiplied_trees)
