def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiple,
    "/": divide,
}


def calculation():
    calculation_continue = True
    n_x = 0 #n1 temporary storage for the next loop if user's answer will be yes to continue
    while calculation_continue:
        if n_x == 0:
            while True:
                try:
                    n1 = float(input("First number? ")) 
                    break
                except ValueError: 
                    print("Enter number please")
                    continue
        else: 
            n1 = n_x
        for o in operations:
            print(o)
        selected_operation = input("please choose kind of operation from the list above:\n")
        while True:
            try:
                n2 = float(input("Second number? "))
                if selected_operation == '/' and n2 == 0:
                    print("Error: You cannot divide by zero. Please try again.")
                    continue
                break
            except ValueError:
                print("Enter number please")
                continue
        result = operations[selected_operation](n1,n2)
        print(f"{n1} {selected_operation} {n2} = {result}")
        while True:
            ask_to_cont = input(f"Do you like to continue calculations with {result}? Print (Y/N)? ").lower()
            if ask_to_cont in ['y','n']:
                break
            else:
                print("Please enter only 'Y' or 'N'")
        if ask_to_cont == 'y':
            n_x = result
        else:
            calculation_continue = False

def main():
    calculator_work = True
    while calculator_work:
        try:
            while True:
                ask_user = input("Want to calculate something? (Y/N) ").lower()
                if ask_user in ['y','n']:
                    break
                else:
                    print("Please enter only 'Y' or 'N'")
            if ask_user == 'y':
                print("\n"*100)
                print(f"Welome to calculator")
                calculation()
            else:
                calculator_work = False
                print("Thanks and goodbye")
        except KeyboardInterrupt:
            print("\nBye")
            calculator_work = False


            
if __name__ == "__main__":
    main()