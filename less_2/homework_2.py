# 1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
# Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
# Создай два объекта и задай им разные значения. Выведи информацию по каждому.

class Person:

    def set_data(self, name, age):
        self.name = name
        self.age = age


    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

bobik = Person()
bobik.set_data('Vasya', 5)

taburetka = Person()
taburetka.set_data('Valera', 15)

print(bobik.get_data())
print(taburetka.get_data())

print()

# 2. Добавь в класс Point методы set_coords(x, y) и get_coords().
# Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
# После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().

class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
print(p.get_coords())

print()

# 3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
# Проверь, что результат совпадает с обычным вызовом p.get_coords().

metod = getattr(p, 'get_coords')
print(metod())

p.get_coords()
print(p.get_coords())

print()

# 4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
# Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.

# 5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
# где <имя> — значение поля name. Создай и удали объект вручную с помощью del.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def __del__(self):
        print(f'Удалён объект: {self.name}')

objj = Person('Petr', 22)
print(objj.show_info())

objj2 = Person('Vova', 18)
del objj2

print()

# 6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
# Добавь метод area(), который возвращает площадь прямоугольника.
# Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.

class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

a = Rectangle(2, 4)
print(a.area())

b = Rectangle()
print(b.area())

print()

# 7. Создай класс Logger, который всегда возвращает один и тот же объект.
# При создании экземпляра в __new__ выводи Создание логгера,
# а при вызове __init__ — Инициализация логгера.

class Logger:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print('Создание логгера')
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print('Инициализация логгера')


a = Logger()
b = Logger()