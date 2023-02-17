# w = input().split()
# s = set(w)
# n = list()
# d = {}

# w1 = sorted(list(s))

# for i in w1:
#     n.append(w.count(i))

# for i in range(len(w1)):
#     d[w1[i]]=n[i]
# print(d)

a= input().split()

d={}

for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] =1

for k in sorted(d.keys()):
    print(k ,d[k])