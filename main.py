# print(type(1))
# print(type(1.1))
# print(type("1"))
# print(type([1]))
# print(type((1,)))
# print(type({1}))
# print(type({1:1}))
# print(type(min))

""" Свойства и методы классов

    Свойства - переменные которые находятся внутри класса
    Метод - функции которые находятся внутри класса
    
"""

# class Apple:
#     form = "Круглая"
#     color = "Цвет"
#     taste = "Сладкий"
#
# print(Apple.form)
# print(Apple.color)
# print(Apple.taste)

# class Car:
#     color = "blue"
#     marka = "Lada"
# print(Car.color)
# print(Car.marka)
# print(f"Моя машина {Car.color} цвета и марки {Car.marka}")


# class Person:
#     name = "Вася"
#     time = 15
# print(f"Меня зовут {Person.name} и я заканчиваю работать в {Person.time}")


# class Number:
#     num1 = 5
#     num2 = 10
#     print(num1+num2)
#
# print(Number.num1 + Number.num2)

# class Backpack:
#     things = ["Хомяк","капустка","фонарик","шапка Пикачу","игрушечный меч майнкрафт"]
# for i in Backpack.things:
#     print(i)


# class Apple:
#     color = "red"
#
# apple1 = Apple()
# apple2 = Apple()
# apple3 = Apple()
#
# print(apple1.color)
# print(apple2.color)
# print(apple3.color)

class Person:
    name = "Vasya"
id_1 = Person()
print(id_1.name)