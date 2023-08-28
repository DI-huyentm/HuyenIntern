
from menu import Menu, MenuItem
from coffee_maker import resources
from coffee_maker import CoffeeMaker

class MoneyMachine:
    #print the current profit
    def __init__(self, menu):
        self.menu = menu
    
    def report(self):
        print(f'${resources["profit"]}')

    def make_payment(self, cost):
        if money_in 


# menu = Menu()
# item1 = menu.menu[1]
# item0 = menu.menu[0]
# cfm = CoffeeMaker(menu)
# mm = MoneyMachine(menu)
# # cfm.report()
# cfm.make_coffee(item1)
# cfm.make_coffee(item0)
# mm.report()
