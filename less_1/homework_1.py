# """
# +++++++++++++++++++++++++++++++++++++++++
# Тема задания классы
# +++++++++++++++++++++++++++++++++++++++++
# Задание 1

# Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.


class Dog:
    """Класс для создания профиля собаки."""
    species = "canis"
    legs = 4

bruno = Dog()
bobik = Dog()

print(id(bruno))
print(id(bobik))

bobik.species = 'brodyaga'
bruno.legs = 5

print(id(bruno))
print(id(bobik))


print(bruno.__dict__)
print(bobik.__dict__)

# Задание 2

# Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.

print(Dog.__dict__)
print(Dog.__doc__)

bobik.name = 'bobik'
bobik.age = 5
del bobik.name
# print(bobik.name) ошибка, т.к. атрибута больше не существует


# Задание 3
# Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():

# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.


class User:
    role = "guest"
    active = True

setattr(User, "role", "admin")
print(User.__dict__)
print(getattr(User, 'active'))
setattr(User, "email", "228@mail.ru")
delattr(User, "role")
print(hasattr(User, 'role'))

print(User.__dict__)
