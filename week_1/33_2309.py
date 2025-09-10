
from itertools import combinations

n_height = []

for _ in range(9):
    n = int(input())
    n_height.append(n)

n_height.sort()

result = []
n = len(n_height)
for c in combinations(n_height, 7):
    if sum(c) == 100:
        result = c
for i in range(7):
    print(result[i])