#!/usr/bin/python3

import sys

try:
    if sys.argv[1] == 'a':
        print(float(sys.argv[2]) + float(sys.argv[3]))
    if sys.argv[1] == 'd':
        print(float(sys.argv[2]) / float(sys.argv[3]))
    if sys.argv[1] == 'm':
        print(float(sys.argv[2]) * float(sys.argv[3]))
    if sys.argv[1] == 's':
        print(float(sys.argv[2]) - float(sys.argv[3]))
except:
    print('You need to specify numbers to operate with.')
