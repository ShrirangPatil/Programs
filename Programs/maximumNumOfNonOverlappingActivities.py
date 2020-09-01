"""
Maximum number of non overlapping activity from a set of starting point
of activities arrays and ending point of acctivies
"""

i = -1
def mapFun(num):
    global i
    i += 1
    return (i, float(num))

def sortKey(a):
    return a[1]


def end(a):
    return EndPoints[a[0]][1]

def start(a):
    return StartPoints[a[0]][1]


def isSingleLine(a, b):
    if a[1] != start(b) or end(a) != b[1]:
        return 1
    return 0

if __name__ == "__main__":
    StartPoints = list(map(mapFun, input().split(' ')))
    i = -1
    EndPoints = list(map(mapFun, input().split(' ')))

    SStartPoints = sorted(StartPoints, key = sortKey)
    SEndPoints = sorted(EndPoints, key = sortKey, reverse = True)
    print(SStartPoints, SEndPoints, sep = "\n")


    #print(end(SStartPoints[2]))
    #print(start(SEndPoints[1]))

    i = 0
    count = 0
    minEnd = None
    maxStart = None

    while i < len(StartPoints):
        print(SStartPoints[i][1], start(SEndPoints[i]))
        print(end(SStartPoints[i]), SEndPoints[i][1])
        if isSingleLine(SStartPoints[i], SEndPoints[i]): #SStartPoints[i][1] != start(SEndPoints[i]) or end(SStartPoints[i]) != SEndPoints[i][1]:
            minEnd = end(SStartPoints[i])
            maxStart = start(SEndPoints[i])
            break
        i += 1
    print(minEnd, maxStart, i)
    #print(end(SStartPoints[i]), start(SEndPoints[i]))
    if i < len(StartPoints):
        count = 2
        while (i+1 < len(StartPoints)) and (end(SStartPoints[i]) <= start(SEndPoints[i])):
            if isSingleLine(SStartPoints[i+1], SEndPoints[i+1]):
                i += 1
                continue
            if start(SStartPoints[i+1]) >= minEnd:
                count += 1
                minEnd = end(SStartPoints[i+1])
            elif end(SStartPoints[i+1]) < minEnd:
                minEnd = end(SStartPoints[i+1])

            if end(SEndPoints[i+1]) <= maxStart:
                count += 1
                maxStart = start(SEndPoints[i+1])
            elif start(SEndPoints[i+1]) > maxStart:
                maxStart = start(SEndPoints[i+1])
            i += 1
        print(count)
    else:
        print(1)

# Test cases
"""
1 2 3 0 4
2 3 4 2 5
4
"""
"""
1 1 1.5 2.5 3
5 2.5 3 3.5 4.5
2
"""
"""
2 2 2 2
3 3 3 3
1
"""
