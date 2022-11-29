import random


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def sum_nambers() -> int:
    """Сумма цифр вещественного числа"""

    try:
        number = float(input("Введите число: ").replace(',', '.'))
        if type(number) in [int, float]:
            a = [i for i in str(number)]
            a.remove('.')
            if str(number).endswith('.0'):
                str(number).replace('.0', '')
                print(f'- {str(number).replace(".0", "")} -> {sum(list(map(int, a)))}')
            else:
                print(f'- {number} -> {sum(list(map(int, a)))}')
    except ValueError:
        print('Введенное число должно быть либо целым, либо вещественным!')
        print('Повторите ввод!')
        return sum_nambers()


# sum_nambers()

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def products_of_numbers():
#     N = int(input('Введите целое число: '))
#     a = []
#     Factorial = 1
#     for i in range(1, N + 1):
#         Factorial = Factorial * i
#         a.append(Factorial)
#     Factorial = str(1)
#     b = []
#     b.append(Factorial)
#     for j in range(2, N + 1):
#         Factorial += '*' + str(j)
#         b.append(Factorial)
#     print(f'- пусть N = {N}, тогда {a} ({", ".join(b)})')
#
#
# # products_of_numbers()
#
# # Задайте список из n чисел последовательности (1+1/ n)^n и выведите на экран их сумму.
#
# def dict_comprehension() -> dict:
#     try:
#         n = int(input('Введите целое число >=0:'))
#         if n > 0:
#             dict = {k: round((1 + 1 / k) ** k, 2) for k in range(1, n + 1)}
#             print(f'- Для n = {n}: {dict} ')
#             return sum(dict.values())
#         return {}
#     except ValueError:
#         print('Вы ввели не целое число!')
#         print('Повторите ввод')
#         return dict_comprehension()
#
#
# # print(f'Сумма {dict_comprehension()}')
#
# # Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
#
# def products_of_numbers_on_index():
#     try:
#         N = int(input("Введите количество элементов в списке: "))
#         if type(N) in [int]:
#             list_of_numbers = [i for i in range(-N, N + 1) if i != 0]
#             print(f'В сгенерированном списке {len(list_of_numbers)} элементов\n'
#                   f'Введите индескы элеменов от 0 до {len(list_of_numbers)}')
#             element_index = list(map(int, (input("Введите индексы элементов списка через пробел: ").split())))
#             result = 1
#             for i in element_index:
#                 result *= list_of_numbers[i]
#             print(result)
#     except ValueError:
#         print("Количество элементов в списке должено быть целым числом!")
#         print("Повторите ввод!")
#         return products_of_numbers_on_index()
#
#
# # products_of_numbers_on_index()
#
#
# # Реализуйте алгоритм перемешивания списка.
#
# def list_shuffling() -> list:
#     list_shuf = [_ for _ in range(11)]
#     print(f'Исходный список: {list_shuf}')
#     random.shuffle(list_shuf)
#     print(f'Перемешанный список: {list_shuf}')
#
#
# list_shuffling()
print(ord('→'))
print(chr(8594))
print(ord('↑'))
print(chr(8593))
print(ord('←'))
print(chr(8592))
print(ord('↓'))
print(chr(8595))
