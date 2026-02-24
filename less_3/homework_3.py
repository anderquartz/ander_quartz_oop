# 1. Создай класс Circle, в котором:
# есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
# метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
# Проверь результат вызова:
# print(Circle.is_valid_radius(500))   # True
# print(Circle.is_valid_radius(1500))  # False



class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))

