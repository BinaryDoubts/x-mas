from random import *


def dicePool(size):
    results = []
    cur = 0
    while cur < size:
        results.append(randrange(1,6))
        cur += 1

    results.sort()
    return results


groups = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
}

trials = 100

for j in range(0, trials):
    matches = [0, 0, 0, 0, 0, 0]
    res = dicePool(4)

    for i in range(0, len(res)):
        matches[res[i]-1] += 1

    for j in range(0, len(matches)):
        if matches[j] > 0:
            if matches[j] > 5:
                matches[j] = 5
            groups[str(matches[j])] += 1


print("No matches: " 
print("Pairs: " + str(groups["2"] / 10 / trials * 100))
print("Triples: " + str(groups["3"] / 10 / trials * 100))
print("Quads: " + str(groups["4"] / 10 / trials * 100))
print("Five+: " + str(groups["5"] / 10 / trials * 100))