n = int(input())
a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

cnt = 0

for row in a:
    for elem in row:
        if elem < 0:
            cnt +=1
print(cnt)