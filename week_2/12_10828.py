import sys
input = sys.stdin.readline

number = int(input())
stack = []
n = 0

for i in range(number):
    abc = input().split()
    abc_1 = abc[0]
    abc_2 = abc[1] if len(abc) > 1 else None
    if abc_1 == "push":
        stack.append(abc_2)
        n += 1
    if abc_1 == "pop":
        if n <= 0:
            print(-1)
        else:
            print(stack[n-1])
        if len(stack) > 0:
            stack.pop()
            n -= 1
    if abc_1 == "size":
        print(len(stack))
    if abc_1 == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    if abc_1 == "top":
        if not stack:
            print(-1)
        else:
            print(stack[n-1])