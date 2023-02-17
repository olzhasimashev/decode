n = int(input())
values = []

for i in range(n):
    values.append(input())

sorted_values = sorted(values, key = len)
sorted_values.reverse()

for n in range(len(sorted_values)-1, 0, -1):
    for i in range(n):
        if len(sorted_values[i]) == len(sorted_values[i + 1]):
            swap = []
            swap.append(sorted_values[i])
            swap.append(sorted_values[i+1])
            swap.sort()
            sorted_values[i] = swap[0]
            sorted_values[i+1] = swap[1]
            break

print(*sorted_values)