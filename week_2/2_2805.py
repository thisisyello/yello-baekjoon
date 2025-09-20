import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n = 나무의 개수 / m = 필요한 나무의 길이
height = list(map(int, input().split())) # 나무의 높이

def cut_tree(arr, target):
    left, right = 0, max(arr)

    while left <= right:
        mid = (left + right) // 2
        cut = 0
        for h in arr:
            if h > mid:
                cut += h - mid
        if cut >= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(cut_tree(height, m))