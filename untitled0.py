# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m8mUMyW4Z4MI34dIBk4MxtwKQmTIjpQ1
"""

a = 5
print("Введите число B:")
b=int(input())
c=a*b
print("C:")
print(a,b,c)

print("Введите число А:")
a = int(input())
print("Введите число B:")
b=int(input())
c=(a+b)**2
print("C:")
print(a,b,c)

a = 15
b=10
print("Введите число C:")
c=int(input())
d=(a+b)/c
print("D:")
print(a,b,c,d)

print("Введите число А:")
a = int(input())
print("Введите число B:")
b=int(input())
c=a**2+2*a*b+b**2
print("Формула суммы квадратов:")
print(a,b,c)

print("Введите число А:")
a = int(input())
print("Введите число B:")
b=int(input())
c=a//b
d=a*b
f=a%b
print("Деление двух чисел без остатка:")
print(c)
print("умножение двух чисел:")
print(d)
print("получение остатка от деления двух чисел :")
print(f)

print("Здравствуйте!")
print("Введите номер месяца:")
a=int(input())
if a==1 :
   print("Январь.")
elif a==2:
  print("Февраль.")
elif a==3:
  print("Март.")
elif a==4:
  print("Апрель.")
elif a==5:
  print("Май.")
elif a==6:
  print("Июнь.")
elif a==7:
  print("Июль.")
elif a==8:
  print("Август .")
elif a==9:
  print("Сентябрь.")
elif a==10:
  print("Октябрь.")
elif a==11:
  print("Ноябрь.")
elif a==12:
  print("Декабрь.")
else:
  print("Такого месяца нету. Идите в школу) ")

print("Введите число:")
a=int(input)