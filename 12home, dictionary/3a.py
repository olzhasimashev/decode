n = int(input())

d = {}

for i in range(n):
    i = input().split()
    d[i[0]] = i[1:]

n1 = int(input())
cities = list()

for i in range(n1):
    cities.append(input())

for i in range(n1):
    for j in d.keys():
        if cities[i] in d[j]:
            print(j)