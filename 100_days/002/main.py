print("Welcome to the tip calculator!")
bill = float(input(f"What was the total bill? $"))
percent = float(input(f"How much tip in percent would you like to give? 10, 12, or 15? "))
num_of_people = float(input(f"How many people to split the bill?? "))

per_people = round((bill * (1+percent/100))/num_of_people,2)
print(f"Each person should pay: ${per_people}")