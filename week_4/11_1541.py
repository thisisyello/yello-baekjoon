import sys
input = sys.stdin.readline

n = input().strip()
nn = n.split('-')
int_nn = 0
nnn = []

result = 0

for i in range(len(nn)):
    nnn.append(sum(map(int, nn[i].split('+'))) * -1)

nnn[0] = nnn[0] * -1
for j in range(len(nnn)):
    result = sum(nnn)
    
    
print(result)