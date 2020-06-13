# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
It is an example of how ot create an executable that accepts arguments:
    1.  Create an executable by running:  "pyinstaller temp.py" from command line.
    2.  Test it by running the .exe from the command line.  Use something like-
        Add_Example_temp(5,9)
        should return 14
        python "c:\python\PythonScripts\Add_Example_Temp.py" 5 9 
    3.  from pathlib import Path
"""

import sys

def main(A,B):
    return A + B



# ----------------------------
# Script Catch at end of file
# ----------------------------
if __name__ == "__main__":
    print("\nHello World!!\n")
    print ("Length = " , len(sys.argv))
    print("argv[0] = FullPathFilename:  ", sys.argv[0])
    #print("argv[1] = first argument value:  ", sys.argv[1])
    #print("argv[1] = first argument value:  ", sys.argv[2])
    print("The list of arguments is as follows:")
    val=[]
    for arg in sys.argv:
        print(arg)
        val.append(arg)
    NotANumber = False    
    if len(val) == 3:
        # strip the "-" on the nubmer check so negative values can be used
        if val[1].lstrip("-").isdecimal():
            A = int(float(val[1]))
            print("A = ", A)
        else:
            NotANumber = True
        if val[2].lstrip("-").isnumeric():
            B = int(float(val[2]))
            print("B = ", B)
        else:
            NotANumber = True
        if NotANumber:
            print("Invalid arguments; they were not integers.  Please try again")
        else:
            print("C =  A + B = ", main(A, B))
