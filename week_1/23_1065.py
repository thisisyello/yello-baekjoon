n = str(input())
count = 0

for i in range(1, int(n)+1):
    if i < 100:
        count += 1
        # print(n)
    else:
        s = str(i)
        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            count += 1

print(count)