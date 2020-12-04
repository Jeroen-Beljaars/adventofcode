"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

import re
def check_amount_valid_passwords(policies_and_passwords):
    """
    find the two entries that sum to and then multiply those two numbers together.

    :param numbers:     List of numbers to use
    :param desired_sum: Desired sum, the algorithm will try to find two items from the numbers list that sum to this
                        number.
    :return:            The product of the two numers that sum to the desired sum.
    """
    amount_of_valid_passwords = 0
    for policy_password in policies_and_passwords:
        if not policy_password:
            continue

        policy, password = policy_password.split(": ")
        policy_matched = re.search(r"([0-9]*)-([0-9]*) ([a-zA-Z])", policy)
        min_occurrence, max_occurrence, letter = int(policy_matched.group(1)), int(policy_matched.group(2)), \
                                                 policy_matched.group(3)

        letter_count = password.count(letter)

        if min_occurrence <= letter_count <= max_occurrence:
            amount_of_valid_passwords += 1

    return amount_of_valid_passwords

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")
    print(check_amount_valid_passwords(input_data))
