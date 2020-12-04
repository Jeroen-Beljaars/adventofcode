import re

REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate_passport(passport):
    """
    Checks if a passport is valid

    :param passport: The biome. Must be made of . for empty spaces and # for trees
    """
    passport_attributes = re.split(r"[\n ]", passport)
    passport_attribute_names = set([passport_attribute.split(":")[0] for passport_attribute in passport_attributes])

    present_attributes = passport_attribute_names.intersection(REQUIRED_ATTRIBUTES)

    return present_attributes == set(REQUIRED_ATTRIBUTES)

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n\n")
    valid_passports = 0
    for passport in input_data:
        valid_passports += 1 if validate_passport(passport) else 0
    print(f"Amount of valid passports: {valid_passports}")