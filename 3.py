from random import randint

x = randint(1,3)
print(x)

a = int(input())

if a-x==0:
    print("draw")
elif a==1:
    if x==2:
        print("win")
    else:
        print("lose")
elif a==2:
    if x==3:
        print("win")
    else:
        print("lose")
elif a==3:
    if x==1:
        print("win")
    else:
        print("lose")