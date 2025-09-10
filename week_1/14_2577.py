a = int(input())
b = int(input())
c = int(input())

d = a * b * c
result = [0] * 10
std = str(d)

for i in std:
    result[int(i)] += 1

for j in result:
    print(j)