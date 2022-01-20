"""Пользователь вводит строку, Ваша задача — преобразовать строку в hashtag.
Парочка правил:
никаких символов из набора string.punctuation быть не должно, в том числе и пробелов;
длина должна быть не более 140 символов.
Если последнее правило нарушено - обрезать итоговую строку до 140 символов.
Примеры:
'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes"""
import string
a = input("")
b = str.maketrans(dict.fromkeys(string.punctuation))
c=a.translate(b)
d=c.title()
e=d.replace(' ', '')
print("#"+e[:139])
