num_list = []
max_num = 0
index = 0

for i in range(9):
    a = int(input())
    num_list.append(a)

for j in range(9):
    if num_list[j] > max_num:
        max_num = num_list[j]
        index = j + 1

print(max_num)
print(index)