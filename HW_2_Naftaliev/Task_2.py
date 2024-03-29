# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать сумму и 
# произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction


a1, b1 = [int(i) for i in input("Введите первую дробь через/").split("/")]
a2, b2 = [int(i) for i in input("Введите вторую дробь через/").split("/")]
s = (a1 * b2 + a2 * b1) / (b1 * b2)
p = (a1 * a2) / (b1 * b2)
a = Fraction(a1, b1)
b = Fraction(a2, b2)
print(f"{s} = {a + b}, {p} = {a * b}")
