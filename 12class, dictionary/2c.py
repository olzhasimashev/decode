w = input()
s = set(w)
n = list()
d = {}

w1 = sorted(list(s))

for i in w1:
    n.append(w.count(i))

for i in range(len(w1)):
    d[w1[i]]=n[i]

for i in d.keys():
    print(i,':', d[i])