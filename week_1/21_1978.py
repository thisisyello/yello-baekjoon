n = int(input())
a = list(map(int, input().split()))
is_prime = True
count = 0

for i in a:
    is_prime = True
    if i == 1:
        continue
    for j in range(2, i): 
        if i % j == 0:
            is_prime = False
            break
    if(is_prime):
        count += 1
    
print(count)