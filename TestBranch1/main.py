from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from info import MENU, resources

menu_today = Menu()
machine1 = CoffeeMaker()
money1= MoneyMachine()


resources["profit"] = 0

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        machine1.report()
    else:
        find = menu_today.find_drink(choice)
        if (find != None):
            suff = machine1.is_resource_sufficient(choice)
            if suff :
                pay = money1.make_payment(MENU[choice]["cost"])
                if pay:
                    resources["profit"] += MENU[choice]["cost"]
                    machine1.make_coffee(choice)
                    print(f"Here is your {choice} ^3^ Enjoy!")                          
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough resource")
        else:
            print("Cant find. We dont have it here")
        
                
            

            