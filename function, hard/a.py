def sort():
    values.sort()
    even = list()
    odd = list()
    for i in values:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even+odd



n = int(input())
values = list()
for i in range(n):
    values.append(int(input()))

print(sort())