# 1. Создай класс Circle, в котором:
# есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
# метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
# Проверь результат вызова:
# print(Circle.is_valid_radius(500))   # True
# print(Circle.is_valid_radius(1500))  # False

# 2. Добавь в класс Circle:
# статический метод area(radius),
# который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
# инициализацию в __init__, которая сохраняет радиус,
# только если он проходит валидацию через метод is_valid_radius()
# (подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
# Пример:
# c = Circle(10)
# print(c.area(c.radius))  # Площадь круга

# 3. Расширь Circle, добавив обычный метод print_info, который выводит:
# Радиус: ...
# Допустимый диапазон: [MIN, MAX]
# Метод должен использовать и self, и атрибуты класса через type(self).
# Пример вызова:
# c.print_info()

from math import pi

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * radius ** 2

    def print_info(self):
        print("Радиус: ", self.radius)
        print("Допустимый диапазон: ", [type(self).MIN_RADIUS, type(self).MAX_RADIUS])

print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))

print()

c = Circle(10)
print(c.area(c.radius))

print()

c.print_info()

print()

# 4. Создай класс User, в котором:
# приватные атрибуты __login и __password;
# метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
# метод get_credentials(), который возвращает кортеж из логина и пароля.
# Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.

class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = password

    def get_credentials(self):
        return self.__login, self.__password

user1 = User("Keker", 123)

user1.login = "kekerrrrr" # dont work
print(user1.get_credentials())

user1.set_credentials("Kekerboy", "")
print(user1.get_credentials())

