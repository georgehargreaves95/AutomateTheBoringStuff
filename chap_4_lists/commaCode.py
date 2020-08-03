# Input a list separated by commas and print on a single line as a comma separated list

import sys


def print_comma_list(string_list: [str]):
    print_string = '\n'
    if len(string_list) == 0:
        print("\nYou gave me an empty list!\n")
    else:
        for index, item in enumerate(string_list):
            if item == '':
                continue
            if index == len(string_list) - 1:
                print_string += 'and ' + item
            else:
                print_string += item + ', '
        print(print_string)


def get_list_input():
    list_input = []
    print()
    while True:
        val = input("Enter a value: ")
        if val == 'STOP':
            sys.exit()
        elif val == 'PRINT':
            break
        else:
            list_input.append(val)
            continue
    print_comma_list(list_input)


def __main__():
    if __name__ == '__main__':
        print("Welcome to list printer! \nEnter your list and type PRINT to print. \nType STOP to exit")
        while True:
            get_list_input()
            cont = input("\nType Y to continue printing: ")
            if cont == 'Y':
                continue
            else:
                print("\nBye!")
                sys.exit()


__main__()
