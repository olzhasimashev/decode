a = []

for i in range(8):
    a.append([j for j in input().split()])

for i in range(len(a)):
    for j in range(len(a[i])):
        if ord(a[i][j]) == 83:
            # for k in range(1, 8-i):
            #     a[i+k][j+k] = '!'
            # for k in range(1, i-1):
            #     a[i-k][j+k]= '!'
            # for k in range(1, 8-i):
            #     a[i+k][j-k]= '!'
            # for k in range(1, i-1):
            #     a[i-k][j-k]= '!'
            for k in range(i+1, 8-1):
                a[k][k+1] = '!'
            for k in range(i-1, 0, -1):
                a[k][k-1] = '!'
            for k in range(j+1, 8-1):
                a[k+1][k] = '!'
            for k in range(j-1, 0, -1):
                a[k-1][k] = '!'

print()

for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()