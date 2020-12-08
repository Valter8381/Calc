"""
Калькулятор ver 2
"""

# TODO изучить pep8
# TODO изучить flake8
# TODO почитать docstring
# TODO почитать docstring
# TODO заменить все ковычки на одинарные
# TODO убрать всю табуляцию заменить на точки/пробелы 4
# TODO строки складываються через format или f строки
# TODO по pep8 в конце файла всегда перенос строки
# TODO убрать все лишние символы в конце любой строки
# TODO по возможности переделать работу на фукнцию

from colorama import init
from colorama import Fore
from colorama import Back
# from colorama import Style


# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)  # noqa
print(Back.GREEN)

what = input("Что делаем? (+,-):")

print( Back.CYAN )

a = float(input("Введи первое число:") )
b = float(input("Введи второе число:") )

print( Back.YELLOW )  # noqa

if what == "+":
    c = a + b
    print("Результат: {}".format(
        str(c)
    )
elif what == "-":
	c = a - b
	print("Результат: " + str(c))		 
else:
    print("Выбрана неверная операция!")	

input()