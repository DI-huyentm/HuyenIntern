from info import MENU

class MenuItem:
    def __init__(self, name, cost,  ingredients:dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
    
    def __str__(self):
        return f"{self.name}"

class Menu:
    def __init__(self, menu:dict=MENU):
        menu_list =[]
        for item, info in menu.items():
            menu_item = MenuItem(
                name=item, #info["name"]
                cost=info["cost"],
                ingredients=info["ingredients"]
            )
            menu_list.append(menu_item)
        self.menu=menu_list
        
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                return item
        return None




