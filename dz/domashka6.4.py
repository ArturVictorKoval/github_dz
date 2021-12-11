# Калькулятор
import math
what = input("Выберите операцию (+,-,/,*): ")
a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "/":
    if b == 0:
        print("на ноль делить нельзя")
    else:
        c = a / b
        print("Результат: " + str(c))
elif what== "*":
    c = a * b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция!")
