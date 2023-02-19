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
        if (i+j)%2 == 0:
            a[i][j] += 1
        else:
            a[i][j] -= 1

for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()