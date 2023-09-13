from info import resources

class MoneyMachine:
    def report(self):
        print(f'${resources["profit"]}')

    def make_payment(self, cost:float):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) 
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        change =  round( quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01 - cost , 2)
        if change > 0:
            print(f"Here is ${change} in change")
            return True
        elif change ==0:
            return True    
        else:
            return False
        

