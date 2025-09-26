from collections import deque
import sys
input = sys.stdin.readline

# n = 세로 / m = 가로
n, m = map(int, input().split())
# 2차원 배열
maze = [list(map(int, input().strip())) for _ in range(n)]

# 큐를 생성하고 시작점 삽입
q = deque([(0, 0)])
# 상하좌우 인접 칸을 탐색하기 위한 방향 벡터 모음
directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# q 가 empty일 때 까지
while q:
    # 현재 좌표값?
    x, y = q.popleft()
    # 만약에 끝점에 도달하면
    if x == n - 1 and y == m - 1:
        # 최종점 출력 (밑에 for문에서 누적이 됨)
        print(maze[x][y])
        break
    
    # 상하좌우 인접 칸 탐색
    for dx, dy in directs:
        nx, ny = dx + x, dy + y
        # 좌표가 범위 밖인가? 만약 그 칸이 1이면
        if n > nx >= 0 and m > ny >= 0 and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.append((nx, ny))