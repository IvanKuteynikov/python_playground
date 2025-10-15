from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu_today = Menu()
cashier = MoneyMachine()
use_machine = True

def validate_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Please enter {" or ".join(valid_options)}")

print("Coffee maker at your disposal")
while use_machine:
    users_choice = validate_user_input(f"What do you want to order, today? We have: {", ".join(menu_today.get_items()[0:3])} ", menu_today.get_items())
    while users_choice == 'report':
        machine.report()
        cashier.report()
        users_choice = validate_user_input("Do you want anything else? (Y,N) ", ['y','n'])
        if users_choice == 'y':
            break
        else:
            print("Goodbye")
            use_machine = False
    if use_machine == False:
        break
    if users_choice == 'y':
        users_choice = validate_user_input(f"What do you want to order, today? We have: {", ".join(menu_today.get_items()[0:3])} ", menu_today.get_items())
    ordered = menu_today.find_drink(users_choice)
    can_make = machine.is_resource_sufficient(ordered)
    if can_make == False:
        users_choice = validate_user_input("Do you want anything else? (Y,N) ", ['y','n'])
        if users_choice == 'n':
            break
        else:
            continue
    print(f"Your order is {ordered.name}, cost is ${ordered.cost}")
    cashier.make_payment(ordered.cost)
    machine.make_coffee(ordered)
    users_choice = validate_user_input("Do you want anything else? (Y,N) ", ['y','n'])
    if users_choice == 'n':
        print("Goodbye")
        use_machine = False
    

