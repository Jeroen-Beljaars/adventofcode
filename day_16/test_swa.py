import re

puzzle = open('input.txt').read().splitlines()

rules = {}
names = {}
your_ticket = []
nearby_tickets = []
options = {}
valid_tickets = 0

t = 0
for x in puzzle:
    if x == '':
        t += 1
        continue
    if t == 0:
        thing, ranges = x.split(': ')
        ranges = [int(_) for _ in re.findall(r'\d+', ranges)]
        rules[thing] = ranges
    elif t == 1:
        if x.startswith('y'):
            continue
        your_ticket = [int(_) for _ in x.split(',')]
    else:
        if x.startswith('n'):
            continue
        nearby_tickets.append([int(_) for _ in x.split(',')])


def is_withing_ranges(value, ranges):
    return ranges[0] <= value <= ranges[1] or \
           ranges[2] <= value <= ranges[3]


def is_valid(values):
    for value in values:
        invalid = []
        for ranges in rules.values():
            invalid.append(not is_withing_ranges(value, ranges))
        if all(invalid):
            return False
    return True


options = {}
valid_tickets = 0
for ticket in nearby_tickets:
    if not is_valid(ticket):
        continue

    valid_tickets += 1
    for i, value in enumerate(ticket):
        for name, ranges in rules.items():
            if is_withing_ranges(value, ranges):
                if options.get(name, -1) == -1:
                    options[name] = [i]
                    continue
                options[name].append(i)

checked = []
amount_per_index = {}
for i in range(len(options.items())):
    for name, option in options.items():
        count = [(i, option.count(i)) for i in range(len(set(option)))]
        count.sort(key=lambda tup: tup[1])
        count = [x[0] for x in count if x[1] == valid_tickets]
        amount_per_index[name] = count

for i in range(len(amount_per_index.items())):
    for name, option in amount_per_index.items():
        for c in checked:
            if c in option:
                option.remove(c)
        if len(set(option)) == 1:
            checked.append(option[0])
            names[name] = option[0]

count = 1
for x in [_ for _ in rules.keys() if _.startswith('departure')]:
    count *= your_ticket[names[x]]
print(count)
