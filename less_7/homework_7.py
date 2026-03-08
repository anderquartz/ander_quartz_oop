# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.

class Cat:
    def speak(self, text):
        print(f"{text}: Кот")

class Dog:
    def speak(self, text):
        print(f"{text}: Пэс")

class Duck:
    def speak(self, text):
        print(f"{text}: Утка")

lst = [Cat(), Dog(), Duck()]

for animal in lst:
    animal.speak("Животное")


# 2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого.

class Shape:
    def get_pr(self):
        print('\nФигура:')

class Square(Shape):
    def get_pr(self):
        super().get_pr()
        print('Квадрат')

class Rectangle(Shape):
    def get_pr(self):
        super().get_pr()
        print('Прямоугольник')

class Triangle(Shape):
    def get_pr(self):
        super().get_pr()
        print('Треугольник')

pr = [Square(), Rectangle(), Triangle()]
for p in pr:
    p.get_pr()


# 3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
from abc import ABC, abstractmethod

class Shape2(ABC):
    @abstractmethod
    def get_pr(self):
        print('\nФигура:')

class Square2(Shape):
    def get_pr(self):
        super().get_pr()
        print('Квадрат')

class Rectangle2(Shape):
    def get_pr(self):
        super().get_pr()
        print('Прямоугольник')

class Triangle2(Shape):
    def get_pr(self):
        super().get_pr()
        print('Треугольник')


# pp = Shape2() #TypeError


# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.

class A:
    def __init__(self):
        pass

class B:
    def __init__(self):
        pass

class C:
    def __init__(self):
        pass

class D(A, B, C):
    def __init__(self):
        super().__init__()

print(D.__mro__)


# 5. Создай MixinLog (как в уроке).
# Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# Создай класс, который наследует оба класса. Создай экземпляр этого класса.
import datetime

class Hotel:
    def __init__(self, name, stars, price):
        super().__init__()
        print("init Hotel")
        self.name = name
        self.stars = stars
        self.price = price

    def reserv(self):
        print(f"Забронирован отель: {self.name}, {self.stars} звёзд за цену: {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"ID_брони: {self.id}, Время брони: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

class Gostinizza(Hotel, MixinLog):
    pass

Roza = Gostinizza("Rozalia", 5, 10000)
Roza.reserv()
Roza.save_sell_log()
print(Gostinizza.__mro__)

# 6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?

# Будет почти одно и то же что в 5 задании, если изменить порядок наследования - логика изменится, программа не сработает, потому что в миксин лог не передадутся переменные


# 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"

# 8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"

# 9. Модифицируй код так, чтобы после обработки конкретных ошибок
# был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# "Произошла неизвестная ошибка"

# 10. При перехвате исключений из 7 и 8 заданий,
# сохрани ошибку в переменную e и выведи её текст:

class input_num:
    def division(self):
        try:
            a = int(input("Введите число а: "))
            b = int(input("Введите число b: "))
            res = a / b
            print(f"Результат: {res}")
            return res
        except ZeroDivisionError:
            print("\nНа ноль делить нельзя!\n")
        # except ValueError:
        #     print("\nОшибка ввода: введите два числа через пробел!\n")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            print(f"Тип ошибки: {type(e).__name__}")



# nums = input_num()
# nums.division()


# 11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.

# 12. Запроси у пользователя два числа и выполни деление.
# Если деление прошло успешно без ошибок — выведи
# "Деление выполнено успешно" через (но не в блоке try)

# 13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления.

try:
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    res = a / b
    print(f"Результат: {res}")
except ArithmeticError:
    print("Арифметическая ошибка")
else:
    print("Деление выполнено успешно")
finally:
    print("Работа программы завершена")


# 14. Реализуй две вложенные конструкции:
# Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
# Внутренний try/except ловит деление на ноль.

try:
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    try:
        res = a / b
        print(f"Результат: {res}")
    except ZeroDivisionError:
        print("\nНа ноль делить нельзя!\n")
except ValueError:
    print("Ошибка типа!")


# 15. Вынеси обработку деления в отдельную функцию divide(x, y)
# с собственным try/except.
# Во внешнем коде обработай только ошибку ввода.

def divide():
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    try:
        res = a / b
        print(f"Результат: {res}")
    except ZeroDivisionError:
        print("\nНа ноль делить нельзя!\n")

try:
    divide()
except ValueError:
    print("Ошибка типа!")