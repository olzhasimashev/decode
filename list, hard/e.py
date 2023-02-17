n = int(input())
values = []
cnt = 0

for i in range(n):
    values.append(int(input()))

for i in values:
    flag = True
    for j in range(2, i):

        if i%j==0:
            flag = False
    if flag and i != 1 and i != 0:
        print(i)