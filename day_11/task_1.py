"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the
tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry,
you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can
predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
For example, the initial seat layout might look like this:

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
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and
always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from the seat).
The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause
no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?
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

            surrounding_seats.append(seat_blueprint[row_index + r][seat_index + s])

    if current_status == SeatStatus.EMPTY.value and surrounding_seats.count(SeatStatus.OCCUPIED.value) == 0:
        return SeatStatus.OCCUPIED.value
    elif current_status == SeatStatus.OCCUPIED.value and surrounding_seats.count(SeatStatus.OCCUPIED.value) >= 4:
        return SeatStatus.EMPTY.value

    return current_status

def predict_seating(input_data):
    new_seating, current_seating = input_data, input_data

    while True:
        current_seating = deepcopy(new_seating)

        for row_index, row in enumerate(current_seating):
            for seat_index, seat in enumerate(row):
                new_seating[row_index][seat_index] = get_new_seat_status(row_index, seat_index, current_seating)

        for row in new_seating:
            print(row)

        print()

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