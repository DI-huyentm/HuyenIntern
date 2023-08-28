from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine(menu)
money_machine.report()

coffe_maker = CoffeeMaker(menu)
coffe_maker.report()
