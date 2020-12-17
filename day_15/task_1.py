def sayNums(start, end = 2020):
    while len(start) != end:
        if start.count(start[-1]) == 1:
            start.append(0)
        else:
            i = 0
            for e in reversed(start):
                if e == start[-1] and i != 0:
                    start.append(i)
                    break
                i += 1
    return start[-1]

def main():
    return sayNums([20,9,11,0,1,2])

print(main())