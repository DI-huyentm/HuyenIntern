from info import resources, MENU
from menu import Menu

# menu_today = Menu()

class CoffeeMaker:
    def report(self):        
        print(resources)
    
    def is_resource_sufficient (self, drink:str):
        # find = menu_today.find_drink(drink)
        # if find != None:
        for key in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][key] <= resources[key]:
                return True
            else:
                return False

    def make_coffee(self, order:str):
        for key in MENU[order]["ingredients"]:
            resources[key] -= MENU[order]["ingredients"][key]