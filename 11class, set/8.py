s = input().split()
a = set()
print(s)
for i in s:
    a.update(set(i))
a = list(a)
a.sort(reverse=True)
print(a)
