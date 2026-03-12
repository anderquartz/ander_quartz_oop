# 1. Создай две функции: inner() и outer().
# В inner() вызови деление на ноль.
# В outer() просто вызови inner().
# Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
from datetime import time
from symtable import Class


def inner():
    return 10/0

def outer():
    inner()

outer()
#сначала ошибка где вызывается метод outer, потом в самой функции, и только потом уже в inner где деление на ноль


# 2. Добавь вокруг вызова outer() конструкцию try/except,
# чтобы перехватить исключение и вывести сообщение
# "Ошибка перехвачена на верхнем уровне".

def inner():
    return 10/0

def outer():
    inner()


try:
    outer()
except ZeroDivisionError:
    print("Ошибка перехвачена на верхнем уровне")


# 3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
# В случае ошибки возвращай строку "Ошибка в inner".

def inner():
    try:
        return 10/0
    except ZeroDivisionError:
        print("Ошибка в inner")

def outer():
    inner()

outer()



# 4. Сделай так:
# В inner() ошибка не перехватывается.
# В outer() ошибка перехватывается через try/except.
# В outer() при перехвате напечатай "Ошибка в outer".

def inner():
    return 10/0

def outer():
    try:
        inner()
    except ZeroDivisionError:
        print("Ошибка в outer")

outer()


# 5. Напиши функцию get_value(), которая кидает ValueError.
# Напиши тестовую функцию test_get_value(), которая:
# Вызывает get_value();
# Ловит ValueError;
# Завершает тест с assert False, если исключение поймано.


def get_value():
    raise ValueError

def test_get_value():
    try:
        get_value()
    except ValueError:
        print('Ошибка ValueError')
    # assert False, "Исключение поймано"

test_get_value()


# 6. Создай функцию divide(x, y).
# Если y == 0, выбрасывай ZeroDivisionError через raise.
# Иначе возвращай результат деления.

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    print('x / y = ', x / y)
    return x / y

divide(1, 2)

import math

# 7. Создай функцию sqrt(x), которая:
# Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
# Иначе возвращает квадратный корень из x.
# Проверь поведение функции через try/except.

def sqrt(x):
    if x < 0:
        raise NegativeNumberError
    else:
        print(math.sqrt(x))
        return math.sqrt(x)

class NegativeNumberError(Exception):
    """негативное число"""

sqrt(5)



# 8. Создай базовый класс MathError.
# От него унаследуй:
# NegativeNumberError
# DivisionByZeroError
# В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
# Проверь в try/except обработку ошибок через базовый класс MathError.

class MathError(Exception):
    pass


class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Деление на ноль")
    print('x / y = ', x / y)
    return x / y

try:
    safe_divide(1, 0)
except MathError as e:
    print("Поймана ошибка:", e)



# 9. Создай тестовую функцию test_sqrt(), которая:
# вызывает sqrt(x) с отрицательным числом;
# перехватывает NegativeNumberError;
# завершает тест с assert False и сообщением
# "Нельзя брать корень из отрицательного числа".

def test_sqrt(x):
    try:
        sqrt(x)
    except NegativeNumberError as e:
        print("Поймана ошибка:", e)
        assert False, "Нельзя брать корень из отрицательного числа"


test_sqrt(5)


# 10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
# Обеспечь закрытие файла через with.

with open("sample.txt", encoding='utf-8') as f:
    # for line in f:
    #     print(line, end="")
    content = f.read()
    print(content)


# 11. Создай класс BackupList, который:
# делает копию списка при входе в with,
# при выходе сохраняет изменения, если ошибок не было,
# откатывает изменения при ошибке.
# Проверь:
# успешное изменение списка;
# откат при ошибке.

class BackupList:
    def __init__(self, original):
        self.original = original
        print("Оригинал списка: ", self.original)
        pass

    def __enter__(self):
        self.backup = self.original.copy()
        print('Копирование списка')
        return self.backup

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original[:] = self.backup[:]
            print("Изменения сохранены")
        else:
            print("Ошибка! Откат изменений")
        return False

data = [1337, 228, 322]
with BackupList(data) as lst:
    lst.append(666)
print(data)



try:
    with BackupList(data) as lst:
        lst.append(4)
        raise ValueError("Ошибка")
except ValueError:
    print("Поймали ошибку")
print(data)


# 12. Создай декоратор-класс Timer,
# который измеряет время выполнения функции и выводит результат.
import datetime
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = datetime.datetime.now()
        result = self.func(*args, **kwargs)
        end_time = datetime.datetime.now()
        full_time = end_time - start_time
        print("Время выполнения функции: ", full_time)
        return result

@Timer
def test_example():
    print("Выполняется функция...")
    time.sleep(3)

test_example()