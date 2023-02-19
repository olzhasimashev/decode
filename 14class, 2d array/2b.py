n = int(input())
m = int(input())

a = []

for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == max(a[i]):
            print(i,':', j)
    
    