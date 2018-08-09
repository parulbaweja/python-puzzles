import collections
import pprint

d = collections.Counter()
with open("puzzle-2.txt") as file:
    for line in file:
        d.update(line)

    pprint.pprint(d)

