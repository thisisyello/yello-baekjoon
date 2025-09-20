import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ps = input().strip()
    ps_list = []
    state = True

    for i in ps:
        if i == '(':
            ps_list.append(i)
        else:
            if not ps_list:
                state = False
                break
            ps_list.pop()

    if state and not ps_list:
        print('YES')
    else:
        print('NO')