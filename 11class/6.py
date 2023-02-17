l = []
s = set()
for i in range(int(input())):
    l.append(input())
s.update(l)
print(len(l)-len(s))