def f(n):
    if n ==0:
        return 0
    return f(n//10)+n%10

print(f(int(input())))