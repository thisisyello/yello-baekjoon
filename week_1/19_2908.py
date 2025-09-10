num1, num2 = map(str, input().split())
num1_list=[]
num2_list=[]

for i in range(len(num1)):
    num1_list.insert(0, num1[i])
    num2_list.insert(0, num2[i])

num1 = int(''.join(num1_list))
num2 = int(''.join(num2_list))

if num1 > num2:
    print(num1)
else:
    print(num2)