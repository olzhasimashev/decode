n = int(input())
m = int(input())

a = []

for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in a:
    i.reverse()

for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()