n = int(input())
values = list()

for i in range(n):
    values.append(input())

file = open("olzhas.txt", "w")

for i in values:
    file.write(i + "\n")
file.close()