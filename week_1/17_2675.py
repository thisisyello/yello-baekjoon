t = int(input())

for i in range(t):
    s = input().split()
    snum = int(s[0])
    spop = s.pop()

    for i in spop:
        print(i * snum, end='')
    print()

