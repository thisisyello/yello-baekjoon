c = int(input())

average = 0
count = 0
result = []

for i in range(c):
    n = list(map(int, input().split()))
    average = (sum(n) - n[0]) / n[0]

    for j in range(1, len(n)):
        if n[j] > average:
            count += 1
    a = (count / n[0]) * 100
    result.append(f"{a:.3f}%")
    count = 0

for r in result:
    print(r)
