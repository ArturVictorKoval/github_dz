#import modulya random
import random
#sozdayu spisok 4isel
c = list(range(0, 100))
#sozdayu slu4aynue 4isla s mnogestvom elementov ot 3 do 10
for i in range(3,10):
    b = random.sample(c,i)
#vivogu polu4ennuy spisok
print(b)
#vuvodim ukazannue elementy
a = b[0],b[2],b[-2]
print(a)
