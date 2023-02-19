def f(n,k=2):
    if n == 1:
        return
    if n % k == 0:
        print(k,end= " ")
        return f(n/k)
    return f(n,k+1)

f(int(input()))