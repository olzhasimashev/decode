a = []

for i in range(8):
    a.append([j for j in input().split()])

for i in range(len(a)):
    for j in range(len(a[i])):
        if ord(a[i][j]) == 82:
            for k in range(i+1, 8):
                a[k][j] = '!'
            for k in range(i-1, -1, -1):
                a[k][j] = '!'
            for k in range(j+1, 8):
                a[i][k] = '!'
            for k in range(j-1, -1, -1):
                a[i][k] = '!'

print()

for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()