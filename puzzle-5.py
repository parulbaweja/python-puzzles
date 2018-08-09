import pickle
import pprint

with open("puzzle-5.txt", "rb") as f:
    unpickled = pickle.load(f)
    for line in unpickled:
        #     print(line)
        print("".join([i*j for i, j in line]))
#     for line in f:
#         print(pickle.loads(line))
