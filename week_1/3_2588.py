A = int(input())
B = int(input())

B_2 = B % 10
B_1 = (B // 10) % 10
B_0 = B // 100

print(A * B_2, A * B_1, A * B_0, A * B, sep="\n")