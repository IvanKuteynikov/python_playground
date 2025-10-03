print("Let's check number odd or even, to STOP enter 0 \n")
while True:
  try:
    number = int(input(f"\ninput any number: "))
  except ValueError: 
    print("Enter number please")
    continue
  if number == 0:
    break
  elif number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f"{number} is odd")