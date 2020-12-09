"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous
set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127.
(Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range;
in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""
from day_9.task_1 import validate_numbers


def find_contiguous_set(numbers, required_number):
    for index, number in enumerate(numbers):
        resulting_number = 0
        end_index = index + 2
        while resulting_number < required_number:
            subset = numbers[index:end_index]
            resulting_number = sum(subset)

            if resulting_number == required_number:
                return min(subset) + max(subset)

            end_index += 1

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")
    input_data = [int(n) for n in input_data if n]

    print(f"The sum of the min & max of the contagious set is {find_contiguous_set(input_data, validate_numbers(input_data))}")