n = int(input())
values = []

for i in range(n):
    values.append(int(input()))

print(*sorted(values))