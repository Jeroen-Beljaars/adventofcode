"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to
grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently,
nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty,
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be
valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long;
make sure you get all of it.)
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
        bag_map[bag] = []

        if "no other bags" in rule:
            continue

        bags_pattern = r"[1-9][0-9]* [a-z]+ [a-z]+"

        matches = re.findall(bags_pattern, rule)
        for match in matches:
            bag_map[bag].append(" ".join(match.split(" ")[1:]))

    return bag_map


def check_bag(possible_bags, bag_map):
    """
    Check if the possible bags for a bag may contain the target bag

    :param possible_bags:   Bags to check
    :param bag_map:         The bag map
    :return:                True if the bag may contain the target bag False if it may not
    """
    if TARGET_BAG in possible_bags:
        return True
    elif not possible_bags:
        return False

    for bag in possible_bags:
        res = check_bag(bag_map[bag], bag_map)
        if res:
            return True

    return False

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")[:-1]
    bag_count = 0

    bag_map = generate_bag_map(input_data)
    for bag in bag_map.keys():
        if check_bag(bag_map[bag], bag_map):
            bag_count += 1

    print(f"The total answer count is {bag_count}")