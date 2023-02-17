def numbers(n):
    if n != 1:
        numbers(n-1)
    print(n, end = ' ')

numbers(int(input()))