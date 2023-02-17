name = input()

if name.istitle():
    print('Welcome')
else:
    raise ValueError('Чел ты...')