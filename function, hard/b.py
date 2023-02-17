def greater_seven():
    for i in films.keys():
        if films[i]>7:
            print(i)

n = int(input())
films = dict()

for i in range(n):
    name, score = input().split()
    films[name] = int(score)

greater_seven()