# lambda, map
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

# summa = 0
# num = input("Введите число: ")
# for i in range(len(num)):
#     if num[i].isdigit():
#         summa += int(num[i])
# print(f"Сумма цифр в числе = {summa}")

summa = sum(list(map(lambda a: int(a) if a.isdigit() else 0, input("Введите число: "))))
print(f"Сумма цифр в числе = {summa}")
