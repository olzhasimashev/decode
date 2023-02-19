n = int(input())

d1 = {}
d2 = {}

for i in range(n):
    log1, pas1 = input().split()
    d1[log1]=pas1

m = int(input())

for i in range(m):
    log2, pas2 = input().split()
    d2[log2]=pas2

for i in d2.keys():
    if i not in d1.keys():
        print('user not defined')
    elif d2[i]==d1[i]:
        print('welcome')
    else:
        print('wrong')