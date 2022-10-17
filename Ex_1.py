# list comprehension
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# num = [1.1, 1.2, 3.1, 5, 10.01]
# fractional = []
# for i in num:
#     if i % 1 > 0:
#         fractional.append(round(i % 1, 4))
# print(max(fractional) - min(fractional))

num = [1.1, 1.2, 3.1, 5, 10.01]
fractional = [round(i % 1, 4) for i in num if i % 1 > 0]
print(max(fractional) - min(fractional))
