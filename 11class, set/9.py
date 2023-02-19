s1 = set()
s2 = set()
for i in range(int(input())):
    s1.add(input())
for i in range(int(input())):
    s2.add(input())
print("absence:", s2-s1 )
print("imposter:", s1-s2 )