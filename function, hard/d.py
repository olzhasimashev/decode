def k_max(k):
    values.sort(reverse = True)
    values1 = list(dict.fromkeys(values))
    return values1[k-1]

n = int(input())
values = list()

for i in range(n):
    values.append(int(input()))

k = int(input())

print(k_max(k))