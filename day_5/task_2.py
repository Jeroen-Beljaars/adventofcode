"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

import re
from math import ceil, floor

REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def calculate_seat_id(seat_instructions):
    """
    :param seat_instruction:    The direction to the seat using binary space partitioning.
    :return                     The Seat ID (Row * 8 + column)
    """
    row_min, row_max = 0, 127
    column_min, column_max = 0, 7

    seat_row, seat_column = 0, 0
    for instruction in seat_instructions:
        # F means lower half
        if instruction == "F":
            if row_max - row_min == 1:
                seat_row = row_min
                continue

            row_max -= ceil((row_max - row_min) / 2)
        elif instruction == "B":
            if row_max - row_min == 1:
                seat_row = row_max
                continue

            row_min += ceil((row_max - row_min) / 2)
        elif instruction == "L":
            if column_max - column_min == 1:
                seat_column = column_min
                continue
            column_max -= ceil((column_max - column_min) / 2)
        elif instruction == "R":
            if column_max - column_min == 1:
                seat_column = column_max
                continue
            column_min += ceil((column_max - column_min) / 2)

    return (seat_row * 8) + seat_column

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")[:-1]
    seat_ids = [calculate_seat_id(instructions) for instructions in input_data]
    seat_ids = sorted(seat_ids)

    current_id = seat_ids[0]
    for seat_id in seat_ids:
        if seat_id != current_id:
            print(f"Your seatnumber is {current_id}")
            current_id += 1
        current_id += 1
