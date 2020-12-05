"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""


def calculate_seat_id(seat_instructions):
    """
    :param seat_instruction:    The direction to the seat using binary space partitioning.
    :return                     The Seat ID (Row * 8 + column)
    """
    # Extract the row instructions and convert it to binary
    row_instructions = seat_instructions[:7].replace("F", "0").replace("B", "1")

    # Extract the column instructions and convert it to binary
    column_instructions = seat_instructions[7:].replace("L", "0").replace("R", "1")

    # Convert the row binary to a number
    seat_row = int(row_instructions, 2)

    # Convert the col binary to a number
    seat_column = int(column_instructions, 2)

    # Convert it to binary
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
