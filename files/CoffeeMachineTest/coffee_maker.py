
from info import resources
from menu import Menu, MenuItem

class CoffeeMaker:
    def __init__(self, menu, res:dict=resources):
        self.menu = menu
        self.resources = res

    def report(self):
        print(self.resources)

    def is_resource_sufficient(self, drink):
        choice = self.menu.find_drink(drink)
        if choice:
            for key, value in choice.ingredients.items():
                if value > self.resources[key]:
                    return False
            return True
        return False
    
    resources["profit"] = 0


    def make_coffee(self, order:MenuItem):
        make = self.is_resource_sufficient(order.name)
        if make :
            for key, value in order.ingredients.items():
                self.resources[key] -= value
            
            self.resources["profit"] += order.cost

           

        
# menu = Menu()
# item1 = menu.menu[0]
# cfm = CoffeeMaker(menu)
# # cfm.report()
# # cfm.make_coffee(item1)
# # cfm.report()
