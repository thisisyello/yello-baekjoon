import sys
input = sys.stdin.readline

n = int(input())

tile_0 = 1
tile_1 = 2

if n <= 3:
    print(n)
else:
    for i in range(n - 2):
        new_n = (tile_0 + tile_1) % 15746
        tile_0 = tile_1
        tile_1 = new_n

    print(tile_1)