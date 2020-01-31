import sys
from cpu import *

cpu = CPU()

if len(sys.argv) < 2:
    print('Give me a program to run, puny human.')
else:
    cpu.load(sys.argv[1])
    cpu.run() 