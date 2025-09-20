import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
    def pop(self):
        if self.q:
            return self.q.popleft()
        else:
            return -1
    def size(self):
        return len(self.q)
    def empty(self):
        if not self.q:
            return 1
        else:
            return 0
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1
    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1
        
n = int(input())
queue = Queue()

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.push(command[1])
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())


# ----- 클래스로 추상화하지 않고 if/elif로 명령어를 처리한 구조라 “간단한 큐 시뮬레이션” 버전 -----
# n = int(input())
# queue = deque()

# for i in range(n):
#     command = input().split()
#     command_1 = command[0]
#     command_2 = command[1] if len(command) > 1 else None

#     if command_1 == 'push':
#         queue.append(command_2)
#     elif command_1 == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue.popleft())
#     elif command_1 == 'size':
#         print(len(queue))
#     elif command_1 == 'empty':
#         if not queue:
#             print(1)
#         else:
#             print(0)
#     elif command_1 == 'front':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#     elif command_1 == 'back':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[-1])