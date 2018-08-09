import collections
import re

regex = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
with open("puzzle-3.txt") as f:
    for line in f:
        cur = re.findall(regex, line)
        if cur:
            print(cur)
