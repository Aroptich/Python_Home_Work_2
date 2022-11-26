
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def sum_nambers() -> int:
    """Сумма цифр вещественного числа"""

    try:
        number = float(input("Введите число: ").replace(',', '.'))
        if type(number) in [int, float]:
            a = []
            for i in str(number):
                a.append(i)
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


sum_nambers()