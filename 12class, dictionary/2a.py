n = int(input())

d={}

for i in range(n):
    name,grade = input().split()

    d[name] = int(grade)

print('name | grade')
for i in sorted(d.keys()):
    print(i,':',d[i])