import random

choice = ['papier', 'kamien', 'nozyce']
licznik_komputera = 0
licznik_usera = 0
while licznik_komputera < 3 and licznik_usera < 3:
  computer_choice = random.choice(choice)
  user_choice = input('Papier, kamien czy nozyce?')
  print(f'Komputer wybral{computer_choice}')
  if user_choice not in choice:
    print(f'co ty dajesz, podales {user_choice}')
  elif user_choice == computer_choice:
    print('remis. graj dalej')
  elif (user_choice == 'kamien' and computer_choice == 'nozyce') or (
      user_choice == 'papier'
      and computer_choice == 'kamien') or (user_choice == 'nozyce'
                                           and computer_choice == 'papier'):
    licznik_usera += 1
  else:
    licznik_komputera += 1

  if licznik_usera == 3:
    print('wygrales')
  elif licznik_komputera == 3:
    print('przegrales')
  else:
    print('graj dalej')