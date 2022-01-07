"""Для массива целых чисел нужно найти сумму элементов с четными
индексами [0-й, 2-й, 4-й итд],затем перемножить эту сумму
на последний элемент исходного массива.
Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 [ноль].
[0, 1, 2, 3, 4, 5] => (0 + 2 + 4) * 5 = 30
[1, 3, 5] => 30
[6] => 36
[] => 0"""
#import modulya random
import random
#sozdayu spisok 4isel
c = list(range(0, 10))
#sozdayu slu4aynue 4isla s mnogestvom elementov ot 3 do 10
for i in range(0,10):
    b = random.sample(c,i)
print("massiv 4isel : ",b)
d = b[::2]
print("4isla s 4etnym indeksom : ",d)
e = b[-1]
print("4islo s poslednym indeksom : ",e)
for num in d:
    g = sum(b[::2]*e)
if d == [] in d:
    print(0)
else:
    print(g)

