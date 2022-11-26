# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# def sum_nambers() -> int:
#     """Сумма цифр вещественного числа"""
#
#     try:
#         number = float(input("Введите число: ").replace(',', '.'))
#         if type(number) in [int, float]:
#             a = []
#             for i in str(number):
#                 a.append(i)
#             a.remove('.')
#             if str(number).endswith('.0'):
#                 str(number).replace('.0', '')
#                 print(f'- {str(number).replace(".0", "")} -> {sum(list(map(int, a)))}')
#             else:
#                 print(f'- {number} -> {sum(list(map(int, a)))}')
#     except ValueError:
#         print('Введенное число должно быть либо целым, либо вещественным!')
#         print('Повторите ввод!')
#         return sum_nambers()
#
#
# sum_nambers()

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def products_of_numbers():
    N = int(input('Введите целое число: '))
    a = []
    Factorial = 1
    for i in range(1, N + 1):
        Factorial = Factorial * i
        a.append(Factorial)
    Factorial = str(1)
    b = []
    b.append(Factorial)
    for j in range(2, N + 1):
        Factorial += '*' + str(j)
        b.append(Factorial)
    print(f'- пусть N = {N}, тогда {a} ({", ".join(b)})')


# products_of_numbers()

# Задайте список из n чисел последовательности (1+1/ n)^n и выведите на экран их сумму.

def dict_comprehension() -> dict:
    try:
        n = int(input('Введите целое число >=0:'))
        if n > 0:
            dict = {k: round((1 + 1 / k) ** k, 2) for k in range(1, n + 1)}
            print(f'- Для n = {n}: {dict} ')
            return sum(dict.values())
        return {}
    except ValueError:
        print('Вы ввели не целое число!')
        print('Повторите ввод')
        return dict_comprehension()


# print(f'Сумма {dict_comprehension()}')
