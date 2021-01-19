#coding:utf-8

import argparse
from morse_tables import Morse
from os import path

if not path.exists('morse_tables.py'):
    print("\033[31mHave not 'morse_tables.py': file not found ERROR\033[0m")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input string')
parser.add_argument('-a', '--all', action='store_true', help='all print')
parser.add_argument('-v', '--verbose', action='store_true', help='explain what is being done')
args = parser.parse_args()

print("--*-- MorseCode --*--")

def main(n):
    if not Morse().error_check(n):
        return ()

    print("input: '{}'".format(n))
    n_str = n.replace(' ', '')
    for s in list(n_str):
        if s.isalpha():
            s = s.upper()
        get_value = Morse().MORSE_TABLES.get(s)
        if args.verbose:
            print("{0}:: {1}".format(s, get_value))
        else:
            print("{}".format(get_value),end='')
            print(' ',end='')
    print()

def _All_View():
    print("--All view mode--")
    for key, value in Morse().MORSE_TABLES.items():
        print("key:{0}, value:{1}".format(key, value))
    print()

if __name__ == '__main__':
    if args.all:
        _All_View()
    else:
        main(args.input)
