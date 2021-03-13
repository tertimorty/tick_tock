from colorama import *
import sys
from termcolor import colored, cprint
import time
empty_space = ' '


def tick_tock_game():
    '''this is simple tick tock game played in terminal '''
    # Generate board and tell that game has started
    text = colored('Welcome to TICK TOCK game!!', 'cyan', attrs=['blink'])
    print(text)
    time.sleep(1)
    print(Fore.YELLOW + f'When you are ready insert position in which you \
whant your character')
    time.sleep(1)
    print(f'The one who makes three in a row wins!' + Style.RESET_ALL)
    time.sleep(1)
    wrong_choice_text = f'You can not place your tile in that space, choose \
another place'
    invalid_a_txt = f'You entered invalid adress'
    w_txt = f'You Won player '
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
                place_x = input(f'Where do you whant to place {input_text}? ')
                try:
                    if space_values[place_x] == empty_space:
                        space_values[place_x] = 'X'
                        print_chooser(space_values)
                        break
                    elif space_values[place_x] != empty_space:
                        print(Fore.RED + wrong_choice_text + Style.RESET_ALL)
                except KeyError:
                    print(Fore.RED + invalid_a_txt + Style.RESET_ALL)

            if check_for_victory(space_values) == 1:
                print(Fore.YELLOW + w_txt + f'{input_text}' + Style.RESET_ALL)
                play_again1 = play_again(space_values)
                if play_again1 != 'y':
                    break
                else:
                    print_chooser(space_values)
            if check_for_draw(space_values) != 1:
                print(Fore.YELLOW + f'This is a draw' + Style.RESET_ALL)
                play_again1 = play_again(space_values)
                if play_again1 != 'y':
                    break
                else:
                    print_chooser(space_values)

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
                    print(Fore.RED + invalid_a_txt + Style.RESET_ALL)

            if check_for_victory(space_values) == 1:
                print(Fore.YELLOW + w_txt + f'{input_text}' + Style.RESET_ALL)
                play_again1 = play_again(space_values)
                if play_again1 != 'y':
                    break
                else:
                    print_chooser(space_values)
            if check_for_draw(space_values) != 1:
                print(Fore.YELLOW + f'This is a draw' + Style.RESET_ALL)
                play_again1 = play_again(space_values)
                if play_again1 != 'y':
                    break
                else:
                    print_chooser(space_values)


def print_red(input_str):
    print(Fore.RED + f'{input_str}', end="" + Style.RESET_ALL)


def print_blue(input_str):
    print(Fore.BLUE + f'{input_str}', end="" + Style.RESET_ALL)


def print_with_space(input_str):
    print(f'{input_str}', end="")


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


def check_for_draw(space_values):
    '''This function checks if there is draw'''
    for key in space_values:
        if space_values[key] == ' ':
            return 1


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


def play_again(space_values):
    play_again = input('Do you want to play again y/n?')
    if play_again == 'y':
        for key in space_values:
            space_values[key] = empty_space
        return 'y'


tick_tock_game()
