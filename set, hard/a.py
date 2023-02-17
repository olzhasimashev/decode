n = int(input())
values = set()
for i in range(n):
    values.add(int(input()))
flag = False
for i in values:
    if i==1 or i==0:
        flag = True
        break
    for j in range(2, i):
        if i%j == 0:
            flag = True
            break
if flag:
    print('bad')
else:
    print('good')