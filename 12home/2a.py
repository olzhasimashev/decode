a = input().split()

count = list()

for i in range(len(a)):
    if a[i] in a[:i]:
        count.append(a[:i].count(a[i]))
    else:
        count.append(0)
print(*count)