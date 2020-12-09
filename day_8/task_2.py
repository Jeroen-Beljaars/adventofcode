"""
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
(No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in
 the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never
leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions
are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last
instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?
"""


def boot(input_data):
    operations = []
    for operation in input_data:
        command, value = operation.split(" ")
        # Command, numeric value, visited True/False
        operations.append([command, int(value), False])

    current_index = 0
    acc_value = 0
    index_history = []
    changed_index = -1
    lock_history = False
    while True:
        if current_index >= len(operations):
            return acc_value

        if not lock_history:
            index_history.append(current_index)

        current_operation = operations[current_index]
        command, value, visited = current_operation

        if visited:
            lock_history = True
            if changed_index != -1:
                command = operations[index_history[changed_index]][0]
                operations[index_history[changed_index]][0] = "nop" if command == "jmp" else "jmp"

                changed_index -= 1
            else:
                changed_index = len(index_history) - 1

                command = operations[index_history[changed_index]][0]
                operations[index_history[changed_index]][0] = "nop" if command == "jmp" else "jmp"

            current_index = 0
            acc_value = 0
            for operation in operations:
                operation[2] = False

            continue

        if command == "acc":
            acc_value += value

        if command == "jmp":
            current_index += value
        else:
            current_index += 1

        # Set visited to True
        current_operation[2] = True


if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n")[:-1]

    acc = boot(input_data)

    print(f"Acc is {acc}")