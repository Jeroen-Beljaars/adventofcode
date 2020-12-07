"""
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of
bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example;
be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.
"""
import re
from string import ascii_lowercase

TARGET_BAG = "shiny gold"


def generate_bag_map(rules):
    """
    Generate a dictionary containing the different bags, and which bags these bags may contain

    :param rules:   The rule string for a specific bag
    :return:        The bag map
    """
    bag_map = {}
    for rule in rules:
        bag = rule.split(" bags ")[0]
        bag_map[bag] = {}

        if "no other bags" in rule:
            continue

        bags_pattern = r"[1-9][0-9]* [a-z]+ [a-z]+"

        matches = re.findall(bags_pattern, rule)
        for match in matches:
            match_split = match.split(" ")
            bag_map[bag][" ".join(match_split[1:])] = int(match_split[0])

    return bag_map


def count_bags(possible_bags, bag_map):
    """
    Check if the possible bags for a bag may contain the target bag

    :param possible_bags:   Bags to check
    :param bag_map:         The bag map
    :return:                Amount of bags in a given bag (including the bag itself)
    """
    # Assing 1 to bag count since we currently are in a bag
    bag_count = 1

    # Loop over all the possible bags
    for bag, amount in possible_bags.items():
        bag_count += amount * count_bags(bag_map[bag], bag_map)

    return bag_count

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")[:-1]
    bag_map = generate_bag_map(input_data)

    possible_bags = bag_map[TARGET_BAG]
    bag_count = count_bags(possible_bags, bag_map)

    # Subtract 1 from the resulting bag count to exclude the outer bag
    bag_count -= 1

    print(f"The total bag count is {bag_count}")