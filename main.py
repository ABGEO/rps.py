from os import system, name
from time import sleep
import random

objects = {
    'r': {
        'title': 'Rock',
        'icon': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        'weight': 3
    },
    'p': {
        'title': 'Paper',
        'icon': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        'weight': 1
    },
    's': {
        'title': 'Scissors',
        'icon': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
        'weight': 2
    }
}

score = [0, 0]


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def print_logo():
    print("""
Welcome to
 _ __ _ __  ___   _ __  _   _ 
| '__| '_ \\/ __| | '_ \\| | | |
| |  | |_) \\__ \\_| |_) | |_| |
|_|  | .__/|___(_) .__/ \\__, |
     |_|         |_|    |___/ 
(Rock, Paper, Scissors) v1.0.0
""")


def print_animation():
    for k, v in objects.items():
        print(v['icon'])
        sleep(0.5)
        clear()


def get_user_input():
    first = True
    while True:
        clear()

        if not first:
            print('Invalid input. Please, select existing object (r, p, s)!')

        first = False

        selected = input('Select Rock(r), Paper(p) or Scissors(s): ')

        if selected == 'r' or selected == 'p' or selected == 's':
            return selected


def get_winner(player1, player2):
    w1 = player1['weight']
    w2 = player2['weight']

    if w1 == w2:
        return 0
    elif (w1 - w2) % 3 == 1:
        score[0] += 1
        return 1
    else:
        score[1] += 1
        return 2


def main():
    clear()
    print_animation()
    clear()
    print_logo()

    win_titles = ['Tie', 'You win', 'Computer wins']

    while True:
        start_action = input('\nPress any key to start or q for exit...')

        if start_action == 'q' or start_action == 'Q':
            exit()

        user_input = get_user_input()
        user_object = objects.get(user_input)
        comp_object = objects.get(random.choice(['r', 'p', 's']))

        print(
            user_object['title'] + ' (YOU) ' + user_object['icon'] +
            ' \n\n\tVS \n\n' +
            comp_object['title'] + ' (COMPUTER) ' + comp_object['icon']
        )

        winner = get_winner(user_object, comp_object)

        print('\n' + win_titles[winner])

        print('\n\nScore:\n\t(YOU) ' + str(score[0]) + ':' + str(score[1]) + ' (COMPUTER)')


if __name__ == '__main__':
    main()
