name = input()

if name.count('@') == 1:
    print('Welcome')
else:
    raise ValueError('Чел ты...')