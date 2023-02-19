name = input().split('@')

if name[0].islower():
    print('Welcome')
else:
    raise ValueError('Чел ты...')