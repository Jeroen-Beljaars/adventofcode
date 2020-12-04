"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?


"""

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
