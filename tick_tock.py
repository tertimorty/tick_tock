# making a tick tack game
# 1.) create board
# 2.)update board
# 3.) make everything in seperate functions and game engine just /
# calls functions in order while game is valid
from colorama import *
import sys
from termcolor import colored, cprint
import time
empty_space = ' '


def tick_tock_game():
    '''this is simple tick tock game played in terminal '''
    # Generate board and tell that bame has started
    text = colored('Welcome to TICK TOCK game!!', 'cyan', attrs=['blink'])
    print(text)
    time.sleep(2)
    print(Fore.YELLOW + f'When you are ready insert position in which you \
whant your character')
    time.sleep(3)
    print(f'The one who makes three in a row wins!' + Style.RESET_ALL)
    time.sleep(2)

    # This is place where intro is finished and game begins, the x
    # initialized below is used to diferentiate between players to
    # know which ones turn it is
    wrong_choice_text = f'You can not place your tile in that space, choose \
another place'
    x = 1
    vin_condition = 0
    space_values = {'a1': empty_space, 'a2': empty_space, 'a3': empty_space,
                    'b1': empty_space, 'b2': empty_space, 'b3': empty_space,
                    'c1': empty_space, 'c2': empty_space, 'c3': empty_space}
    print_chooser(space_values)
    while True:
        # Games runtime part
        if x == 1:
            input_text = 'X'
            x = 0
            while True:
                place = input(f'Where do you whant to place {input_text}? ')
                try:
                    if space_values[place] == empty_space:
                        space_values[place] = 'X'
                        print_chooser(space_values)
                        break
                    elif space_values[place] != empty_space:
                        print(Fore.RED + wrong_choice_text + Style.RESET_ALL)
                except KeyError:
                    print(Fore.RED + f'You entered invalid adress' +
                            Style.RESET_ALL)

            vin_condition = check_for_victory(space_values)
            if vin_condition == 1:
                print(Fore.YELLOW + f'You won player {input_text}' + Style.RESET_ALL)
                break

        elif x == 0:
            input_text = 'O'
            x = 1
            while True:
                palce_o = input(f'Where do you whant to place {input_text}? ')
                try:
                    if space_values[palce_o] == empty_space:
                        space_values[palce_o] = 'O'
                        print_chooser(space_values)
                        break
                    elif space_values[palce_o] != empty_space:
                        print(Fore.RED + wrong_choice_text + Style.RESET_ALL)
                except KeyError:
                    print(Fore.RED + f'You entered invalid adress' +
                            Style.RESET_ALL)

            vin_condition = check_for_victory(space_values)
            if vin_condition == 1:
                print(Fore.YELLOW + f'You won player {input_text}' + Style.RESET_ALL)
                break


def print_red(input_str):
    print(Fore.RED + f'{input_str}', end="" + Style.RESET_ALL)


def print_blue(input_str):
    print(Fore.BLUE + f'{input_str}', end="" + Style.RESET_ALL)

def print_with_space(input_str):
    print(f'{input_str}', end="")


space_values = {'a1': empty_space, 'a2': empty_space, 'a3': empty_space,
                    'b1': empty_space, 'b2': empty_space, 'b3': empty_space,
                    'c1': empty_space, 'c2': empty_space, 'c3': empty_space}


def print_board(space_values):
    '''based on input and what not chooses which print to use for each of lines'''

    print(f"    a   b   c")
    print(f"  -------------")
    print_with_space(f"1 | ")
    print_red(f"{space_values['a1']}")
    print_with_space(f" | ")
    print_red(f"{space_values['b1']}")
    print_with_space(f" | ")
    print_red(f"{space_values['c1']}")
    print(f" | ")
    print(f"  -------------")
    print_with_space(f"2 | ")
    print_blue(f"{space_values['a2']}")
    print_with_space(f" | ")
    print_blue(f"{space_values['b2']}")
    print_with_space(f" | ")
    print_blue(f"{space_values['c2']}")
    print(f" | ")
    print(f"  -------------")
    print_with_space(f"3 | ")
    print_red(f"{space_values['a3']}")
    print_with_space(f" | ")
    print_red(f"{space_values['b3']}")
    print_with_space(f" | ")
    print_red(f"{space_values['c3']}")
    print(f" | ")
    print(f"  -------------")


def check_for_victory(space_values):
    '''This function contains all the win conditions of this game'''
    if space_values['a1'] == space_values['b1'] == space_values['c1'] and \
            space_values['a1'] != empty_space:
        return 1
    if space_values['a2'] == space_values['b2'] == space_values['c2'] and \
            space_values['a2'] != empty_space:
        return 1
    if space_values['a3'] == space_values['b3'] == space_values['c3'] and \
            space_values['a3'] != empty_space:
        return 1
    if space_values['a1'] == space_values['a2'] == space_values['a3'] and \
            space_values['a3'] != empty_space:
        return 1
    if space_values['b1'] == space_values['b2'] == space_values['b3'] and \
            space_values['b3'] != empty_space:
        return 1
    if space_values['c1'] == space_values['c2'] == space_values['c3'] and \
            space_values['c3'] != empty_space:
        return 1
    if space_values['a1'] == space_values['b2'] == space_values['c3'] and \
            space_values['c3'] != empty_space:
        return 1
    if space_values['a3'] == space_values['b2'] == space_values['c1'] and \
            space_values['c1'] != empty_space:
        return 1


# tick_tock_game()

def print_chooser(space_values):
    printable_list = ["    a   b   c", "  -------------"]
    for each in printable_list:
        print(f'{each}')
    print_with_space(f"1 | ")
    first_three = ['a1', 'b1', 'c1']
    for each in first_three:
        if space_values[each] == 'X':
            print_red(f"{space_values[each]}")
        elif space_values[each] == 'O':
            print_blue(f"{space_values[each]}")
        else:
            print_with_space(f"{space_values[each]}")
        print_with_space(f" | ")
    print(f'')
    print(f"  -------------")
    print_with_space(f"2 | ")
    second_three = ['a2', 'b2', 'c2']
    for each in second_three:
        if space_values[each] == 'X':
            print_red(f"{space_values[each]}")
        elif space_values[each] == 'O':
            print_blue(f"{space_values[each]}")
        else:
            print_with_space(f"{space_values[each]}")
        print_with_space(f" | ")
    print(f'')
    print(f"  -------------")
    print_with_space(f"3 | ")
    last_three = ['a3', 'b3', 'c3']
    for each in last_three:
        if space_values[each] == 'X':
            print_red(f"{space_values[each]}")
        elif space_values[each] == 'O':
            print_blue(f"{space_values[each]}")
        else:
            print_with_space(f"{space_values[each]}")
        print_with_space(f" | ")
    print(f'')
    print(f"  -------------")


tick_tock_game()
