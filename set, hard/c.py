n = int(input())
values = set()

for i in range(n):
    values.add(int(input()))

values = sorted(values)

for i in range(len(values)-1, 0, -1):
    for j in range(1, i):
        if i+(j) == max(values):
            print(i, j)