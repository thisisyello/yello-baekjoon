import sys
input = sys.stdin.readline

n = int(input()) # list a 에 들어갈 수의 개수
list_a = set(map(int, input().split()))
m = int(input()) # list b 에 들어갈 수의 개수
list_b = list(map(int, input().split()))

for i in list_b:
    if i in list_a:
        print(1)
    else:
        print(0)


def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
list_a = list(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))
list_a.sort()

for i in list_b:
    idx = lower_bound(list_a, i)
    if idx < len(list_a) and list_a[idx] == i:
        print(1)
    else:
        print(0)

# 구현 경계성 단조성 ##############