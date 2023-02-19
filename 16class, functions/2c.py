def ispower2(n):
    if n==1:
        return 'Yes'
    elif n%2==1:
        return 'No'
    else:
        return ispower2(n/2)


print(ispower2(int(input())))