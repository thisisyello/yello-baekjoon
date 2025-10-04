import sys
input = sys.stdin.readline

# 물건의 개수와 버틸 수 있는 무게
n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
about_item = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    w, v = about_item[i - 1]
    for j in range(k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])