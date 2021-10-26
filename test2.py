import random

def replacing_list():
    a = []
    for i in range (20):
        a.append(random.randint(1,20))
    print(a)

    n=int(input('Введите число от 0 до 10'))
    a[n]=n
    print(a)
replacing_list()