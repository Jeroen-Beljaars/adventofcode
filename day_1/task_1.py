"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

DEFAULT_SUM = 2020


def find_sum(numbers, desired_sum=DEFAULT_SUM):
    """
    find the two entries that sum to and then multiply those two numbers together.

    :param numbers:     List of numbers to use
    :param desired_sum: Desired sum, the algorithm will try to find two items from the numbers list that sum to this
                        number.
    :return:            The product of the two numers that sum to the desired sum.
    """
    for index, number in enumerate(numbers):
        # We calculate the number required to get to 2020.
        required_num = desired_sum - number

        # Check if the required number is in the list (this way we don't have to loop over all nums & try to see if
        # it's the desired number!)
        if required_num in numbers and numbers.index(required_num) != index:
            print(f"Numbers {number} and {required_num} together sum to {desired_sum}!")

            return number * required_num


if __name__ == '__main__':
    input_data = [1865, 1179, 1328, 1390, 322, 1999, 1713, 1808, 1380, 1727, 1702, 1304, 1481, 1334, 1728, 1953, 1413,
                  1753, 1723, 1379, 1532,
                  1918, 1490, 71, 1388, 1519, 807, 1427, 1729, 1952, 970, 1405, 1500, 1782, 1899, 1501, 1720, 1832,
                  1706, 1658, 1333, 486, 1670,
                  1674, 1290, 1893, 1382, 1761, 1945, 1607, 1319, 1508, 1464, 1733, 1917, 1483, 1620, 1677, 1835, 1810,
                  1385, 1840, 1705, 1994,
                  1695, 1599, 1681, 1566, 1153, 1672, 1373, 1679, 1714, 1283, 1950, 1197, 1696, 1936, 1218, 1910, 1786,
                  958, 1565, 1583, 1914,
                  1853, 1682, 1267, 1543, 1322, 1965, 1406, 860, 1754, 1867, 1393, 1404, 1191, 1861, 2007, 1613, 1938,
                  1340, 1227, 1628, 1826, 1638, 1970,
                  1993, 1748, 496, 1661, 1736, 1593, 1298, 1882, 1763, 1616, 1848, 92, 1338, 1707, 1587, 1996, 1708,
                  700, 1460, 1673, 1450, 1815, 1537, 1825, 1683, 1743, 1949, 1933, 1289, 1905, 1307, 1845, 1855, 1955,
                  1554, 1570, 1931, 1780, 1929, 1980, 1978, 1998, 1371, 1981, 1817, 1722, 1545, 1561, 1352, 1935, 1553,
                  1796, 1847, 1640, 1414, 1198, 1669, 1909, 1879, 1744, 1783, 1367, 1632, 1990, 1937, 1919, 1431, 2002,
                  1603, 1948, 1317, 1282, 1349, 1839, 1575, 1730, 1849, 1959, 1971, 2009, 1641, 1402, 1924, 1757, 1605,
                  1693, 1762, 283, 1525, 1964, 1715, 1602]
    print(find_sum(input_data))
