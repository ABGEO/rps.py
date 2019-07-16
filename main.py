#!/usr/bin/python
"""
Module main.py
"""
from os import system, name
from time import sleep
import random

OBJECTS = {
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

SCORES = [0, 0]


def clear():
    """
    Clear screen.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def print_logo():
    """
    Print application logo.
    """
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
    """
    Print game animation.
    """
    for _, item in OBJECTS.items():
        print(item['icon'])
        sleep(0.5)
        clear()


def get_user_input():
    """
    Get user's selected game object.
    """
    first = True
    while True:
        clear()

        if not first:
            print('Invalid input. Please, select existing object (r, p, s)!')

        first = False

        selected = input('Select Rock(r), Paper(p) or Scissors(s): ')

        if selected in ['r', 'p', 's']:
            return selected


def get_winner(player1, player2):
    """
    Return winner from given players.
    """
    w_1 = player1['weight']
    w_2 = player2['weight']

    if w_1 == w_2:
        return 0
    elif (w_1 - w_2) % 3 == 1:
        SCORES[0] += 1
        return 1
    else:
        SCORES[1] += 1
        return 2


def main():
    """
    Application main function.
    """
    clear()
    print_animation()
    clear()
    print_logo()

    win_titles = ['Tie', 'You win', 'Computer wins']

    while True:
        start_action = input('\nPress any key to start or q for exit...')

        if start_action in ['q', 'Q', 'exit', 'quit']:
            exit()

        user_input = get_user_input()
        user_object = OBJECTS.get(user_input)
        comp_object = OBJECTS.get(random.choice(['r', 'p', 's']))

        print(
            user_object['title'] + ' (YOU) ' + user_object['icon'] +
            ' \n\n\tVS \n\n' +
            comp_object['title'] + ' (COMPUTER) ' + comp_object['icon']
        )

        winner = get_winner(user_object, comp_object)

        print('\n' + win_titles[winner])

        print('\n\nScore:\n\t(YOU) ' + str(SCORES[0]) + ':' + str(SCORES[1]) + ' (COMPUTER)')


if __name__ == '__main__':
    main()
