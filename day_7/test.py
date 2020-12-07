import re


def import_input(file):
    with open(file) as f:
        inputs = f.readlines()
        return [str(x).replace('\n', "") for x in inputs]


def import_input_7():
    raw_data = import_input("input.txt")
    bag_rules = {}
    for line in raw_data:
        main_bag = line.split(' bags contain ')[0]
        sub_bags = [bag.replace(' bags', '').replace(' bag', '').replace('.', '')
                    for bag in line.split(' bags contain ')[1].split(', ')]
        if sub_bags[0] == 'no other':
            sub_bags_with_count = [(0, '')]
        else:
            sub_bags_with_count = [(int(list(re.findall(r'^\d+', bag))[0]), re.findall(r'\D+', bag)[0].strip())
                                   for bag in sub_bags]
        bag_rules[main_bag] = sub_bags_with_count
    return bag_rules


def solve_day7_1():
    dict_rules = import_input_7()
    dict_rules_simple = {k: [bags[1] for bags in v] for k, v in dict_rules.items()}

    shiny_gold_bags = set([k for k, v in dict_rules_simple.items() if 'shiny gold' in v])
    for i in range(len(dict_rules_simple.keys())):
        shiny_gold_bags |= set(
            [k for k, v in dict_rules_simple.items() if any([shiny in v for shiny in shiny_gold_bags])])

    return len(shiny_gold_bags)

print(solve_day7_1())