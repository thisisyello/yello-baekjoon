import sys
input = sys.stdin.readline


a = list(input())
b = list(input())

lcs = [[0] * (len(b)) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(a) - 1][len(b) - 1])