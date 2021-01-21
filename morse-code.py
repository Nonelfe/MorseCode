#!/usr/bin/env python3
#coding:utf-8

import argparse
from morse_tables import Morse
from os import path

if not path.exists('morse_tables.py'):
    print("\033[31mHave not 'morse_tables.py': file not found ERROR\033[0m")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--encode', help='input string')
parser.add_argument('-a', '--all', action='store_true', help='all print')
parser.add_argument('-v', '--verbose', action='store_true', help='Detail deiplay of results')
parser.add_argument('-d', '--decode', help='morse code decoding')
parser.add_argument('--wabun', action='store_true', help='morse code decoding wabun')
args = parser.parse_args()

print("--*-- MorseCode --*--")

def encode(n):
    if not Morse().error_check(n):
        return ()

    print("input: '{}'".format(n))
    result = Morse().encode(n)

    if args.verbose:
        view = dict(zip(list(n.replace(' ', '')), result.split()))
        for k, v in view.items():
            print("{0}:: {1}".format(k, v))
    else:
        print("{}".format(result))
    print()

def decode (n):
    print("input: '{}'".format(n))
    if args.wabun:
        result = Morse().decode(n, args.wabun)
    else:
        result = Morse().decode(n)
    print("result:{}".format(result))

def _All_View():
    print("--All view mode--")
    for key, value in Morse().MORSE_TABLES.items():
        print("key:{0}, value:{1}".format(key, value))
    print()

if __name__ == '__main__':
    if args.all:
        _All_View()
    elif args.encode and not args.decode:
        encode(args.encode)
    elif not args.encode and args.decode:
        decode(args.decode)
    else:
        print("'--input' and '--output' interfare it") 
