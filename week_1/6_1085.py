x, y, w, h = map(int,input().split())

hansu = [x, y, w-x, h-y]

print(min(hansu))