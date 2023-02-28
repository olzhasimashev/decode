import os

name = input()

try:
    os.remove(name)
    print("Файл {} удален".format(name))
except Exception as e:
    print("Файл {} не найден".format(name))