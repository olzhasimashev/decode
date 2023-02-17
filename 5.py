print("Консольный калькулятор")
print("Первое число:")
a=int(input())
print("Operator:")
b=input()
print("Second number:")
c=int(input())
print('Result')
if b=='+':
    print(a+c)
elif b=='-':
    print(a-c)
elif b=='*':
    print(a*c)
elif b=='/':
    print(a/c)
elif b=='**':
    print(a**c)
elif b=='//':
    print(a//c)
elif b=='%':
    print(a%c)