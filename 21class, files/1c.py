name = input()
format = input()

file = open("{}.{}".format(name, format), "w")

file.close()

print("Файл {}.{} создан".format(name, format))