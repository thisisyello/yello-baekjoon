import math

def is_prime(a):
    # a_list = []
    prime = [True] * (a + 1)  # 처음에는 모두 true로 초기화
    prime[0] = prime[1] = False  # 1은 소수가 아니므로

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(a)) + 1):
        if prime[i]:
            for j in range(i * i, a + 1, i):
                prime[j] = False

    # for i in range(2, a + 1):
    #     if prime[i] == True :
    #         a_list.append(i)
    return prime

t = int(input())
n_list = []
max_num = 0

for i in range(t):
    n = int(input())
    n_list.append(n)
max_num = max(n_list)

prime = is_prime(max_num)
for i in n_list:
    p = i // 2
    while p >= 2:
        o = i - p
        if prime[p] and prime[o]:
            print(p, o)
            break
        p -= 1