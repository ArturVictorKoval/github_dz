"""
Написать программу, которая перемещает все нули в конец списка.

Ваша задача — изменить список так, что бы нули оказались в конце списка.

Порядок ненулевых чисел должен сохранится.
"""
a = [1,2,0,4,6,9,0,2,0,4,0,9]
for x in a:
    if x == 0:
        a.remove(0)
        a.append(0)
print(a)