import re

def count_trees_in_path(biome):
    """
    Find the amount of trees which cross the provided path of 3 right 1 down

    :param biome: The biome. Must be made of . for empty spaces and # for trees
    """
    amount_of_trees = 0

    for row_num, row in enumerate(biome):
        if not row:
            continue

        current_position = (row_num * 3) % len(row)
        if row[current_position] == "#":
            amount_of_trees += 1

    return amount_of_trees

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")
    print(count_trees_in_path(input_data))
