
print('Welcome to Treasure Island. Your mission is to find the treasure.')
print('Your mission is to find the treasure.')

while True:
  print('You are at the crossroad, where do you want to go?')
  while True:
    choice = input('"LEFT" or "RIGHT"? ').lower()
    if choice in ['left', 'right']:
      break

  if choice == 'right':
    print('\nYou fall into a hole, GAME OVER!')

  if choice == 'left':
    print('\nIn front of you lake?')
    print('You could wait for the boat or swim accross?')

    while True:
      choice = input('"SWIM" or "WAIT"? ').lower()
      if choice in ['swim', 'wait']:
        break
      
    if choice == 'swim':
      print('\nAttacked by trout. GAME OVER!')

    if choice == 'wait':
      print('\nIn front of you three doors?')
      print('Red, blue, yellow, which do you choose?')

      while True:
        choice = input('"RED", "BLUE" or "YELLOW"? ').lower()
        if choice in ['red', 'blue', 'yellow']:
          break

      if choice == 'red':
        print('\nBurned by fire. GAME OVER!')

      elif choice == 'blue':
        print('\nEaten by beasts. GAME OVER!')

      else:
        print("\nYou won!")
  restart_choice = ''
  while restart_choice not in ['y', 'n']:
    restart_choice = input('\nPlay again (Y/N)? ').lower()
  if restart_choice == 'n':
    print("Thanks for playing")
    break
  if restart_choice == 'y':
    continue








