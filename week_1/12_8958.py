a = int(input())
answer_list = []

for i in range(a):
    answer = input()
    answer_list.append(answer)

start_score = 1
last_score = 0

for j in range(a):
    for b in range(len(answer_list[j])):
        if answer_list[j][b] == "O":
            last_score += start_score
            start_score += 1
        else:
            start_score = 1
    start_score = 1

    print(last_score)

    last_score = 0