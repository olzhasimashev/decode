n = int(input())

d={}
bank = 0

for i in range(n):
    name, money = input().split()

    if name not in d:
        d[name]=int(money)
    else:
        d[name]+=int(money)
    bank+=int(money)

for i in sorted(d.keys()):
    percent = (d[i]/bank)*100
    print(i , f'{percent}%')