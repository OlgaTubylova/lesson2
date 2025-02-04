# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

fraction1 = input("Введите первую дробь (a/b): ")
fraction2 = input("Введите вторую дробь (a/b): ")

frac1 = Fraction(fraction1)
frac2 = Fraction(fraction2)

sum_fractions = frac1 + frac2
product_fractions = frac1 * frac2

print(f"Сумма дробей: {sum_fractions}")
print(f"Произведение дробей: {product_fractions}")