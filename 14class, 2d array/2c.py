a = []

for i in range(8):
    a.append([j for j in input().split()])

for i in range(len(a)):
    for j in range(len(a[i])):
        if ord(a[i][j]) == 88:
            a[i][j] = '@'
            a[i+1][j] = '@'
            a[i-1][j] = '@'
            a[i][j+1] = '@'
            a[i][j-1] = '@'

print()

for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()