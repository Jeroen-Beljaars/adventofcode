DEFAULT_SUM = 2020


def find_three_sum(numbers, desired_sum=DEFAULT_SUM):
    """
    find the two entries that sum to and then multiply those two numbers together.

    :param numbers:             List of numbers to use
    :param desired_sum:         Desired sum, the algorithm will try to find two items from the numbers list that
                                sum to this number.
    :return:                    The product of the two numbers that sum to the desired sum.
    """
    for index, number in enumerate(numbers):
        # We calculate the number required to get to 2020.
        required_num = desired_sum - number

        for index2, number2 in enumerate(numbers[index:]):
            sum_of_num = number + number2
            required_num = desired_sum - sum_of_num

            if required_num < 0:
                continue

            # Check if the required number is in the list (this way we don't have to loop over all nums again &
            # try to see if it's the desired number!)
            if required_num in numbers and numbers.index(required_num) != index:
                print(f"Numbers {number}, {number2}, and {required_num} together sum to {desired_sum}!")

                return number * number2 * required_num


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

    print(find_three_sum(input_data))
