print("Welcome to Pizza py")
bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small_pizza = 2
pepperoni_med_large_pizza = 3
add_extracheese = 1

while True:
  size = input("Pizza size (S,M,L)? ").lower()
  if size in ['s','m','l']:
    break
  else:
    print("Please enter S, M or L")

while True:
  pepperoni = input("Add pepperoni?(Y,N)? ").lower()
  if pepperoni in ['y','n']:
    break
  else:
    print("Please enter Y, N")

while True:
  extracheese = input("Add extracheese?(Y,N)? ").lower()
  if extracheese in ['y','n']:
    break
  else:
    print("Please enter Y, N")

if size == 's':
  bill = small_pizza
elif size == 'm':
  bill = medium_pizza
else:
  bill = large_pizza

if pepperoni == 'y':
  if size == 's':
    bill += pepperoni_small_pizza
  else:
    bill += pepperoni_med_large_pizza

if extracheese == 'y':
  bill += add_extracheese

print(f"Your total bill is: {bill}$")
