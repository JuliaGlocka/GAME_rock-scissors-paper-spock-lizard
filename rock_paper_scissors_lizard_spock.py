import random

print('Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons spock, spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves spock, spock vaporizes rock, rock crushes scissors')
choice = ['paper', 'rock', 'scissors', 'lizard', 'spock']
licznik_komputera = 0
licznik_usera = 0

while licznik_komputera < 3 and licznik_usera < 3:
    computer_choice = random.choice(choice)
    user_choice = input('Paper, rock, scissors, lizard, or spock? ').lower()  # Convert user input to lowercase
    print(f'Computer chose {computer_choice}')

    if user_choice not in choice:
        print(f'Wrong, you have chosen {user_choice.capitalize()}!')  # Capitalize user input for display
    elif user_choice == computer_choice:
        print('Tie. Continue match.')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'lizard' and computer_choice == 'spock') or \
         (user_choice == 'spock' and computer_choice == 'scissors') or \
         (user_choice == 'rock' and computer_choice == 'lizard') or \
         (user_choice == 'paper' and computer_choice == 'spock') or \
         (user_choice == 'spock' and computer_choice == 'rock') or \
         (user_choice == 'lizard' and computer_choice == 'paper') or \
         (user_choice == 'scissors' and computer_choice == 'lizard'):
         licznik_usera += 1
    else:
        licznik_komputera += 1

if licznik_usera == 3:
    print('You win!')
elif licznik_komputera == 3:
    print('You lose!')
else:
    print('Continue match.')
