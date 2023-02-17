# -*- coding: utf-8 -*-
"""Hometask#1_IG.py
Дом. задание №1

1.1. Написать цикл для выведения на экран каждой буквы своего ФИО
"""

first_name = input("Ваше имя: ")
middle_name = input("Ваше отчество: ")
last_name = input("Ваша фамилия: ")
a = last_name + first_name + middle_name 
for i in range(len(a)):
   print(a[i])

"""1.2. Написать функцию для перевода доллара (U$D) в евро (Euro) c округлением до 2х знаков после запятой,                               
если известно, что текущий курс составляет 1.17 долларов за один евро."""

def currency_exchange(usd):
    ref1 = usd/1.17
    return ref1
def exchange_rate_rub(usd):
    ref2 = usd*74.79  # курс рубля к доллару США на 17.02.23
    return ref2
usd = float(input("Ввести сумму в долларах США: "))

print("Сумма перевода в Euro = ",'{:.2f}'.format(currency_exchange(usd)))
print("Сумма перевода в Рублях (по курсу ЦБ РФ) = ",'{:.2f}'.format(exchange_rate_rub(usd)))