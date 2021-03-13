# making a tick tack game
# 1.) create board
# 2.)update board
# 3.) make everything in seperate functions and game engine just calls functions in order while game is valid
from colorama import *
import sys
from termcolor import colored, cprint
import time
empty_space = ' '


def tick_tock_game():
    '''this is simple tick tock game '''
    # Generate board and tell that bame has started
    text = colored('Welcome to TICK TOCK game!!', 'cyan', attrs=['blink'])
    print(text)
    time.sleep(2)
    print(Fore.YELLOW + f'When you are ready insert position in which you whant your \
character')
    time.sleep(3)
    print(f'The one who makes three in a row wins!' + Style.RESET_ALL)
    time.sleep(2)
    x = 1
    space_values = {'a1': empty_space, 'a2': empty_space, 'a3': empty_space,
                    'b1': empty_space, 'b2': empty_space, 'b3': empty_space,
                    'c1': empty_space, 'c2': empty_space, 'c3': empty_space}
    print_board(space_values)
    while True:
        # Games runtime part
        if x == 1:
            input_text = 'X'
            x = 0
            while True:
                place = input(f'Where do you whant to place {input_text}? ')
                if space_values[place] == empty_space:
                    space_values[place] = 'X'
                    print_board(space_values)
                    break
                else:
                    print(f'You can not place your tile in that space, choose \
another place')
            print(f'x part ends')
        elif x == 0:
            input_text = 'O'
            x = 1
            while True:
                palce_o = input(f'Where do you whant to place {input_text}? ')
                if space_values[palce_o] == empty_space:
                    space_values[palce_o] = 'O'
                    print_board(space_values)

                    break
                else:
                    print(f'You can not place your tile in that space, choose \
                    another place')


def print_board(space_values):
    print(f"    a   b   c\n  -------------\n1\
 | {space_values['a1']} | {space_values['b1']} | {space_values['c1']} \
|            \n  -------------\n\
2 | {space_values['a2']} | {space_values['b2']} | {space_values['c2']} |\
                \n  -------------\n\
3 | {space_values['a3']} | {space_values['b3']} | {space_values['c3']} |\
                \n  -------------\n")


space_values = {'a1': empty_space, 'a2': empty_space, 'a3': empty_space,
                    'b1': empty_space, 'b2': empty_space, 'b3': empty_space,
                    'c1': empty_space, 'c2': empty_space, 'c3': empty_space}


def check_for_victory(space_values):
    if space_values['a1'] == space_values['a1'] == space_values['a1'] \
    and space_values['a1'] == empty_space:
        print(f'you won!')


check_for_victory(space_values)
