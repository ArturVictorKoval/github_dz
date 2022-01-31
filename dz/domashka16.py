"""Написать функцию, которая представит человека 
по переданным параметрам.
Входные данные: Два аргумента строка(str) и положительное число(int)
Функция должна вернуть строку.
say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
"""

def represent():
    name = input("Hi, write your name, please: ")
    age = input("write your age, please: ")
    a = ("Hi. My name is " + name + " and I'm " + age + " years old")
    return a
print(represent())
