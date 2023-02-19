s = input()
d = {}
cnt = 0

for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] +=1

for i in d.values():
    if i%2 != 0:
        cnt += 1

if cnt>1:
    print('wasted')
else:
    print('good')