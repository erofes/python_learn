# -*- coding: utf-8 -*-
def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    # Вернём эту функцию
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


stand_alone_function()
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?
# А я - код, срабатывающий после

# Наверное, теперь мы бы хотели, чтобы каждый раз, во время вызова
# stand_alone_function, вместо неё вызывалась stand_alone_function_decorated.
# Для этого просто перезапишем stand_alone_function:
stand_alone_function = my_shiny_new_decorator(stand_alone_function)
stand_alone_function()


# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?
# А я - код, срабатывающий после

# Синтаксис декораторов
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


another_stand_alone_function()


# Я - код, который отработает до вызова функции
# Оставь меня в покое
# А я - код, срабатывающий после

def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# --ветчина--
sandwich = bread(ingredients(sandwich))
sandwich()


# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

# Синтаксис декораторов
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

# Другое следование
@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)

sandwich()
# #помидоры#
#
# --ветчина--
# <\______/>
# ~салат~