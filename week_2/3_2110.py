import sys
input = sys.stdin.readline

n, count = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

def can(d):
    placed = 1
    last = home[0]
    for x in home[1:]:
        if x - last >= d:
            placed += 1
            last = x
            if placed >= count:
                return True
    return False

left, right = 1, home[-1] - home[0]
ans = 0
while left <= right:
    mid = (left + right) // 2
    if can(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)