# Калькулятор
import math
y = True
n = False
con = "y"
while con == "y":
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
    elif what == "*":
        c = a * b
        print("Результат: " + str(c))
    else:
        print("Выбрана неверная операция!")
    con = input("Для продолжения работы введите 'y' " + "или введите 'n' для окончания работы: ")
print("Конец работы")
