import sys
input = sys.stdin.readline

k = int(input())
sum_list = []

for i in range(k):
    num = int(input())
    
    if num == 0:
        sum_list.pop(len(sum_list) - 1)
    else:
        sum_list.append(num)

print(sum(sum_list))