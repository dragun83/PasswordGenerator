#!/usr/bin/python3
import random
import argparse
random.seed()
alpha='abcdefghijklmnopqrstuvwxyz1234567890!@#$%&?-_'
pas=''

def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('Len',  nargs='?',default = 16,  type=int, help='Leng of password...')
    return parser

params = set_parser().parse_args()

for i in range(0, params.Len):
    maxlen = len(alpha)
    a = random.randint(0, maxlen - 1)
    c = random.randint(0, 1)
    if (c == 0):
        pas = pas + str(alpha[a])
    if (c == 1):
        pas = pas +  str(alpha[a]).upper()
print(pas)
