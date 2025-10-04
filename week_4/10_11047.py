import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# coins.sort(reverse=True)

count = 0

# for c in coins:
#     count += k // c
#     k = k % c
#     if k <= 0:
#         break

for i in range(len(coins) - 1, -1, -1):
    count += k // coins[i]
    k = k % coins[i]
    if k <= 0:
        break

print(count)