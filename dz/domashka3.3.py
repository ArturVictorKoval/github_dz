import math
list = int(input("введите пятизначное число"))
x, y = divmod(list, 1000)
w, z = divmod(y, 100)
c, d = divmod(z, 10)
a, b = divmod(x, 10)
print(d,c,w,b,a)
