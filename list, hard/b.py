n = int(input())

letters = []
ans = []

for i in range(n):
    letters.append(input())

value = input()

for i in range(n):
    if letters[i] == value:
        ans.append(i)

if len(ans) > 1:
    print(min(ans), max(ans))
else:
    print(*ans)