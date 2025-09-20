import sys
import heapq
input = sys.stdin.readline

n = int(input())
x_list = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not x_list:
            print(0)
        else:
            print(-heapq.heappop(x_list))
    else:
        heapq.heappush(x_list, -x)
# print(x_list)


# nums = [5, 3, 8, 1, 2]
# heapq.heapify(nums) # 리스트를 바로 최소 힙으로 변환
# print(nums)
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(nums)

# pq = []
# for x in nums:
#     heapq.heappush(pq, -x)   # 음수로 저장

# print(-heapq.heappop(pq))  # 8 (가장 큰 값)
# print(-heapq.heappop(pq))  # 5
# print(pq)
# print(nums)
