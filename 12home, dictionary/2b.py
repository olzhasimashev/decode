a= input()

d={}

for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] =1
print(d)