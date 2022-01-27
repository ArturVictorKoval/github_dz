"""Ваша задача — написать программу, которая переводит число во время
в читабельном виде.
Пользователь должен ввести число больше 0 и меньше 8639999.
Число необходимо перевести в день, часы, минуты и секунды.
Ну и дополнительной задачей является — забота о выводе.
Слово "день" подбирается на основе кол-ва дней, а часы, минуты и секунды должны заполняться
нулями при одноцифровых значениях.
Пример:
to_readable(0) -> 0 дней, 00:00:00
to_readable(224930) -> 2 дня, 14:28:50
to_readable(466289) -> 5 дней, 09:31:29
to_readable(8639999) -> 99 дней, 23:59:59"""
import datetime
from datetime import timedelta
t = int(input("Введите число: "))
if 0 > t or t > 8639999:
    print("Введите число от 0 до 8639999")
elif  t < 86400:
    a = timedelta(seconds=t)
    print("0 days ",a)
else:
    b = timedelta(seconds=t)
    print(b)
