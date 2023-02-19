def sum(values):
    if len(values) == 0:
        return 0
    else:
        return sum(values[:-1])+values[-1]

values = list(map(int,input().split()))
print(sum(values))