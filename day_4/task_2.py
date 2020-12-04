import re

# The attributes with their validation
REQUIRED_ATTRIBUTES = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("cm" in x and (150 <= int(x.replace("cm", "")) <= 193)) or
                     ("in" in x and (59 <= int(x.replace("in", "")) <= 76)),
    "hcl": lambda x: re.match(r"#[0-9a-f]{6}", x) is not None,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}


def validate_passport(passport):
    """
    Checks if a passport is valid

    :param passport: The biome. Must be made of . for empty spaces and # for trees
    """
    passport_attributes = re.split(r"[\n ]", passport)
    passport_attribute_names = set([passport_attribute.split(":")[0] for passport_attribute in passport_attributes])
    present_attributes = passport_attribute_names.intersection(REQUIRED_ATTRIBUTES)

    # First check if all attributes are present. If not then we don't need to validate.
    if present_attributes != set(REQUIRED_ATTRIBUTES.keys()):
        return False

    for passport_attribute in passport_attributes:
        name, value = passport_attribute.split(":")
        if name in REQUIRED_ATTRIBUTES.keys() and not REQUIRED_ATTRIBUTES[name](value):
            return False

    return True

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n\n")
    valid_passports = 0
    for passport in input_data:
        valid_passports += 1 if validate_passport(passport) else 0
    print(f"Amount of valid passports: {valid_passports}")