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
