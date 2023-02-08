from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    csr = calculate_square_root(your_number)
    if your_number <= 0:
        return csr

    print(f'Мы вычислили квадратный корень'
          f' из введённого вами числа. '
          f'Это будет: {csr}')


print(message)
calc(25.5)
