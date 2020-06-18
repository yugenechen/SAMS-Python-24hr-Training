# -*- coding: utf-8 -*-
"""
Explore sending arguements to an executable.
[0] is always the name of the python file [<python>.py] run by python
    ex. python c:/project/python/myProgram.py
    argv[0] = c:/project/python/myProgram.py
[1..n] are the arguments fed to the <python>.py program
"""
import os
import sys
sys.path.append(os.getcwd() + "/packages")
import packages.ytcLibrary as ytc

def main(A, B):
    return A + B

# Script Catch at end of file
if __name__ == "__main__":
    print("\nHello World!\n")

    i = 0
    for arg in sys.argv:
        print("argv[" + str(i) + "] = ", arg)
        i += 1

    if len(sys.argv) > 1:
        if (sys.argv[1].isdecimal or  ytc.isfloat(sys.argv[1])):
            A =  ytc.str_to_float_or_int(sys.argv[1])
    if len(sys.argv) > 2:
        if (sys.argv[2].isdecimal or  ytc.isfloat(sys.argv[2])):
            B = int(float(sys.argv[2]))

            print("\nC = A + B = ", main(A, B))
"""
Lastly,
1. create an executable by running:  "pyinstaller temp.py" from command line.
2. test it by running the temp.exe from command line:
   python d:/projects/python/temp.exe 5 9
"""
