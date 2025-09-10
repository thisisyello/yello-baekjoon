def hanoi(n, start, layer, end):
    if n == 1:
        print(start, end)
        return 1
    hanoi(n - 1, start, end, layer)
    hanoi(1, start, layer, end)
    hanoi(n - 1, layer, start, end)


n = int(input())
k = 2 ** n - 1

if n > 20:
    print(k)
else:
    print(k)
    hanoi(n, 1, 2, 3)