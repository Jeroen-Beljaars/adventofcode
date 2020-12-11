"""
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats -
they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight
 directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an
occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply:
empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs,
you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty,
once equilibrium is reached, how many seats end up occupied?
"""
from collections import defaultdict, Counter
from copy import deepcopy
from enum import Enum


class SeatStatus(Enum):
    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."


def get_new_seat_status(row_index, seat_index, seat_blueprint):
    current_status = seat_blueprint[row_index][seat_index]
    if current_status == SeatStatus.FLOOR.value:
        return SeatStatus.FLOOR.value

    row_range = range(-1 if row_index else 0, 2 if row_index < len(seat_blueprint) - 1 else 1)
    seat_range = range(-1 if seat_index else 0, 2 if seat_index < len(seat_blueprint[0]) - 1 else 1)

    surrounding_seats = []
    for r in row_range:
        for s in seat_range:
            if r == 0 and s == 0:
                continue

            seat_status = seat_blueprint[row_index + r][seat_index + s]

            check_r = r
            check_s = s
            while seat_status == SeatStatus.FLOOR.value and 0 <= row_index + check_r < len(seat_blueprint) and \
                    0 <= seat_index + check_s < len(seat_blueprint[0]):
                seat_status = seat_blueprint[row_index + check_r][seat_index + check_s]
                check_r += r
                check_s += s

            surrounding_seats.append(seat_status)

    if current_status == SeatStatus.EMPTY.value and surrounding_seats.count(SeatStatus.OCCUPIED.value) == 0:
        return SeatStatus.OCCUPIED.value
    elif current_status == SeatStatus.OCCUPIED.value and surrounding_seats.count(SeatStatus.OCCUPIED.value) >= 5:
        return SeatStatus.EMPTY.value

    return current_status


def predict_seating(input_data):
    new_seating, current_seating = input_data, input_data

    iteration = 1
    while True:
        current_seating = deepcopy(new_seating)

        for row_index, row in enumerate(current_seating):
            for seat_index, seat in enumerate(row):
                new_seating[row_index][seat_index] = get_new_seat_status(row_index, seat_index, current_seating)

        print(iteration)

        iteration += 1

        if current_seating == new_seating:
            return new_seating

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")
    input_data = [list(n) for n in input_data if n]

    seat_prediction = predict_seating(input_data)
    flat_prediction = []
    for row in seat_prediction:
        flat_prediction.extend(row)

    seat_status_count = Counter(flat_prediction)

    print(f"Predicted amount of seats taken {seat_status_count[SeatStatus.OCCUPIED.value]}")