# enumerate, list comprehension
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def odd_sum(numbers_list):
#     buf = 0
#     for i in range(1, len(numbers_list), 2):
#         buf += numbers_list[i]
#     return buf


def odd_sum(numbers_list):
    return sum([j for i, j in enumerate(numbers_list, start=1) if not i % 2])


arr = [2, 3, 5, 9, 3]
summa = odd_sum(arr)
print(summa)
