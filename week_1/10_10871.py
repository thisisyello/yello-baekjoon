N, X = map(int, input().split())

A = list(map(int, input().split()))
B = []

# if len(A) > N:
#     print(f'{N}개만 입력해라..')
# else:
for i in range(N):
    if X > A[i]:
        print(A[i]) # ends = ' '?