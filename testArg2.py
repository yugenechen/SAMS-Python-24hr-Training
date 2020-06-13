# -*- coding: utf-8 -*-
"""Program explores using arguments in a compiled programm call or in a python \
program call from the command line.  Splits user input arguments into three \
groups:

1) Dictionary of named arguments (**kargs, named or keyed arguments).  
   form:  <name>=<value>
   example:  path="C:/Python/PythonScripts"
   Intended use:  Check against the dictionary keys for keyValues provided \
                  the user so that user input values are used instead of \
                  program default values.  
       example:  dirve = "C:\" # Default drive
                 User enters drive="D" and the program then detects the user \
                 entry and utilizes "D:\" as the root drive for accessing fiels \
                 (appending file paths and files to it as appropriate).
        
2) List of Switches (typically on/off switches for the program)
    form: -<SwitchName>
    example: -debug
    Intended use:  Set Switch options (i.e. turn on the option).  Program can \
                   search through the list and if a switch is detected then set \
                   the option on or utlize the option in the porgram.  In the \
                   "-debug" example this might turn on print statements in the
                   program for printing out info for troubleshooting.
                   
3) List of keywords to generate action in the program if the keywords are \
   detected.  Alternatively, might be used for freen entry text or special 
   handling of optional **args (un-named argument values).
        
        
Examples of use:
---------------
1) Script call from the command line:
    a. filename only:
       python testArg2.py fn=Add_Example_temp.py a=-3 b=-55 -echo baseball \
       names cheeks
    b. Full File pathname:
       python C:/python/PythonScripts/testArg2.py fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks
   
2) Executable (.exe) :
   testArg2 fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks

3) Python compiled file (.pyc)
       testArg2.pyc fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks

Authored Info:
-------------
Created on Fri Jun 12 16:11:33 2020

@author: ychen
"""

import sys
print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

myDict = {"Filename":sys.argv[0]}
mySwitches = []
keyWordList = []
for arg in sys.argv:
    if arg != sys.argv[0]:
        if "=" in arg:
            # Use zip method to create the dictionary
            iterator = iter(arg.split("="))
            myDict.update(dict(zip(iterator, iterator)))
        elif "-" in arg:
            mySwitches.append(arg)
        else:
            keyWordList.append(arg)
        
print("myDict: \n", myDict, "\n\n")
print("mySwitches: \n", mySwitches, "\n\n")
print("myList: \n", keyWordList, "\n\n")

"""Run the following line from the DOS command line within the directory 
   containing the pythone script file (in this case "testArg2.py"):
python testArg2.py fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks

    Alternatively, run the test from any directory and provide the FullPathFilename:
python C:/python/PythonScripts/testArg2.py fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks
"""