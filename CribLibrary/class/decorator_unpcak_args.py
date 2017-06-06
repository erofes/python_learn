# -*- coding: utf-8 -*-
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()
# Передали ли мне что-нибудь?:
# ()
# {}
# Python is cool, no argument here.


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)
# Передали ли мне что-нибудь?:
# (1, 2, 3)
# {}
# 1 2 3


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))


function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
# Передали ли мне что-нибудь?:
# ('Билл', 'Линус', 'Стив')
# {'platypus': 'Определенно!'}
# Любят ли Билл, Линус и Стив утконосов? Определенно!


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))


m = Mary()
m.sayYourAge()
# Передали ли мне что-нибудь?:
# (<__main__.Mary object at 0x028919F0>,)
# {}
# Мне 28 лет, а ты бы сколько дал?