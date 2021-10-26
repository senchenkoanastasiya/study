import random
a = []
digit = 8
for i in range(10):
    a.append(random.randint(0,10))
print(a)
print(f'Число {digit} находится в списке под номером {a.index(digit)}')