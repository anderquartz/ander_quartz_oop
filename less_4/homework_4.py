from datetime import datetime

# 1. Создай класс SecureData, который:
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"

# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def get_secret(self):
        return self.__secret

    def __setattr__(self, key, value):
        if key == 'token':
            raise AttributeError("ошибка атрибута")
        object.__setattr__(self, key, value)

data = SecureData("пароль123")
# print(data.__secret)
# print(data.get_secret())


data.other = "ok"
print(data.__dict__)
# data.token = "abc123" ❌ AttributeError



# 3. Создай класс SafeDict, в котором:
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"

class SafeDict:
    def __getattr__(self, name):
        return "N/A"

    def __delattr__(self, name):
        print(f"Удален атрибут '{name}'")
        object.__delattr__(self, name)

d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"


# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError
        self.__salary = value

    @salary.deleter
    def salary(self):
        print("зарплата удалена")
        del self.__salary


e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

print()

del e.salary
print(e.__dict__)


# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

class LoginForm:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.getter
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        print(f"[LOG] "
              f"username изменён ")
        self.__username = value

form = LoginForm("")
form.username = "admin"  # выводит лог
print(form.username)     # "admin"


# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.

class Card:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return f"**** **** **** {self.__number[-4:]}"

    @number.setter
    def number(self, value):
        if len(value) != 16+3:
            raise ValueError
        self.__number = value

    @number.deleter
    def number(self):
        print(f"[LOG]"
              f"удаление номера '{self.__number}' "
              f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        del self.__number

card = Card('')
card.number = "1234 5678 9101 1213"
print(card.number)
# del card.number

assert card._Card__number == '1234 5678 9101 1213'
assert card.number == '**** **** **** 1213'


# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.


class UserData:
    def __init__(self,
                 email: str,
                 age: int,
                 is_active: bool):
        self.email = email
        self.age = age
        self.is_active = is_active

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, mail):
        if not '@' in mail:
            raise ValueError("Нет собаки")
        self._email = mail

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Число меньше 18")
        self._age = age

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError('Может быть только булевым значением')
        self._is_active = value

    @property
    def json(self):
        return {
            'email': self._email,
            'age': self._age,
            'is_active': self._is_active
        }



user = UserData("test@mail.com", 20, True)
assert user.json == {'email': 'test@mail.com', 'age': 20, 'is_active': True}


try:
    UserData("test@mail.com", 15, True)
    assert False
except ValueError:
    pass


try:
    UserData("testmail.com", 20, True)
    assert False
except ValueError:
    pass