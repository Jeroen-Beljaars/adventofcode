"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""
from string import ascii_lowercase

def get_answer_count(answers):
    """
    :param answers: String containing letters which represent an answer
    :return         The total amount of answers given by every person in a group
    """
    answers_per_person = answers.split("\n")

    answer_matches = set(answers_per_person[0])
    for person_answers in answers_per_person[1:]:
        if not person_answers:
            continue

        answer_matches = answer_matches.intersection(set(person_answers))

        if not answer_matches:
            break

    return len(set(answer_matches))

if __name__ == '__main__':
    input_data = open("input.txt", "r").read().split("\n\n")

    answer_count = 0

    for answers in input_data:
        answer_count += get_answer_count(answers)

    print(f"The total answer count is {answer_count}")
