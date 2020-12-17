"""
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely.
Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets.
The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket,
including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class,
and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure.
What do you get if you multiply those six values together?
"""
from day_16.task_1 import validate_tickets, generate_rules
from collections import Counter



def identify_ticket_values(tickets, rules):
    position_prediction = {
            rule: []
            for rule in rules.keys()
        }

    for ticket in tickets:
        for index, ticket_value in enumerate(ticket):
            ticket_value = int(ticket_value)

            for rule_name, rule in rules.items():
                valid = int(rule[0]) <= ticket_value <= int(rule[1]) or \
                        int(rule[2]) <= ticket_value <= int(rule[3])

                if valid:
                    position_prediction[rule_name].append(index)

    valid_options = {
        key: [key for key, count in Counter(value).items() if count == len(tickets)]
        for key, value in position_prediction.items()
    }

    checked = set()

    final_prediction = {}
    for i in range(len(valid_options)):
        for rule_name, option in valid_options.items():
            valid_options[rule_name] = list(set(option) - checked)

            if len(option) == 1:
                checked.add(option[0])
                final_prediction[rule_name] = option[0]

    return final_prediction

if __name__ == '__main__':
    input_data = open("input.txt", "r").read()

    data_split = input_data.split("\n\n")

    own_ticket = data_split[1].replace("your ticket:\n", "").split(",")
    rules = generate_rules(data_split[0])
    _, valid_tickets = validate_tickets(input_data)
    ticket_values = identify_ticket_values(valid_tickets, rules)

    res = 1
    for k, v in ticket_values.items():
        if "departure" in k:
            res *= int(own_ticket[v])

    print(f"The answer is: {res}")
