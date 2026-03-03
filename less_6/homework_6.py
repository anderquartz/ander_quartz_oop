# 1. Создай базовый класс Shape с методом area(), который возвращает 0.
# Отнаследуй два класса: Circle и Square.
# Переопредели метод area() так, чтобы он возвращал площадь круга или квадрата.
#
# c = Circle(5)
# s = Square(4)
#
# print(c.area())  # ~78.5
# print(s.area())  # 16
import math


class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        s = math.pi * self.radius**2
        return round(s, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(5)
s = Square(4)

print(c.area())  # ~78.5
print(s.area())  # 16


# 2. Создай базовый класс BasePage с методом open(url).
# Сделай добавь магический init, в котором указан текст на странице (любой)
# От него унаследуй LoginPage и добавь метод find(text).
# Проверь, что методы из базового класса тоже доступны:
# page = LoginPage()
# page.open("https://example.com/login")
# page.text("Зима")
# Вывод в консоли:
# На странице найден текст: "Зима"


class BasePage:
    def __init__(self, text):
        self.text = text

    def open(self, url: str):
        print(url)

class LoginPage(BasePage):
    def find(self, text):
        print('На странице найден текст: ', text)

page = LoginPage('Зима')                           #сделал не как в задании
page.open("https://example.com/login")
page.find("Зима")



# 3. Создай свой класс ResultList,
# который наследует list и добавляет метод success_count(),
# возвращающий количество успешных результатов (где item["status"] == "passed").
#
# results = ResultList([
#     {"status": "passed"},
#     {"status": "failed"},
#     {"status": "passed"},
# ])
#
# print(results.success_count())  # 2


class ResultList(list):
    def success_count(self):
        counter = 0
        for item in self:
            if item.get('status') == "passed":
                counter += 1
        return counter

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count())



# 4. Создай классы BaseStep и LoginStep, отнаследуй второй от первого.
#  Создай объект step = LoginStep()
#  Проверь, что он является экземпляром и LoginStep, и BaseStep, и object.
#
# print(issubclass(LoginStep, BaseStep))  # True
# print(isinstance(step, BaseStep))       # True
# print(isinstance(step, object))         # True


class BaseStep:
    pass

class LoginStep(BaseStep):
    pass

step = LoginStep()
print(issubclass(LoginStep, BaseStep))  # True
print(isinstance(step, BaseStep))       # True
print(isinstance(step, object))         # True



# 5. Создай класс ExtendedDict, который наследуется от dict,
# и переопредели __str__, чтобы словарь красиво выводился в формате:
# ключ: значение
# ключ: значение
# Пример:
# d = ExtendedDict(a=1, b=2)
# print(d)
# Ожидаемый вывод:
# a: 1
# b: 2


class ExtendedDict(dict):
    def __str__(self):
        lines = []
        for key, value in self.items():
            lines.append(f"{key}: {value}")
        return "\n".join(lines)                   # это было неожиданно и сложно, сам бы я не додумался, а в описании задания и подсказки не было

d = ExtendedDict(a=1, b=2)
print(d)



# 6. Создай два класса:
#
# Widget: принимает x, y и сохраняет как self.x, self.y;
# Button: наследует Widget, добавляет label, но обязательно вызывает super().
# Проверь, что всё сохраняется корректно.
#
# btn = Button(100, 200, "OK")
# print(btn.x, btn.y, btn.label)  # 100 200 OK


class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label)


# 7. Модифицируй Button, чтобы не вызывать super() вовсе.
# Что произойдёт? Проверь через print(btn.__dict__).

class Widget2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button2(Widget2):
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

btn = Button2(100, 200, "OK")
print(btn.x, btn.y, btn.label)
print(btn.__dict__) # Всё работает данные выдаются, но потенциально так лучше не делать из-за потенциальных ошибок


# 8. Создай классы:
# Logger — метод log(self, msg) просто печатает сообщение;
# HTMLLogger(Logger) — переопредели метод log.
# logger = HTMLLogger()
# logger.log("Login successful")
#
# Ожидаемый вывод (обрати внимание что выводится 2 строки:
# одна из log класса Logger, другая из log класса HTMLLogger):
# [LOG] Login successful
# <p>Login successful</p>



class Logger:
    def log(self, msg):
        print(f'[LOG] {msg}')

class HTMLLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print(f'<p>{msg}</p>')

logger = HTMLLogger()
logger.log("Login successful")