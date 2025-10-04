import sys
input = sys.stdin.readline

n = int(input())
num_list = [0, 1]

for i in range(n):
    if n < len(num_list):
        break
    new_n = num_list[i] + num_list[i + 1]
    num_list.append(new_n)

print(num_list[-1])