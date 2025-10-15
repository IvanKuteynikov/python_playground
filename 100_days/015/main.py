from data import menu_data, initial_capacity, quarters, dimes, nickels, pennies
from art import logo

machine = initial_capacity.copy()
continue_to_use_machine = True

def validate_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Please enter {" or ".join(valid_options)}")

def drinks_to_choose():
    """Here we provide list of available drinks to choose for the customer and special service report"""
    x = 1
    for drinks in menu_data:
        print(f"({x}) {drinks} ${menu_data[drinks]["cost"]}")
        x += 1
            

def check_machine(choosen_drink):
    """Is there enough ingridients"""
    status_ingridients = []
    what_is_absent = []
    for c in machine:
        for i in menu_data[choosen_drink]["ingridients"]:
            if c == i:
                if machine[c] < menu_data[choosen_drink]["ingridients"][i]:
                    what_is_absent.append(c)
                    status_ingridients.append(-1)
                else:
                    status_ingridients.append(0)
    return sum(status_ingridients), what_is_absent

def money_count(cost_of_drink, drink):
    quarters_q = 0
    dimes_q = 0
    nickels_q = 0
    pennies_q = 0
    total_paid = 0
    while cost_of_drink > total_paid:
        try:
            quarters_q += int(input("How many quarters? ($0.01) "))
            dimes_q += int(input("How many dimes? $0.10) "))
            nickels_q += int(input("How many nickels? ($0.05) "))
            pennies_q += int(input("How many pennies? ($0.25) "))
            total_paid = quarters_q * quarters + dimes_q * dimes + nickels_q * nickels + pennies_q * pennies
            if total_paid < drink_cost:
                print(f"It's not enough, please add ${round(cost_of_drink-total_paid,2)}")
                continue
        except ValueError:
            print("Please enter number!")
    change = round(total_paid - cost_of_drink, 2)
    if change > 0:
        print(f"Thanks! Here is your change: ${change}")
    print(f"Thanks, enjoy your {drink}!")
    return total_paid


while continue_to_use_machine:
    print(logo)
    drinks_to_choose()
    users_choice = validate_user_input("What do you want to drink? ",['1','2','3',"report"])
    while users_choice == 'report':
        print("Here is your report, boss:")
        for i in machine:
            print(f"{i} = {machine[i]}")
        want_to_order = validate_user_input("Want do order something? ", ['yes','no'])
        if want_to_order == 'yes':
            break
        else:
            print("Thanks and goodbye!")
            continue_to_use_machine = False
            break
    if continue_to_use_machine == False:
        break
    if users_choice not in ['1','2','3']:
        users_choice = int(validate_user_input("What do you want to drink? ",['1','2','3',"report"])) - 1
    else:
        users_choice = int(users_choice) - 1
    drink_name = list(menu_data.keys())[users_choice]
    drink_cost = menu_data[drink_name]["cost"]
    status_check = check_machine(drink_name)
    if status_check[0] < 0:
        print(f"Sorry, not ehough: {", ".join(status_check[1])}")
        break
    else:
        print(f"please pay ${drink_cost}")
    money_count(drink_cost, drink_name)
    for i in menu_data[drink_name]["ingridients"]:
        machine[i] -= menu_data[drink_name]["ingridients"][i]
    machine["money"] += drink_cost
    want_to_order = validate_user_input("Do you want anything else? ", ['yes','no'])
    if want_to_order == 'yes':
        continue
    else:
        print("Thanks and goodbye!")
        continue_to_use_machine = False
    
