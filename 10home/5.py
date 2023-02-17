s = input()
l = []

for i in s:
	l.append(i)

for i in l:
    if i.islower():
        print(i, ":", ord(i)-96)
    else:
        print(i, ":", ord(i)-64)