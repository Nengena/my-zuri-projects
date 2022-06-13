import random

draws = 0
wins = 0
losses = 0
is_ended = 0
prompt = "(choose Rock(R), Paper(P) Scissors(S), or 'Q' to quit: "

while True:
    user_choice = input(prompt)
    while user_choice not in ['R', 'P', 'S', 'Q']:
        user_choice = input(prompt)
    if user_choice == 'Q' :
        break
    else:
        computer_choice = random.choice(['R', 'P', 'S'])
        if computer_choice == 'R':
            move = 'Rock'
        elif computer_choice == 'P':
            move = 'Paper'
        else:
            move = 'Scissors'
        print('computer ' + move)
        if computer_choice == user_choice:
            print('Draw')
        elif (computer_choice == 'R' and user_choice == 'P') or \
             (computer_choice == 'P' and user_choice == 'S') or\
             (computer_choice == 'S' and user_choice == 'R'):
             print('you win!')
             wins += 1
        else:
            print('you lose!')
            losses += 1
print('you have ' + str(wins) + str(draws) + 'draws, and '\
      + str(losses) + ' losses.') 
        