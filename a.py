n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
index = 0
g = 0

for i in range(n):
    step = a[index] #элемент массива становится шагом. Вначале шаг=первый элемент
    
    if step==0: #если шаг=0, значит ему некуда двигатся. Нужно взять элемент до 0
        index-=g #берется на один элемент до 0
        
        step=a[index] #шагу присвается элемент до 0
        
        if index==0: #если элементов до 0 не осталось значит до конца дойти не получится
            print('no')
            break
        g+=1
        
    index +=step #цикл движется по элементам с шагом
    
    if index>=n-1:
        print('yes')
        break
    