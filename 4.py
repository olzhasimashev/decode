from random import randint

print("Определение абонента телефона. Введите номер в числовом формате")
print("Введите свой номер:")
a=(int(input()))%10000000000//10000000
print("Ваш абонент:")
if a==727:
    print("activ")
elif a==700 or a==708:
    print("altel")
elif a==705 or a==771 or a==776 or a==777:
    print("beeline")
elif a==701 or a==702 or a==775 or a==778:
    print("kcell")
elif a==707 or a==747:
    print("tele2")
else:
    print("inappropriate")