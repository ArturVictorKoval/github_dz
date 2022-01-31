"""
Ваша задача — написать функцию, которая будет проверять, является ли
предложение палиндромом. Палиндромом — предложение, которое читается
одинаков слева на право и справа налево.
Пример:
is_palindrome('A man, a plan, a canal: Panama') -> True
is_palindrome('0P') -> False
is_palindrome('a.') -> True
"""
import string
a = str(input(""))
def palindrome(a):
    b = str.maketrans(dict.fromkeys(string.punctuation))
    a = a.translate(b)
    a = a.replace(' ', '')
    a = a.lower()
    if a != a[::-1]:
        return ('False')
    else:
        return ('True')
print(palindrome(a))