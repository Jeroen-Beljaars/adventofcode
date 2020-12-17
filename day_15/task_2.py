def sayNumsHashed(start, end = 30000000):
    ht = {}
    def addToHt(ht, e, ts):
        if e in ht:
            ht[e].append(ts)
        else:
            ht[e] = [ts]
    def getLastSeen(ht, e, ts):
        assert e in ht
        if ht[e][-1] == ts:
            return ht[e][-2]
        else:
            return ht[e][-1]

    for i in range(len(start)):
        addToHt(ht, start[i], i+1)
    ts = len(start)
    lastSeen = start[-1]
    while ts != end:
        if len(ht[lastSeen]) == 1:
            lastSeen = 0
            addToHt(ht, 0, ts + 1)
        else:
            ls = getLastSeen(ht, lastSeen, ts)
            age = ts - ls
            lastSeen = age
            addToHt(ht, age, ts + 1)
        ts += 1
    return lastSeen

def main():
    return sayNumsHashed([20,9,11,0,1,2])

print(main())