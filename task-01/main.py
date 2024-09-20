# Самостоятельная работа №1


# Задача №1. Куб

def make_cube(n):
    return n ** 3


# Задача №2. Повторение

def repeat(n):
    if isinstance(n, str):
        return n * 3
    return str(n) * 2


# Задача №3. Возведение в степень
def create_powers(*args, power=2):
    return [n ** power for n in args]


# Задача №4. Разворот числа
def reverse_number(n):
    result = 0
    while n > 0:
        d = n % 10
        result = result * 10 + d
        n = n // 10
    return result


# Задача №5*. Рекурсия (задача со звёздочкой)

def fac(n):
    if n < 2:
        return 1
    return n * fac(n - 1)


