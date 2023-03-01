file = open("hardC.txt", "r")

values = file.read().split()

for word in values:
    if word == word[::-1]:
        print(word, end = " ")

file.close()