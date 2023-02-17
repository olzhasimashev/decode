n = int(input())
d = {}

for i in range(n):
    x, y = input().split()
    d[x] = y

word = input()

for i in d.keys():
    if d[i] == word:
        print(i)