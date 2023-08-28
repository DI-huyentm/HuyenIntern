from info import MENU

class MenuItem:
    def __init__(self, name:str, ingredients:dict, cost:float):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

menu_item1 = MenuItem(name="espresso", ingredients={"water": 50,"milk": 0,"coffee": 18}, cost = 1.5)
menu_item2 = MenuItem(name="latte", ingredients={"water": 200,"milk": 150,"coffee": 24}, cost = 2.5)
menu_item3 = MenuItem(name="cappuccino", ingredients={"water": 250,"milk": 100,"coffee": 24}, cost = 3.0)

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

class Menu:
    def get_items(self):
        options = ""
        for key in MENU:
            options += f"{key}/"
        return options
    
    def find_drink(self, order_name:str):
        for key in MENU:
            if order_name == f"{key}":
                return MENU[key]           
        return None
    








