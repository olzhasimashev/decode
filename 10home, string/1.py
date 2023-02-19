s = input().split()
cnt = 0

for i in range(len(s)):
    cnt += s.count(s[i])
    
print(cnt)