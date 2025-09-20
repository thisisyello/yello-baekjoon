import sys
input = sys.stdin.readline

n = int(input())

n_list = [int(input()) for _ in range(n)]
height = []
for h in n_list:
    while height and height[-1] <= h:
        height.pop()
    height.append(h)
    
print(len(height))