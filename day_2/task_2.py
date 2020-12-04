"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
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
        first_index, second_index, letter = int(policy_matched.group(1)), int(policy_matched.group(2)), \
                                                 policy_matched.group(3)

        if (password[first_index - 1] == letter) != (password[second_index - 1] == letter):
            amount_of_valid_passwords += 1

    return amount_of_valid_passwords

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")
    print(check_amount_valid_passwords(input_data))
